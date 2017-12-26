## java源码
### list中equals和hashCode实现
1. **equals**  
典型的equals的编写代码的方式：
```
   public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof List))
            return false;

        ListIterator<E> e1 = listIterator();
        ListIterator<?> e2 = ((List<?>) o).listIterator();
        while (e1.hasNext() && e2.hasNext()) {
            E o1 = e1.next();
            Object o2 = e2.next();
            if (!(o1==null ? o2==null : o1.equals(o2)))
                return false;
        }
        return !(e1.hasNext() || e2.hasNext());
    }
```   
1. 判定o和当前对象引用的是不是同一个对象，如果是的直接返回true  
2. 判断o是不是List对象(instanceof)，如果不是List的实例，那就直接返回。此外如果没有这句话的话这样会导致直接生成迭代器的时候会产生错误。  
3. 生成两个迭代器。分别对量迭代器进行分别比较各个迭代器的元素。  
4. 当迭代器中某一个迭代器结束之后，结束循环体，并且还需要保证两个迭代器都同时结束才返回true。  

   **[注意点]**  
* 需要注意的一点应该就是泛型的使用了。另外在比较的时候使用E的equals方法。而不能使用Object。
* 当对象o为null时，o instanceof List 必定返回false。

 2. **hashCode**
```
    public int hashCode() {
        int hashCode = 1;
        for (E e : this)
            hashCode = 31*hashCode + (e==null ? 0 : e.hashCode());
        return hashCode;
    }
```
* 采用31作为系数: 首先当然需要采用质数，最好是一个比较大的质数。因为这样当需要散列的关键字数量太大的时候更不容易出现冲突的情况。而采用31是考虑到这样做是相当于把原来的数左移5位，然后减一，这样计算效果要快的多。据说大部分的jvm都对此进行过优化。因此使用31为系数的hash算法在java里非常常见。 
* 取质数是为了避免在同一个散列中的元素有相同的联系和性质

3. **sort**
说明：default void sort(Comparator<? super E> c)
jdk1.8中List接口中定义了该sort方法，并给出了default实现，但是实际的实现还是使用的Arrays.sort()方法。
