# 并行和并发：
	并行就是多个任务被多个cpu同时执行。并发是一个CPU在多个任务中快速切换。

# 同步和异步：
	同步：就是协同步调，普通单线程/单进程就是同步的--程序只有执行了上面的语句才能执行下面的语句。
	异步：就是可以来回切换。CPU就是通过异步实现在多个进程/线程间切换的。
	
# multiprocessing：
```python {.line-numbers}
Process类：
	p = Process(tartget=函数名，args(参数，))
	p.start()	#子进程开始执行
	p.join()	#p.join()之后的代码会等待p.start()执行完后才执行。join相当于堵塞，用于控制子主进程执行的先后顺序。
	
Pool类：
	p = Pool(最大进程数）

	p.map(func,list)
	for i in range(任务数): 
		p.apply_async(函数名，(参数))	#p.apply_async异步的(同时进行)，p.apply是同步的(一个子进程执行完才到下一个)				
	p.close()	#进程开始	
	p.join()	#主进程完成后就退出，不等待子进程，这是Pool和Process的不同之处，使用Pool一定要加join来控制子主进程执行顺序。
	
进程间通信：
	进程都是独立的，子进程对全局变量的修改不会影响到其他进程，那么如何通信呢？使用multiprocess中的Queue(Process)和Manager(Pool)。
	Queue和Manager相当于一条进程间的管道。
		
	from multiprocessing import Process,Queue,Pool,Manager
	
	def put_data():
		for data in range(10):
			q.put(data)
			print("put_data:{0}".format(data))
	def get_data():
		try:
			data = q.get_nowait()		#在队列Queue为空的情况下get是会等待的，get_nowait则不会，但触发异常。
			print("get_data:{0}".format(data))
		except:
			pass
	#Process类：
	q=Queue()
	put = Process(target=put_data)
	get = Process(target=get_data)		
	put.start()
	get.start()			
	put.join()
	get.join()

	#Pool类：
	q=Manager().Queue()
	p=Pool
	p.apply_async(put_data)
	p.apply_async(get_data)
	p.close()
	p.join()
	

多进程的同步和异步：
	Process类和Pool类都可以通过控制join来达到多个进程是同步还是异步，不同的是，在Pool使用for创建多个线程时，还可以选择async来控制。
```		

# threading：
```python {.line-numbers}
多线程里，主线程执行完了会等待子线程执行完才退出（类似多进程的Process)。一个线程死掉，整个进程就崩。
线程共享全局变量，全局变量用得不好容易导致出错，即线程不安全。
即使多个线程执行的是同一个函数，各个线程的变量都是独有的，即每个线程的函数都有独立的空间，除了全局变量是共享的。

Thread：
	from threading import Thread
	def test(name):
		for i in range(10):
			print("{0}={1}:is runing".format(name,i)
	t1=Thread(target=test,args=("A",))
	t2=Thread(target=test,args=("B"))
	t1.start()
	t2.start()
	
线程间通信：
	对于非共享变量，在函数内部定义就好。线程想用线程的数据，可以使用全局变量，但会导致线程不安全。
	threading有一个local类，解决线程间通信，又不会引发访问全局变量导致出现安全问题。
	
多线程的同步和异步：
	同步：
		全局变量访问同步：
			线程调度的不确定性和线程的全局变量共享，导致线程不安全问题，因此有必要对全局变量的访问实现同步(阻塞)。
			方法有：轮询和互斥锁，threading模块中定义了Lock类，可以方便处理。
		线程执行同步：控制join		
			
	异步：控制join

死锁：
	概念：线程间共享个多资源时，线程之间分别占用一部份资源并且等待对方的资源，就会造成死锁。
	避免死锁：
	1.添加超时时间：mutex.acquire()的timeout添加时间
	2.程序设计避免：如银行家算法（评估安全了才选择分配对象）
	
生产者和消费者模式：
	处理速度不匹配的解决办法是在中间添加缓冲区(或管道）如利用：队列(Queue)达到阻塞。
	生产者和消费者模式的本质就是用了进程间通信或其他通信，解决了进程间的数据沟通。
	multiprocessing模块有个Queue()用于进程间通信，queue模块有个Queue()用于线程间通信。只要是生产和消费者问题，都可以用队列解决。
		
GIL全局解释器锁：
	由于历史原因，Python的多线程是假的，只能使用一个核，原因是GIL。
	如果想在python里实现多任务的并发，可以使用多进程，Python的多进程无锁，因此效率比多线程高。

	解决GIL：用c语言来解决
		c语言的库：想出售软件但不想暴露源码，就可以把源码编译成二进制文件。
			静态库：所有的文件都已直接编译好。
			动态库：有可能很多东西依赖当前的系统。
		
		首先把一个C语言文件（如：test.c)编译成一个动态库，命令：gcc test.c -shared -o libtest.so ,生成libtest.so文件
		在python文件里加载动态库，需要用到ctypes标准库：
			from threading import Thread
			from ctypes import *
			lib = cdll.LoadLibrary("./libtest.so") # 加载本地的c动态库，cdll为ctypes里的功能。
			t.Thread(target=lib.DeadLoop) # 假设DeadLoop为libtest.so里的一个c函数，功能为死循环,由子线程执行
			t.start()
			# 主线程执行另一个死循环，这样，整个进程一共有两个线程执行两个死循环，cpu的两个核会被占满，从而实现并发。
			while True:
				pass
```					
# 协程：
```python {.line-numbers}
假如一个.py文件有A、B两个函数，正常情况下程序从上而下顺序执行A再到B，B必须等待A执行完才能执行，我们说此时的进程是同步的(阻塞的)。
如果想实现异步，即AB相互不必等待，我们可以使用：
	1.多进程，一个进程A，另一个进程B。假如cpu是多核的，还可以并行。
	2.多线程，一个线程A，一个线程B。python的多线程无法并行，因此python的多线程在计算密集型的情况下不比多进程效率高。
	3.协程，类似中断，可以在A执行过程中中断去执行B。
		通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，
		注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定。
	
	
协程vs多线程：
	因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
	第二大优势就是不需要多线程的锁机制，
	因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
	因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
	Python对协程的支持是通过generator实现的。
	传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
	如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高

协程的实现：
	用yield，但生成器本身不是完整的协程，有优秀的第三方包：greenlet，gevent(对greenlet的封装，更加强大)
	
	gevent:
		在遇到耗时操作，会把主动权交出去。yield版协程遇到yield就会切换。
		
协程(gevent)的用途:
	协程主要应用在io密集型(网络)，因为io密集型操作主要是耗时，而gevent可以主动识别哪些操作是耗时的(比如gevent.sleep)
	，从而把主动权切换到其他不耗时的操作。
	
	Tornado框架就是用gevent实现的异步web框架。
	
	可以使用gevent实现并发tcp服务器，gevent里有个socket、monkey类
```

















	
					
		
