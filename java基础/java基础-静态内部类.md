## java基础
### 静态内部类
1. 静态内部类可以有静态成员(方法，属性)，而非静态内部类则不能有静态成员(方法，属性)。 
2. 静态内部类只能够访问外部类的静态成员,而非静态内部类则可以访问外部类的所有成员(方法，属性)。 
3. 实例化一个非静态的内部类的方法： 
   * 先生成一个外部类对象实例 
   * 通过外部类的对象实例生成内部类对象 
4. 实例化一个静态内部类的方法： 
   * 不依赖于外部类的实例,直接实例化内部类对象 
   * 调用内部静态类的方法或静态变量,通过类名直接调用 
5. 静态内部类，没有执行外部类的指针，节省空间。
6. 静态类的说明：静态类只能是内部类，外部的静态类无法通过编译。
7. 内部类（无论是否为静态）可实现延迟加载（也就是用到的时候才会加载），静态内部类可实现延迟加载的单例模式
```
package cn.okc.demo;  
  
public class Singleton {  
    // 静态内部类实现单例  
    private static class Inner {  
        // 单例对象  
        private static Singleton singleton = new Singleton();  
        // 类加载分为加载、链接、初始化三大步骤  
        // 其中链接又分为验证、准备和解析三小个步骤  
        // 类中静态的内容在编译阶段都会被编译到类构造函数<clinit>()中，在初始化步骤调用  
        // 因此这个代码块的调用标志着内部类被初始化了  
        static {  
            System.out.println("内部类被解析了");  
        }  
    }  
  
    // 私有化构造函数  
    private Singleton() {  
        // 判断单例对象是否已经存在，用于控制非法反射单例类的构造函数  
        if (Inner.singleton != null)  
            try {  
                throw new IllegalAccessException("单例对象已经被实例化，请不要非法反射构造函数");  
            } catch (IllegalAccessException e) {  
                e.printStackTrace();  
            }  
    }  
  
    // 合法获取单例对象的途径  
    public static Singleton getInstance() {  
        return Inner.singleton;  
    }  
}  
```