sleep， 进入TIMED_WAITING状态，不出让锁

wait, 进入TIMED_WAITING状态，出让锁，并进入对象的等待队列

park, 进入WAITING状态，对比wait不需要获得锁就可以让线程WAITING，通过unpark唤醒

interrupt, 只是给线程发个信号，如果在wait, sleep会收到exception

yeild, 在操作系统层面让线程从running变成ready状态，等待继续被调度。在jvm的线程状态还是RUNNABLE

https://www.cnblogs.com/23lalala/p/6214356.html
https://blog.csdn.net/ywk253100/article/details/29591755