## java源码
### Collections的用法
用法示例:  
```
List list = Collections.synchronizedList(new LinkedList(...));
```
* 多线程访问同时访问一个list，且只是有一个线程结构性的调整了list，这样的操作需要外部特性保持同步。这通常通过在list上自然封装一些同步对象实现。如果没有这样的对象存在，则需要Collections.synchronizedList(Set，Map)方法包装。
* 为了保证串行的访问，关键在于所有的对支持list的访问都需要通过返回的Synclist来实现。 `使用迭代器遍历它的时候，需要手动进行同步`。示例:

```
List list = Collections.synchronizedList(new ArrayList());
      ...
  synchronized (list) {
      Iterator i = list.iterator(); // Must be in synchronized block
      while (i.hasNext())
          foo(i.next());
  }
```