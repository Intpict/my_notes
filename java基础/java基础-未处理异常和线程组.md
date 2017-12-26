## java基础
### 未处理异常和线程组

1. 未处理异常 
    如果异常没有被捕获该`线程将会停止执行`。  
    Thread.UncaughtExceptionHandler是用于处理未捕获异常造成线程突然中断情况的一个内嵌接口。  
    当一个未捕获异常将造成线程中断的时候JVM会使用，Thread.getUncaughtExceptionHandler()来查询线程的uncaughtExceptionHandler，通过Thread.setUncaughtExceptionHandler设置，并将线程和异常作为参数传递给该handler的uncaughtException()方法进行处理。如果uncaughtExceptionHandler为空，线程默认的handler方法为所在ThreadGroup的uncaughtException方法。
    说明：  
    而在线程组中，因为ThreadGroup类也实现了Thread.UncaughtExceptionHandler接口，所以线程组会成为默认的异常处理器。

    线程组处理异常的流程如下:  
    * 如果该线程组有父线程组，则调用父线程组的uncaughtException方法来处理异常
    * 如果线程类有默认异常处理器，则用该异常处理器处理异常
    * 如果异常对象不是ThreadDeath，就会打印异常信息，并结束该线程  
2. 线程组
    Java中的ThreadGroup类表示线程组，在创建新线程时，可以通过构造函数Thread(group...)来指定线程组。  
    线程组具有以下特征：  
    * 如果没有显式指定线程组，则新线程属于默认线程组，默认情况下，与创建线程所在的组相同
    * 一旦确定了线程所在线程组之后，不允许更改线程组，直到线程死亡
    * 对于线程组ThreadGroup的一个对象，就表示一个线程组，线程组通过ThreadGroup(group...)来初始化
    * 线程组可以通过interrput(), setDamemon()，setMaxPriority()等方法来操作组内线程，通过activeCount()，isDamemon()来获取线程信息