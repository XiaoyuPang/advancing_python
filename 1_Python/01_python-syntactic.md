
# random：
	random.sample(list,n)	#从指定列表(含n个元素)生成n个不重复的元素
	random.random()		#生成0-1之间的浮点数
	random.randint(a,b)	#生成a-b之间的整数

# range：
	range(start，end，step)	#比如range(0,30,3)，生成0,3,6,9
	
# collections
	Counter(iterable)	#用于统计词频，有方法most_common查看词频排序。

# format：
	"{0:032b}.format(10) 	#将10转换程32bit的二进制，其中32前面的0表示不换行，若换成1则换一行。
	
# floor地板除：
	在python3中，a/b是浮点除，a//b是整除，也叫地板除，地板除是向下取整的，与c/c++/java的向0取整不同。
	如：10/3=3.33 10//3=3  , -10/3=-3.33  -10//3=-4  了解了地板除，就可以理解python的取模。
	
	取模：
		b(被除数)//c(除数) =s(商)...y(余数/模)    -->   y=b-c*s
		如：-10%3 =-4....2   10%-3=-4....-2
		
		  

# 文件操作：

	f = open(文件名，'读\写')
	f.read(number)	#number的单位为字节，默认不写全部读取
	f.readlines() # 按照行的方式把文件内容进行一次性读取，并返回一个列表，每一行的数据为一个元素。
	f.tell()	#获取当前读写位置
	f.seek()	#定位到某个位置
	
	os.rename(old_file,new_file)	#文件重命名
	os.remove(file_name)		#删除文件
	os.mkdir()		#创建文件夹
	os.getcwd()		#获取当前目录
	os.chdir("路径")		#改变当前路径
	os.listdir(”路径")	#获取当前目录列表
	os.walk("路径")		#获取当前路径的目录和目录下的文件，返回三个参数：root，dirs，files，是generator对象，用for遍历出来。
	os.rmdir("文件夹名")	#删除文件夹名	
	
	os.path.splitext(filename)		#切分文件名为两部分：名字[0]，后缀名[1]
	os.path.join(路径,filename)		#获取文件的路径

# 可迭代对象：
	可变和不可变：
		比如list和tuple的可变和不可变，都是针对引用（id）而不是值（value），比如a=(1,[1,2,3])，a[1]是可变的，a[1].append(4)不会报错
	str对象：
		切片：xxx[::-1]表示把字符串反转
		方法：	
			find、index、count、replace、split、capitalize、title、startswith、endswith、
			lower、upper、ljust、isdigit、isalnum、rjust、center、lstrip、rstrip、strip、
			rfind、rindex、partition、rpartition、splitlines、isalpha、isspace、join					
	list对象：
		方法：
			append、insert、extend、index、count、del、remove、pop、sort、reverse
		
	tuple对象：
		方法：
			count、index
	dict字典：
		方法:
			del、clear、len、keys、values、items
		内置函数enumerate(): 将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标。
		
	set集合：
		union联合、intersection交、difference差
	
# 函数：
	缺省参数：	def(x,y=20) 不能把y=20放到x前面
	不定长参数：	*args,**kargs
	拆包（元组、字典）：	
		在函数调用参数传递时，若有函数test(*args,**kargs),变量A=(1,2),K={"age":1},可这样传递test(*A,**K)
		如果有B=[1,2]，test(*B,**K)，实际上B会被转换成了tuple，因此拆包实际上只有元组和字典，没有列表。
		
	+=和=+：	sum+=sum 和sum=sum+sum的结果不同（可变类型)，__iadd__修改自身，__add__产生新的对象
	递归	：	一定是返回自身，并且设置有退出条件
	
	匿名函数lambda:
		按value对dict排序：
			a={"lisp":100,"python":200,"java":80}
			sorted(a.items(),key=lambda x:x[1],reverse=True)	#默认是从大到小排序，reverse设置为True则按小到大排序。
		给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
			所有的小写字母在大写字母前面
			所有的字母在数字前面
			所有的奇数在偶数前面
			
			s = "Sorting1234"
			"".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x)))
			
	
