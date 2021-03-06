## java基础
### equals()方法重写的一般步骤

1. 使用==操作符检查“实参是否为指向对象的一个引用”。
2. 使用instanceof操作符检查“实参是否为正确的类型”。 
3. 把实参转换到正确的类型。 
4. 对于该类中每一个“关键”域，检查实参中的域与当前对象中对应的域值是否匹配。
    * 对于既不是float也不是double类型的基本类型的域，可以使用==操作符进行比较
    * 对于对象引用类型的域，可以递归地调用所引用的对象的equals方法 
    * 对于float类型的域，先使用`Float.floatToIntBits转换成int类型的值`，然后使用==操作符比较int类型的值
    * 对于double类型的域，先使用`Double.doubleToLongBits转换成long类型的值`，然后使用==操作符比较long类型的值。
5. 当你编写完成了equals方法之后，应该问自己三个问题：它是否是对称的、传递的、一致的？(其他两个特性通常会自行满足)    如果答案是否定的，那么请找到这些特性未能满足的原因，再修改equals方法的代码。