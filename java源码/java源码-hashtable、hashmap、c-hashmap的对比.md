## java源码
### hashtable、hashmap、c-hashmap的对比
1. 一般对象放入hashMap时，一定要实现他的hashCode方法和equals方法，否则按照地址来进行hash  
2. jdk1.7 hashmap在链表头部插入，jdk1.8 hashmap在链表尾部插入