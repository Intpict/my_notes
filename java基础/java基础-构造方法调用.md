## java基础
### 构造方法调用
1. 调用顺序: 在创建子类的对象时，Java虚拟机首先执行父类的构造方法，然后再执行子类的构造方法。在多级继承的情况下，将从继承树的最上层的父类开始，依次执行各个类的构造方法，这可以保证子类对象从所有直接或间接父类中继承的实例变量都被正确地初始化。
2. 构造函数不能继承，只是调用而已。如果父类没有无参构造函数创建子类时，不能编译，除非在构造函数代码体中第一行，必须是第一行显式调用父类有参构造函数。也就是说：系统会自动先调用父类的无参构造函数。