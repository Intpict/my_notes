## java源码
### ArrayBlockingQueue、LinkedBlockingQueue、SynchronousQueue  
* SynchronousQueue  
    * SynchronousQueue是无界的，是一种无缓冲的等待队列，但是由于该Queue本身的特性，在某次添加元素后必须等待其他线程取走后才能继续添加；可以认为SynchronousQueue是一个缓存值为1的阻塞队列，但是 isEmpty()方法永远返回是true，remainingCapacity() 方法永远返回是0，remove()和removeAll() 方法永远返回是false，iterator()方法永远返回空，peek()方法永远返回null。
    *  声明一个SynchronousQueue有两种不同的方式，它们之间有着不太一样的行为。公平模式和非公平模式的区别:如果采用公平模式：SynchronousQueue会采用公平锁，并配合一个FIFO队列来阻塞多余的生产者和消费者，从而体系整体的公平策略；但如果是非公平模式（SynchronousQueue默认）：SynchronousQueue采用非公平锁，同时配合一个LIFO队列来管理多余的生产者和消费者，而后一种模式，如果生产者和消费者的处理速度有差距，则很容易出现饥渴的情况，即可能有某些生产者或者是消费者的数据永远都得不到处理。

* LinkedBlockingQueue
    * LinkedBlockingQueue是无界的，是一个无界缓存的等待队列。基于链表的阻塞队列，内部维持着一个数据缓冲队列（该队列由链表构成）。当生产者往队列中放入一个数据时，队列会从生产者手中获取数据，并缓存在队列内部，而生产者立即返回；只有当队列缓冲区达到最大值缓存容量时（LinkedBlockingQueue可以通过构造函数指定该值），才会阻塞生产者队列，直到消费者从队列中消费掉一份数据，生产者线程会被唤醒，反之对于消费者这端的处理也基于同样的原理。
    * LinkedBlockingQueue之所以能够高效的处理并发数据，还因为其对于生产者端和消费者端分别采用了独立的锁来控制数据同步，这也意味着在高并发的情况下生产者和消费者可以并行地操作队列中的数据，以此来提高整个队列的并发性能。

* ArrayListBlockingQueue
    * ArrayListBlockingQueue是有界的，是一个有界缓存的等待队列。 基于数组的阻塞队列，同LinkedBlockingQueue类似，内部维持着一个定长数据缓冲队列（该队列由数组构成）。ArrayBlockingQueue内部还保存着两个整形变量，分别标识着队列的头部和尾部在数组中的位置。
    * ArrayBlockingQueue在生产者放入数据和消费者获取数据，都是共用同一个锁对象，由此也意味着两者无法真正并行运行，这点尤其不同于LinkedBlockingQueue；按照实现原理来分析，ArrayBlockingQueue完全可以采用分离锁，从而实现生产者和消费者操作的完全并行运行。Doug Lea之所以没这样去做，也许是因为ArrayBlockingQueue的数据写入和获取操作已经足够轻巧，以至于引入独立的锁机制，除了给代码带来额外的复杂性外，其在性能上完全占不到任何便宜。
    *  ArrayBlockingQueue和LinkedBlockingQueue间还有一个明显的不同之处在于，前者在插入或删除元素时不会产生或销毁任何额外的对象实例，而后者则会生成一个额外的Node对象。这在长时间内需要高效并发地处理大批量数据的系统中，其对于GC的影响还是存在一定的区别。