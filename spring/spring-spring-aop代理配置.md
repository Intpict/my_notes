## spring
### spring-aop代理配置
通过配置织入@Aspectj切面，虽然可以通过编程的方式织入切面，但是一般情况下，我们还是使用spring的配置自动完成创建代理织入切面的工作。

通过aop命名空间的<aop:aspectj-autoproxy />声明自动为spring容器中那些配置@aspectJ切面的bean创建代理，织入切面。当然，spring在内部依旧采用AnnotationAwareAspectJAutoProxyCreator进行自动代理的创建工作，但具体实现的细节已经被<aop:aspectj-autoproxy />隐藏起来了

<aop:aspectj-autoproxy />有一个proxy-target-class属性，默认为false，表示使用jdk动态代理织入增强，当配为<aop:aspectj-autoproxy  poxy-target-class="true"/>时，表示使用CGLib动态代理技术织入增强。不过即使proxy-target-class设置为false，如果目标类没有声明接口，则spring将自动使用CGLib动态代理。

使用@Order注解可以指定aop执行的优先权，数值越小优先级越高：

* 在切入点前的操作，按order的值由小到大执行
* 在切入点后的操作，按order的值由大到小执行

