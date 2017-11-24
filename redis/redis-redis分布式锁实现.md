##redis
###redis分布式锁实现
####redis 2.6版本之前
1. 需要的命令  
SETNX lock.foo \<current Unix time + lock timeout + 1\>  
GETSET lock.foo \<current Unix timestamp + lock timeout + 1\>
2. 现象描述  
如果只用SETNX指令：考虑一种情况，如果进程获得锁后，断开了与 Redis 的连接（可能是进程挂掉，或者网络中断），如果没有有效的释放锁的机制，那么其他进程都会处于一直等待的状态，即出现“死锁”。
3. 解决方案  
在使用 SETNX 获得锁时，我们将键 lock.foo 的值设置为锁的有效时间，进程获得锁后，其他进程还会不断的检测锁是否已超时，如果超时，那么等待的进程也将有机会获得锁。
4. 具体策略  
假设进程P1已经首先获得了锁 lock.foo，然后进程P1挂掉了。接下来的情况：

	* 进程P4执行 SETNX lock.foo 以尝试获取锁
由于进程P1已获得了锁，所以P4执行 SETNX lock.foo 返回0，即获取锁失败
	* P4执行 GET lock.foo 来检测锁是否已超时，如果没超时，则等待一段时间，再次检测
	* 如果P4检测到锁已超时，即当前的时间大于键 lock.foo 的值，P4会执行以下操作 
GETSET lock.foo \<current Unix timestamp + lock timeout + 1\>由于 GETSET 操作在设置键的值的同时，还会返回键的旧值，通过比较键 lock.foo 的旧值是否与之前获取的值相等，可以判断进程是否已获得锁
	* 假如另一个进程P5也检测到锁已超时，并在P4之前执行了 GETSET 操作，那么P4的 GETSET 操作返回的是一个大于当前时间的时间戳，这样P4就不会获得锁而继续等待。注意到，`即使P4接下来将键 lock.foo 的值设置了比P5设置的更大的值也没影响`。
	* 在进程释放锁，即执行 DEL lock.foo 操作前，需要`先判断锁是否已超时`。如果锁已超时，那么锁可能已由其他进程获得，这时直接执行 DEL lock.foo 操作会导致把其他进程已获得的锁释放掉。
5. python伪代码  

```
LOCK_TIMEOUT = 3
lock = 0
lock_timeout = 0
lock_key = 'lock.foo'

# 获取锁
while True:
    now = int(time.time())
    lock_timeout = now + LOCK_TIMEOUT + 1
    lock = redis_client.setnx(lock_key, lock_timeout)
    if lock == 1:
        break
    else:
        old_time1 = redis_client.get(lock_key)
        if old_time1:
            old_time1 = int(old_time1)
            if now > old_time1:
                old_time2 = redis_client.getset(lock_key, lock_timeout)
                # 不为none 且 与old_time1值相等，说明该进程为第一次修改它
                if old_time2 and old_time1 == int(old_time2):
                    break
    time.sleep(0.001)

# 已获得锁
do_job()

# 释放锁
now = int(time.time())
if now < lock_timeout:
    redis_client.delete(lock_key)
```

####redis 2.6版本之后
使用一个命令即可：SET key value [EX seconds] [NX]。其中，可选参数EX second ：设置键的过期时间为 second 秒；NX ：只在键不存在时，才对键进行设置操作。这个命令相当于2.6.12之前的setNx和expire两个命令的原子操作命令。

