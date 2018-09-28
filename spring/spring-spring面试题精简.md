1. Spring Bean的生命周期简单易懂。在一个bean实例被初始化时，需要执行一系列的初始化操作以达到可用的状态。同样的，当一个bean不在被调用时需要进行相关的析构操作，并从bean容器中移除。
2. Spring bean factory 负责管理在spring容器中被创建的bean的生命周期。Bean的生命周期由两组回调（call back）方法组成。
3. Spring中构造器注入和属性注入的差别: ？
4. Spring静态属性能否注入: 可以，但是不能直接在属性上用@Autowired注解，`因为spring是基于对象层面上的依赖注入`。需要在静态属性的set方法上加@Autowired注解，该方法不是静态的。
5. Spring基础属性能否注入：可以，xml使用<property name="username" value="lisi"/>这种形式注入，注解使用@value注入，一般迎来properties对象。