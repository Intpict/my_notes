* resultMap & resultType  
    * resultMap表示将查询结果集中的列一一映射到bean对象的各个属性。映射的查询结果集中的列标签可以根据需要灵活变化，并且，在映射关系中，还可以通过typeHandler设置实现查询结果值的类型转换，比如布尔型与0/1的类型转换。
    * resultType 表示的是bean中的对象类，此时可以省略掉resultMap标签的映射，但是必须保证查询结果集中的属性 和 bean对象类中的属性是一一对应的，此时大小写不敏感，但是有限制。
* ParameterMap(不推荐) & parameterType
    * ParameterMap和resultMap类似，表示将查询结果集中列值的类型一一映射到java对象属性的类型上，在开发过程中不推荐这种方式。
    * 一般使用parameterType直接将查询结果列值类型自动对应到java对象属性类型上，不再配置映射关系一一对应，例如上述代码中下划线部分表示将查询结果类型自动对应到hdu.terence.bean.Message的Bean对象属性类型。