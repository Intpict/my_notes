下面是详细步骤：

1. 首先确定进程的 ID ，可以使用 jps -v 或者 top 命令直接查看

2. 查看该进程中哪个线程占用大量 CPU，执行 top -H -p [PID] 结果如下：

分析占用了大量 CPU 处理时间的是Java 进程中哪个线程

可以发现编号为 350xx 的共有 9 个线程占用了 100% 的 CPU，好，接下来咱们随便取一个线程 ID ，假设我们想看编号为 35053 这个线程。

首先将 35053 转成 16 进制是 88ED （可以用开源中国在线工具转换）

3. 接下来我们将进程中的所有线程输出到一个文件中，执行：jstack [PID] > jstack.txt

4. 在进程中查找对应的线程 ID，执行：cat jstack.txt | grep -i 88ED

结果是：

"HTTP Request From : /xxxx/blog/323432(120.27.143.239)" #266 daemon prio=5 os_prio=0 tid=0x00007fcda4146800 nid=0x88e runnable [0x00007fcd54178000]
由此可以看出在请求 /xxxx/blog/323432 链接的时候，服务器的处理线程占用了 100% 的 CPU。