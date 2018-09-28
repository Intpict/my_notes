## java基础
### java序列化
#### 简介：
1. Java序列化，就是指将一个对象转化为二进制的byte流（注意，不是bit流），然后以文件的方式进行保存。
2. 序列化操作：将对象保存至文件；
3. 反序列化操作：从文件恢复出对象；
#### 配置: 
1. 对象如果要序列化，则必须集成Serializable接口；
2. 在实现序列化时，用ObjectOutputStream实现；
3. 而反序列化时，用ObjectInputStream实现；
#### 方法：
1. 序列化：
* public ObjectOutputStream(OutputStream out) throws IOException
* public final void writeObject(Object obj)
* public void close() throws IOException

2. 反序列化：
* public ObjectInputStream(InputStream in) throws IOException
* public final void readObject(Object obj)
* public void close() throws IOException


#### 注意：
Java序列化是`不能序列化static变量`的，因为其保存的是对象的状态，而static变量保存在全局数据区，在对象未实例化时就已经生成，属于类的状态(`可以通过序列化类对应的class对象`)