# 面向对象：
	(三个要素：封装(全局变量和函数）、继承（子-->父）、多态（定义的时候不确定调用什么功能，真正调用的时才确定调用的是子类还是父类的功能)
	一切对象都有三个属性：	type、id、value	
	==和is：		== 判断两个对象的type和value是否相同，is判断id是否相同
	self:		self保存当前对象的引用。对象的引用由__new__创建实例对象时返回。
	cls：		cls保存类的引用，类的引用由type()创建类时返回，type能创建类，是用了元类（__metaclass__)。
	__init__：	初始化对象就会被执行，目的是给对象设置属性即--给对象传参时要用init，否者只能以：实例.属性=xxx 这种方式动态新建属性。
	__new__:	用来创建对象。类()这个实例化对象过程实际是调用new方法，new接受类引用，返回对象引用。
	__str__：	获取执行的h对象的描述信息，如test = Test(1,2)  print(test) 实际上是打印__str__的返回值。
	__del__		当在类里面定义了__del__方法，在外部使用del 删除对象时，就会调用__del__方法。
	__call__:	使类执行像函数执行一样，定义了__call__方法的类，类()就会调用内部的__call__方法。
	__getattribute__:	属性拦截器
	__mro__:	类.__mro__ 查看继承树，只能用类来查，实例对象没有该属性。
	property（两种用法）：
			（一般我们都会使用私有变量以防安全，然后设置setter和getter方法用来向外提供间接访问私有变量）
			在调用对象方法的时候，是对象.方法()，我们使用property修改调用的方法名如 num=property(方法),调用就变成:对象.num
			property的装饰器用法：在xxx()方法使用@property设置表明是getter，在xxx()方法使用@xxx.setter表明是setter
	
	私有属性和私有方法(__xx)：	不能通过对象直接访问，也无法被子类继承。往往用来做内部事情，起到安全作用。
	
	私有化：
			__xx__一般由python内部保留做魔法方法。
			__xx私有外界无法访问和继承，原因名字被改成:_类名__xx,可使用dir查看对象的方法和属性。
			xx_避免与python关键字冲突。
			_xx 不能 from xxx import *导入。(实际上所有以下划线开头的全局变量都无法用 from xxx import * 导入）
	
	类属性和实例属性：	实例属性在实例之间都是独享的，类属性在实例之间是共享的。要想修改类属性，可调用类修改，或对象使用类方法修改。
					每一个实例都有一个独立的内存，即实例的id都是不同的。而函数则相同。
					
	类属性的继承：
			子类继承父类的类属性，只要子类改变了属性，就以子类的属性为准。
	
	多态(鸭子类型)：def func(obj): return obj.run()   具有run方法的类都可以被func调用，即便在run的实现上不同。
				  定义时不确定，运行时才确定，这就是多态。
				  
	子类初始化父类构造方法(__init__)：
			python中子类继承父类，相同的方法子类会覆盖父类，比如__init__，这个时候即使调用子类中没有的父类方法，
			如果涉及到父类__init__	初始化的属性，也会无法调用，因为子类中没有继承父类的属性，这个时候我们要在子类中初始化父类的构造方法，
			有两种方式：1.使用super  2.超类方法的未绑定版本，父类.__init__(self) 。
	
	
	super()：用于调用父类方法，子类和父类的方法相同，子类方法会覆盖父类方法。super().方法() 不需要self。
			class Cat(A,B):
				def hello(self):
					super(A,self).__init__()
					print(self.name)	
					
			#此时程序会调用B的init而不是A的，super() = super(Cat,self)
	
	类方法@classmethod： 
			有实例方法和实例属性，就有类属性和类方法，我们使用类方法是为了修改类属性。定义一个类方法，
			在该方法上使用@classmethod，并且把self改成cls。类方法的调用和实例方法调用一样。类方法里调用类属性：cls.xxx
	
	静态方法@staticmethod：
			一般在开发的时候，一个.py文件有么全是函数要么全是是类，既有函数又有类会显得不伦不类。我们可以把函数写到类里面，
			再使用@staticmethod装饰，这样，函数既可以写到类里面，又不是类方法，变成单纯的与类无关的普通函数。
			调用静态方法装饰的函数，和调用实例方法、类方法一样：		实例=类();实例.静态函数()
			
	
	
	工厂模式： 在基类(父类)定义接口(方法)而不实现，由继承的子类来实现接口(方法),就是工厂模式。
			  为什么使用工厂模式： 有些方法是子类特有的，必须由子类来实现。
	
	单例模式：
		一个类可以产生多个不同的实例。确保某一个类只有一个实例，这个类叫单例类，单例模式是一种对象创建模式。
		由于创建对象用的是__new__方法，若子类没定义new则自动继承object.__new__(cls),每次创建对象都会自动调用，并产生不同id的对象。
		因此我们需要在子类重写new，满足单例条件则调用父类new来创建对象，不满足则不调用。
		
		方法1使用new：
			class Singleton:
				__instance = None		#用来判断是否创建过对象，若为None则没创建过，此时调用objenct的new来创建新对象
				def __new__(cls):		#注意，new必须有一个变量接受class传来的类的引用，一般用cls
					if cls.__instance == None:
						cls.__instance = object.__new__(cls)	#调用父类的new创建对象，new返回创建的对象的引用保存到__instance
						return cls.__instance					#返回__instance很重要，__init__等等实例方法都要接收对象引用。
					else:
						return cls.__instance	#不创建对象，返回先前创建的对象的引用	
	
		
	元类	：	使用class创建类，实际是调用type创建，type即可以返回对象类型，也可以动态创建类，type创建类是使用了__metaclass__（翻译成元类）
			要控制类的创建行为，可以使用metaclass。metaclass允许你创建类或者修改类，可以把类看成是metaclass创建出来的“实例"。
			什么时候用到元类呢？ 需要创建类的时候。比如ORM，
			思路：
				我们创建对象时，先定义类，再用类创建对象。同理，创建类时，先定义metaclass，再创建类。
			先略过。。。	
			
			
	
	__slots__和python的动态性理解：
	
			动态性：python能在运行的时候添加方法和属性，这叫动态性，假如我们有个对象Test，我们可以这样创建属性Test.name="test"
			
			__slots__:用于限制定义对象的属性：
					class Test：
						__slots__ = ("name","age")
						def __init__(self)
							self.name = "test"
							self.age = "18"
							self.hello = "hello" 	#对象运行时会报错，没有该属性		
# 其他：	
	迭代器：
		可迭代对象(iterable)：可作用于for循环的数据类型,本质上本质上实现了__iter__()方法：如str、list、dict、set、tuple
		迭代器(iterator): 
				实现了__iter__() + __next__()的对象，python里没有现成的迭代器，但可以通过iter(iterable)方法构建出来
				比如： x = "this is a quote"  y = iter(x)  next(y)  
				另外一种方式是使用列表推导式时把[]改成(),如： y = (x for x in range(10))
		
	生成器:	
		generator是一种特殊的迭代器，因为它不用构建__iter__和__next__,而是直接使用关键字yield。所有使用了yield的函数都是生成器。
		yield与return的区别：yield返回生成器，实际上，凡是return iterable的都可以用yield代替
	
	
	闭包:	外部函数里面再定义一个内部函数，外部函数return内部函数，外部函数执行后的输出作为内部函数的输入。
			闭包是函数式编程的一个重要语法结构，装饰器就是闭包的应用。
	
	装饰器：	
		装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
		装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
		概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
	
			装饰器是闭包的应用，比如，我们想在不修改函数的前提下，验证有执行权限后才让你调用函数。
				def out_bag(func):
					print("---装饰器开始执行---"）
					def wrapped():
						if xxx:
							func()
						else:
							print("没有权限")
					return wrapped
					
				#调用方法：func = out_bag(func) = wrapped
				#等价于：  @out_bag
				#		  def func():
				#装饰后调用：func() 等价于 wrapper()
				
			装饰器的执行时间：
				@out_bag	#程序执到这一步的时候会打印“--装饰器开始执行--”，装饰器在装饰的时候就开始执行了，并不是程序调用才开始装饰。	
				def func():
					pass
								
			两个装饰器：(原理是一样的，会两个就会3个，以此类推）
				@makebold
				@makeitalic
				def return_hello():
				#等价：return_hello = makebold(makeitalic(return_hello))
				
			获得装饰器的返回值：
				若想获得func()运行后的返回值(前提func有return),则需要在wrapped()内添一个变量保存func返回值，并且在wrapped内return。
				
			带有参数的装饰器：在外层再定义一个函数
				def big_brother(args):
					print("big_brother")
					def bother(func):
						print("brother")
						def wrapped(*args,**kargs):
							print("wrapped")
							if args:
								s = func(*args,**kargs)
								return s
							else:
								xxx						
						return wrapped		
					return brother
					
				#等价于：
				@big_brother("haha")		#解释器执行到这，会打印big_brother和brother
				def func(*args,**kargs):
				# 虽然多了一层函数，但调用func时，依旧是func = wraaped
				
		类当装饰器：（用到call）
			class Test:
				def __init__(self,func):
					self.__func =func
				def __call__(self):
					self.__func()
			#开始装饰：
				@Test
				def func():
					pass
			
			#装饰后调用：func = Test(func)  ,func() = Test(func).__call__()	
			
		
	
	作用域LEGB：
		local-->enclosing function(内嵌函数，闭包常见）-->global -->building
		在Python的函数里若变量名与全局变量名相同，则会隐藏全局变量名。若想在函数里修改全局变量名，在函数里用关键字：global。
		
	深拷贝和浅拷贝(copy模块)：
		深拷贝（copy.deepcopy):
			对被拷贝对象的完全复制（若是不可变类型则引用而不拷贝），另起一个内存空间。
		浅拷贝(copy.copy):
			浅拷贝对内层嵌套都是引用，只copy第一层，并且针对不可变和不可变类型有不同的操作。
			a=[1];b=[2];c=[a,b];d=copy.copy(c),此时的id(c)和id(d)是不同的。-->对可变类型则新建
			a=[1];b=[2];c=(a,b);d=copy.copy(c)，此时的id(c)和id(d)是同的。-->对不可变类型则引用
			
	
	异常： 把不确定会出错的代码放到try： except 中,手动抛出异常：  raise Exception：
	
	垃圾回收：（引用计数为主，分代回收为辅）
		小整数对象池：Python里一切是对象，对象的实例化为赋值的过程，赋值实际上是引用，引用对象又分为可变和不可变对象。
					int是不可变对象，但Python里[-5,257)这些整数对象是用之前已经提前创建好的。常驻内存。
					目的：为了避免整数的频繁销毁和申请内存空间。
		大整数对象池：每个大整数都会创建一个新对象
		
		intern机制： 类似一个共享机制，字符串是不可变类型，在Python里字符串中若无空格（即单字符串），即便有多份也只是引用，若字符串中含有空格，
					则新建一份，像这种只用一份的的机制叫intern机制
	
	
		引用计数，是Python解决垃圾回收的一个主要机制，当引用为零则Python解释器自动回收内存。
			优点：简单
			缺点：解决不了循环引用
		
		分代回收（generation gc）：python使用三种链表来追踪活跃的对象，当引用计数达到某种程度时触发引用计数减一。
			0代链表（generation zero）：所有新创建的对象都会添加到0代链表，一般引用计数为1。
			1代链表： Python判断0代链表有循环引用的对象的计数减1，计数不为0且没有循环引用的活跃对象被移到一个新的链表：1代链表，
					 引用计数为0的对象被回收，因此处理了引用计数为1的循环引用，多引用计数的循环引用被 减一后继续留在0代。
			2代链表：1代链表引用计数减1，计数不为0的活跃对象被移到2代链表。
		
			垃圾回收模块gc：gc.get_count(),gc.get_threshold(),gc.disable(),
			3中情况触发垃圾回收：1.调用gc.collect(),2.gc模块计数值达到阀值 ，3.程序退出
	
	内建属性：如__class__,__doc__,__repr__,__dict__,__bases__,__new__,__del__,__str__,__getattribute__,__init__
	
	内建函数：range、map、filter、reduce、sorted
	
	functools：partial偏函数、wraps函数、
		wraps：
			我们知道，被装饰器装饰后的原函数不再指向原函数本身，而是指向wrapped。当我们help(原函数)的时候查看到的却是wrapped，与
			我们想要的结果违背了，因此在wrapped之上使用@wraps(原函数),就可以像原本一样访问原函数。
			from functools import wraps
			def out(func):
				@wraps(func)
				def wrapped(*args,**kargs):
					""""wrapped""""
					func()
				return wrapped
			
			@out
			def func():
				"""func"""
				pass
				
			#此时调用func运行忍仍然是调用wrapped，但help(func)的时候返回的就是“”“func"""而不是”“”wrapped“”，
			#func.__name__返回的也是func而不再是wrapped，这就是wraps的好处。
			
	
	__all__：	如果一个模块中有__all__变量， 这个变量以外的元素不会被 from xxx import * 时导入，如 __all__ = ["Test","test1"]
	
	Python自省:
		自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型。type(),dir(),getattr(),hasattr(),isinstance().
	
	给程序传参：
		import sys 	
		sys.argv
	 
	type和object：
	 	所有对象都有两个基本属性：类型（class) 、子父（base)
	 	查看一个类的类型可用type或__class__属性，查看一个类的父类用__bases__属性。
	 	type.__bases__		#返回 object
	 	object.__bases__	#返回 （）
	 						#说明 object是“父子关系”的顶端，object是type的父类。
	 	type.__class__		#返回 type
	 	object.__class__	#返回 type
	 						#说明 type是“类型关系”的顶端，type是object的父类。
	 						
	 	#看下面两个实例
	 	list.__bases__		#返回（object,)
	 	list.__class__		#返回 type
	 	
	 	#mylist = [1,2]
	 	mylist.__class__	#返回 list
	 	mylist.__bases__	# 报错，list' object has no attribute '__bases__ ，实例化的list的类型是<type 'list'>, 而没有了父类
	 	
	 	总结：对象的类型有很多，比如int，list，object，type，其中type是类型中的顶端，一切类型都是type的子类，因此我们可以继承type来
	 		自定义自己的元类。
	 		
	 		对象不是凭空产生，无论什么对象，最终都是object的子类。
	 		
	 		type和object是相互存在的，我们定义一个类，若不继承任何类，则默认同时继承type（__class__)和object(__bases__)。
	 
	 协程和yield：		
	 		
	 	
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
