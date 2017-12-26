## java基础
### Comparator和Comparable在排序中的应用
**1. Comparator**  
强行对某个对象collection进行整体排序的比较函数，可以将Comparator传递给Collections.sort或Arrays.sort。

**2.Comparable**  
强行对实现它的每个类的对象进行整体排序，实现此接口的对象列表（和数组）可以通过Collections.sort或Arrays.sort进行自动排序。

**[总结]**
* 一个类实现了Camparable接口则表明这个类的对象之间是可以相互比较的，这个类对象组成的集合就可以直接使用sort方法排序，但是只能实现一种排序标准(默认升序)。
* Comparator可以看成一种算法的实现，将算法和数据分离，Comparator也可以在下面两种环境下使用：
>1、类的设计师没有考虑到比较问题而没有实现Comparable，可以通过Comparator来实现排序而不必改变对象本身  
>2、可以使用多种排序标准，比如升序、降序。也就是说，可以`为不同的排序标准而实现不同的Comparator类`，这是`策略模式`的一种体现。
