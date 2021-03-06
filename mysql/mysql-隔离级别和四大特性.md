## mysql
### mysql四大特性和隔离级别
#### 四大特性
* 原子性
原子性是指事务包含的所有操作要么全部成功，要么全部失败回滚，简单来说，事务是一个整体，不可分割。
* 一致性
一致性是指事务必须使数据库从一个一致性状态变换到另一个一致性状态，也就是说一个事务执行之前和执行之后都必须处于一致性状态，保证规则的一致。
* 隔离性
隔离性是当多个用户并发访问数据库时，比如操作同一张表时，数据库为每一个用户开启的事务，不能被其他事务的操作所干扰，多个并发事务之间要相互隔离。
* 持久性
持久性是指一个事务一旦被提交了，那么对数据库中的数据的改变就是永久性的，即便是在数据库系统遇到故障的情况下也不会丢失提交事务的操作。
#### 隔离级别
* 可能的问题
    * **脏读**： 一个事务处理过程里读取了另一个未提交的事务中的数据。
    * **不可重复读**: （针对其他提交前后，读取数据本身的对比） 一个事务范围内多次查询却返回了不同的数据值，这是由于在查询间隔，被另一个事务修改并提交了。
    * **幻读**： （针对其他提交前后，读取数据条数的对比） 幻读是指同样一笔查询在整个事务过程中多次执行后，查询所得的结果集是不一样的。幻读针对的是多笔记录。
* 四种隔离级别
    现在来看看MySQL数据库为我们提供的四种隔离级别：
    *  Serializable (串行化)：可避免脏读、不可重复读、幻读的发生。
    * Repeatable read (可重复读)：可避免脏读、不可重复读的发生。
    > 在一条记录上的操作时，不能读取已由其它事务修改了但是未提交的行，其它任何事务也不能修改在当前事务完成之前由当前事务读取的数据。但是对于其它事务插入的新行数据，当前事务第二次访问表行时会检索这一新行。因此，这一个隔离级别的设置解决了 Non-Repeatable Reads 不可重复读取的问题，但是避免不了 Phantom Reads 幻读。
    * Read committed (读已提交)：可避免脏读的发生。
    * Read uncommitted (读未提交)：最低级别，任何情况都无法保证。
**说明**：读提交在读取一条记录时会出现不可重复读，而可重复度通过对事务里面的写操作加锁，读操作使用快照，解决了度提交的问题，但是对统计某个范围内的记录数量，还是会产生幻读。

