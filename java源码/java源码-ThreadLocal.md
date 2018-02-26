 以前我以为，只要是被WeakReference引用的对象，在下一次gc()的时候就会被回收掉，这是不对的。
 还少了一个条件，就是WeakReference引用的对象不再被其他外部对象引用的时候，
 那么，WeakReference引用的对象在下一次gc()的时候就会被回收掉。
 看看这段代码，ThreadLocal的经典实用方式，但这里面有一些以前没考虑到的地方。

 threadSession是一个类的静态成员变量，就是说threadSession在程序运行过程中，不会存在不被引用的情况，
 所以即使threadSession被WeakReference引用，
 但绝对不会被gc()销毁。因此不用考虑ThreadLocalMap的Entity的key==null的情况。
 为什么ThreadLocalMap不是map？
 个人理解，如果ThreadLocalMap是map，那么怎么让虚拟机销毁不再使用资源？虽然可以通过其他的技术手段来销毁，但毕竟增加了工作量，
 而jdk提供这么好用的WeakReference，为什么不使用呢？而且ThreadLocalMap是一个内部类，很明显，就是为了ThreadLocel而设计的。

