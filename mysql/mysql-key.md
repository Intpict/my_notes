## MySql
### key
应该说是 key 属性
1. 如果Key是空的, 那么该列值的可以重复, 表示该列没有索引, 或者是一个非唯一的复合索引的非前导列
2. 如果Key是PRI, 那么该列是主键的组成部分
3. 如果Key是UNI, 那么该列是一个唯一值索引的第一列(前导列),并别不能含有空值(NULL)
4. 如果Key是MUL, 那么该列的值可以重复, 该列是一个非唯一索引的前导列(第一列)或者是一个唯一性索引的组成部分但是可以含有空值NULL
如果对于一个列的定义，同时满足上述4种情况的多种，比如一个列既是PRI,又是UNI
那么"desc 表名"的时候，显示的Key值按照优先级来显示 PRI->UNI->MUL
那么此时，显示PRI
一个唯一性索引列可以显示为PRI,并且该列不能含有空值，同时该表没有主键
一个唯一性索引列可以显示为MUL, 如果多列构成了一个唯一性复合索引
因为虽然索引的多列组合是唯一的，比如ID+NAME是唯一的，但是每一个单独的列依然可以有重复的值
只要ID+NAME是唯一的即可
