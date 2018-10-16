```python {.line-numbers}
网络层：
	应用层("send aa messege")->传输层(添加端口porn）->网络层（ip地址)->链路层(mac地址）

端口：(传输层）
	网络通信，实际上是进程和进程的通信。每个进程在本地操作系统有唯一的pid识别其他进程，但由于是动态的，不适合作为多台电脑网络通信的身份标志。
	端口的提出，是为了识别进程的网络通信，一个端口对应一个进程，端口值从0-65535，端口分配不是随意的，比如apachem默认是80端口，就像现实生活
	中报警电话是110，这种端口属于知名端口，范围0-1023。动态端口：1024-65535可以随意分配。netstat -an 查看端口情况。
	
socket：
	本地的进程通信（ipc）有多种方式：队列、同步（互斥锁、条件变量）
	网络通信：协议+端口 -->socket
	
	Python标准库socket：	（tcp和udp都是全双工的，所以socket是全双工的）	
		import socket
		#创建可收发数据的套接字对象，可选参数AF_INET表示用于Internet进程间通信，若填写AF_UNIX表示同一台机器上进程间通信
		s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp通信，比udp慢，但可靠
		s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #UDP通信，比tcp快，不可靠，用于多点通信：qq,语音/视频广播
					
		#发送数据
		s1.sendto(b"发送的数据",("192.168.1.44",8080)) # 发送了一份数据到192.168.44:8080，python3里sokect发送数据必须是字节码b。
		#接收数据
		s1.recvfrom(1024) ＃表示本次接收最大字节数为1024
		
		#端口问题及端口绑定：用了socket的程序，操作系统每次分配的porn都是随机的。
		binAddr = ('ip',porn) #ip一般不写，因为一台电脑可能有多个ip，如以太网，wifi，虚拟机。
		s1.bind(binAddr) # 绑定端口
		
		＃python3编码问题
		data = "数据"
		s1.sendto(data.encode("utf-8"),address) #python3里socket必须是bytes-like不能是str或其他，我们把数据转成utf-8再发送和在数据前
											　　＃加个ｂ的效果是一样的，若接收方出现乱码，只有可能是接收方的解码方式不是utf-8。
		redata = s1.recvfrom(1024)
		print(redata.decode("utf-8") #把接收到的数据解码成utf-8,若出现乱码，只有可能数据发送方的数据格式不utf-8
		
		
多线程模拟ＱＱ聊天：
	看视频！
	多线程和全局变量的使用
	收和发这两个线程全双工非堵塞
```




 














		
		
		
		
	
		
