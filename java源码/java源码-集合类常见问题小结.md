## java源码
### 集合类常见问题小结
1. HashMap和HashTable  
      相同点：二者都实现了Map接口，因此具有一系列Map接口提供的方法。  
      不同点：  
    * HashMap继承了AbstractMap，而HashTable继承了Dictionary。
    * HashMap非线程安全，HashTable线程安全，到处都是synchronized关键字。
    * 因为HashMap没有同步，所以处理起来效率较高。
    * HashMap键、值都允许为null，HashTable键、值都不允许有null。
    * HashTable使用Enumeration，HashMap使用Iterator。
     >  这些就是一些比较突出的不同点，实际上他们在实现的过程中会有很多的不同，如初始化的大小、计算hash值的方式等等。毕竟这两个类包含了很多方法，有很重要的功能，所以其他不同点，请感兴趣的读者自己去看源码，去研究。笔者推荐使用HashMap，`因为它提供了比HashTable更多的方法`，以及较高的效率，如果大家需要在多线程环境中使用，那么用Collections类来做一下同步即可。

2. Set接口和List接口  
    相同点：都实现了Collection接口  
    不同点：Set接口不保证维护元素的顺序，而且元素不能重复。List接口维护元素的顺序，而且元素可以重复。  
3. TreeMap和HashMap  
     HashMap具有较高的速度(查询)，TreeMap则提供了按照键进行排序的功能。
4. HashSet和LinkedHashSet  
     HashSet，为快速查找而设计的Set。存入HashSet的对象必须实现hashCode()和equals()。
     LinkedHashSet，具有HashSet的查询速度，且内部使用链表维护元素的顺序(插入的次序)，于是在使用迭代器遍历Set时，结果会按元素插入的次序显示。
5. TreeSet和HashSet  
     TreeSet: 提供排序功能的Set，底层为树结构 。相比较HashSet其查询速度低，如果只是进行元素的查询，我们一般使用HashSet。
5. ArrayList和Vector  
      同步性:Vector是线程安全的，也就是说是同步的，而ArrayList是线程序不安全的，不是同步的。
      数据增长:当需要增长时,Vector默认增长为原来一培，而ArrayList却是原来的一半
6. ArrayList和LinkList  
     相同点：都实现了Collection接口  
     不同点：ArrayList基于数组，具有较高的查询速度，而LinkedList基于双向循环列表，具有较快的添加或者删除的速度，二者的区别，其实就是数组和列表的区别。上文有详细的分析。
7. Collection和Collections  
      Collection是一系列单值集合类的父接口，提供了基本的一些方法，而Collections则是一系列算法的集合。里面的属性和方法基本都是static的，也就是说我们不需要实例化，直接可以使用类名来调用。
