## java基础
### newInstance使用
1. 通过反射创建新的类示例，有两种方式：  
* Class.newInstance() 
* Constructor.newInstance() 

2. 以下对两种调用方式给以比较说明： 
* Class.newInstance() 只能够调用无参的构造函数，即默认的构造函数； 
* Constructor.newInstance() 可以根据传入的参数，调用任意构造构造函数。 

3. Class.newInstance() 抛出所有由被调用构造函数抛出的异常。 
* Class.newInstance() 要求被调用的构造函数是可见的，也即必须是public类型的; 
* Constructor.newInstance() 在特定的情况下，可以调用私有的构造函数。 