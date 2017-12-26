## java源码
### LinkedList
LinkedList<E>   
**extends** AbstractSequentialList<E>  
**implements** List<E>, Deque<E>, Cloneable, java.io.Serializable  
1. **Node**  
```
private static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }
```
LinkedList中与Node类配合的方法是Node<E> node(int index)方法，已assert输入的index有效，通过`从头迭代还是从尾迭代通过if (index < (size >> 1))判断`当前传入的index更接近头还是更接近尾。  

2. **节点操作**  
LinkedList有3个变量： 
* 一个是int类的size: 表示当前size的大小 
* 一个是Node类型的first: 表示当前列表中的第一个节点 
* 一个是Node类型的last: 表示当前列表中的最后一个节点

3. **迭代器**  
* 双向迭代器ListItr: listIterator()获取  
>包含四个私有变量的引用： 
> * lastReturned：用来保存刚刚跳过的节点 
> * next：指向下一个应该跳过的节点，被初始化为当前指向的节点，如果index为size则有可能为null。 
> * nextIndex：指向下一个节点的标号，被初始化为传入的index。 
> * expectedModCount：该节点所记录的结构性变化的次数，初始化时被赋予LinkedList的modCount。

* 反向迭代器DescendingIterator: descendingIterator()获取  
>实现方式:   
> ```
>    private class DescendingIterator implements Iterator<E> {
>        private final ListItr itr = new ListItr(size());
>        public boolean hasNext() {
>            return itr.hasPrevious();
>        }
>        public E next() {
>            return itr.previous();
>        }
>        public void remove() {
>            itr.remove();
>        }
>    }
> ```
4. **clone**  
理解clone的特性:  
* 对象类必须支持`Cloneable接口，才能调用super.clone()`，否则即使派生类覆盖了Object#clone()方法，也同样会抛出CloneNotSupportedException这个异常。
* x.clone()!=x的意思是x.clone()返回的对象为新建的对象，与原来的对象地址不同。 
*  x.clone().getClass() == x.getClass()的意思是克隆出的对象与原对象都是同一个类生成的。 
*  x.clone().equals(x)的意思是新的对象与原来的对象相同（在equals()函数下是相同的,所以通常需要覆盖equals()方法，但是在下面的例子里，这句话的返回是false）
*  protected native Object clone() throws CloneNotSupportedException;这里clone()方法修饰符是protected，而不是public。这种访问的不可见性使得我们对Object#clone()方法不可见，同时，我们还需要实现各自类独有的clone操作。所以，`要覆盖Object#clone()方法`。  

**总结：**: clone方法至少保证`第一层的复制是深复制`过程。