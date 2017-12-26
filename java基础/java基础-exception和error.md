## java基础
### exception和error
1. 简介  
* Error是程序无法处理的错误，比如OutOfMemoryError、ThreadDeath等。这些异常发生时，Java虚拟机（JVM）一般会选择线程终止。  * Exception是程序本身可以处理的异常，这种异常分两大类：
    * 非运行时异常（发生在编译阶段，又称checkException)一般就是指一些没有遵守Java语言规范的代码，容易看的出来，并且容易解决的异常，
    * 运行时异常（发生在程序运行过程中，又叫uncheckException）是那些在程序运行过程中产生的异常，具有不确定性，如空指针异常等
2. 异常处理  
    建议语法：
    ```
    try {
        try {

        } finally {
            // 关闭资源
        }
    } catch () {
            // 捕获异常
    }
    ```
3. finally及时`在return后也会执行`。