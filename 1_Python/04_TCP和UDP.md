```python {.line-numbers}

udp单播：１对１
udp多播：１对多
udp广播：１对所有。tcp无广播。一台电脑发送了一份udp广播，由交换机复制多份给每台计算机
	ｓ.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) ＃发送广播数据必须添加这句
	dest = ('<broadcast>',7788) #<broadcast>可以代替本段网络的广播ip,也可写真实的数字ip，但用字母方式好。只有该端口号一致才能接受
	s.sendto("hi",dest) 
	
tcp服务器：
	serverSocket = socket(AF_INET,SOCK_STREAM)　＃创建socket套接字
	serverSocket.bind(("",7788))			＃绑定端口和本地ip
	serverSocket.listen(5)　		＃listen使得套接字变为可以被动连接，最大监听数５
	＃accept等待客户端的连接
	clientSocket,clientInfo = serverSocket.accept() #clientSocket表示这个新的客户端，clientInfo表示这个新客户的ip和端口。
	recvData = clientSocket.revc(1024)　＃udp里接收/发送数据是recvfrom/sendto,tcp里是recv/send。
	print("%s:%s" %(str(clientInfo),recvData)) 
	clientSocket.close() # 关闭这个客户，就不能再为这个客户端服务
	serverSocket.close() # 关闭服务，程序不再接收任何新的客户。
	
tcp客户端：
	clientSocket = socekt(AF_INET,SOCK_STREAM) 
	clientSocekt.connect(("192.168.1",7788)) 	#connect用于客户端连接服务端，连上后，以后发数据都不用再填写对方ip，udp每次都要填ip。
	clientSocket.send("haha".encode("utf-8"))　＃连上服务端就发送一份数据
	recvData = clientSocket.recv(1024)　＃等待接收数据，堵塞，直到收到服务端发来的数据
	print("recvData:%s" % recvData)
	clientSocket.close()
	
	
子网掩码：
	由于ip地址＝网络号＋主机号，我们拿到一个ip地址并不知道它是ＡＢＣＤＥ哪个类，因此引入子网掩码，如Ｃ类子网掩码为255.255.255.0
	子网掩码　＆（按位与）　ip地址＝网络号
	
集线器和交换机：
	集线器收到的数据都会以广播形式发送出去，集线器有将信号放大功能。
	交换机能够选择目标端口，在计算机网络，数据链路层对mac地址的解析在交换机上。
	
tcp三次握手：
	客户端发送ａ　到服务端
	服务端拿到ａ后，把（ａ＋１，ｂ)发送给客户端
	客户端拿到数据后，再向服务端发送　ｂ+1 。　　三次握手完成
	
tcp四次挥手:
	客户端调用close()关闭连接时会发送一个数据包通知服务端“我这边要关闭了”
	服务端收到后，给客户端发送确认收到
	服务端调用close()时会给客户端发送一个数据包通知客户端“我这边也要关闭了”
	客户端收到，发送一个确认收到　。
	【注：每次调用close()都会发送一个数据包】

长链接和短链接：
	短链接：每发送一个数据都要经过三次握手和四次挥手。适合资源少，【浏览器，web服务】
	长链接：只要双方连接上，可以发送完所有数据后，再四次挥手。适合资源多【打游戏，观看视频】
```























	
	
	
