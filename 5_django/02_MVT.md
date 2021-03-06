# 模型M：
    django连接mysql：
        1.mysql-python不支持django2.0，使用mysqlclient代替：
        	$sudo apt install  libmysqlclient-dev
        	$pip3 install mysqlclient
        	       	
        2.settings.py中更改数据库：
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'my_django',
                    'USER':'root',
                    'PASSWORD':'root',
                    'HOST':'localhost',
                    'PORT':'3306',
                }
            }
        3.NAME这个key对应的是数据库名，django的数据迁移只生成表，需要我们提前在mysql中创建数据库。            
        
    字段：models提供的字段
    	如charField,BooleanField
    
    元选项：
    	meta，用于设置元信息,在models类下定义。比如表默认在数据库中的名字为"应用名_表名“，我们可以更：
    		class Meta:
    			db_table = '表名'
    管理器：
    	django提供的models的objects对象就是Manager()类型的对象，管理器Manager是django的模型进行数据库的查询操作的接口 。我们可以
    	自定义管理器，1是可以更改默认查询集  	，2是为管理器额外增加方法（ 比如modles类默认都不能使用__init__方法，因为Manager内部使用了）。
    	所谓ORM，在django中就是modls的管理器。对数据库的查询，就是对管理器的属性访问。 
        
	查询：
		models.objects.查询
		返回查询集：
			all()
			filter()
			exclude()
			order_by()
			values()
		返回单个：
			get()
			count()
			first()
			last()
			exists()		
		字段查询，作为方法filter()、exclude()、get()的参数
		
		
		聚合：

# 视图V：
	一个http请求经过django处理，拿到地址，首先到settings的ROOT_URLCONF，映射到urls.py文件，经过正则匹配，
	然后由定义的路由函数返回响应。如果正则匹配包含一个()括号，即接受来自请求的一个参数，则路由函数有两个参数，
	一个是request，另一个是接收参数。
		
	urls配置，其中的name参数是配置url名字，为了反向解析，在视图重定向的时候用到。
	
	视图函数：
		第一个参数一定是request，不能少。
	错误视图404：
		在templates目录下创建一个404.html，一旦发生404错误就会被调用（前提是settings的debug为false以及模板地址已指定）
		
	request对象:
		django对用户请求的处理，是使用django自带的django.http.QueryDict对象。比如从用户传来的参数，就用到request对象的
		get，get_list等等方法。
			request.GET[]
		
		post请求：csrf跨域请求
			request.POST[]
			
	respons对象：
		cookie，由HttpResponse对象构建。获取，则由request.COOKIES对象 。cookie用于识别用户。
		重定向：HttpResponseRedirect()或redirect，接受的是一个urls而不是html文件。
		
		session：
			http是无状态的，无法记录用户与服务的交互，使用session目的是状态保持。sessoin是一个key-value，key就是cookie，
			保存在浏览器本地，value就是session值，保存在服务器。
			django的中间件已经添加了session支持。session就是一个字典对象。
			
			使用session：
				HttpRequest对象具有一个session属性，get()可以获取回话的值，clear()清除所有会话，
				flush清除当前会话并删除cookie。del request.session['member.id']:删除会话。
				django的  session默认会存在数据库。set_expiry(value)设置会话的超时时间
				
			存储session：
				我们可以指定session的存储路径，settings自定义配置，比如把session存储在redis需要安装redis数据库和下面这个包：
					$pip3 install django-redis-sessions
				
# 模板T：
	作为web框架，django提供了模板，也已便利的动态生成html。模板系统致力于表达外观，而不是程序逻辑。django的模板语言，包括：
		1.变量{{ }}
		2.标签{% %}，有for，if，comment ，include，url反向解析，csrf_token，布尔标签，block，extends，autoescape
		3.过滤器{{变量|过滤器}} ，lower，length等等
		4.注释{# 代码或html #}
		
		使用url反向解析的好处是，url不是写死的，有利于维护。
		
	模板继承：
		{% block  xxx %} 子模板的内容 {% endblock %}  ：block在父模板中定义，继承了父模板的子模板，将在block标签中填写内容。
		{% extend "父模板名" %}	:extend用于在字模板中继承父模板。
		
	html转义：
		html转义，就是将包含的html标签输出，而不被解释执行，原因是当显示用户提交字符串时，可能包含一些攻击性的代码，如js脚本。
		Django会将如下字符自动转义：
			< 会转换为&lt;

			> 会转换为&gt;

			' (单引号) 会转换为&#39;

			" (双引号)会转换为 &quot;

			& 会转换为 &amp;
		
		关闭转义：
			对于变量使用safe过滤器
			{{ data|safe }}
		
	csrf：
		全称Cross Site Request Forgery，跨站请求伪造某些恶意网站上包含链接、表单按钮或者JavaScript，
		它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，这就是跨站攻击。
		在django的模板中，提供了防止跨站攻击的方法：
		<form>
			{% csrf_token %}
			...
		</form>	
		
	验证码：
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

		
