## java基础
### 泛型使用注意点

* java中没法得到泛型参数化类型，因为在编译期没法确定泛型参数化类型，也就找不到对应的类字节码文件，所以`无法使用new T`。
* Java中的泛型基本上都是在编译器这个层次来实现的。在生成的Java字节码中是不包含泛型中的类型信息的。使用泛型的时候加上的类型参数，会在编译器在编译的时候去掉。这个过程就称为类型擦除。
* [泛型生存时间](http://blog.csdn.net/u014143369/article/details/52863229)
*  由于泛型的类型擦除，List<Integer>，List<String>与List在运行期并没有区别，所以List<String>放入List<Integer>并不会产生ArrayStoreException异常。因此，`不能创建泛型数s组`