## java多线程
### sync和reenlock的差别
1. sync为关键字   reenlock为对象
2. sync是内部排他锁, reenlock大量使用CAS(AQS模型和park())
3. sync对象阻塞后，无法通过interupt中断释放， reenlock的lockInterruptibly()方法实现阻塞的中断（显示锁的特点）
4. reenTrantLock可以对锁进行监控，获取锁的状态，需要手动释放锁资源，同时允许公平策略，灵活性高
