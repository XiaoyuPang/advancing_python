
# requests简介：
	“唯一的一个非转基因的 Python HTTP 库，人类可以安全享用”
# 安装 
	pip3 install requests
# 基础用法:
请求:
```python {.line-numbers}
import requests

'''get请求'''
r = requests.get(url）
# 可选参数：
headers = headers		#构造请求头，为dict类，如headers可设置user-agent
auth = ('user','passd')		#某些网站需要登录才能访问
params = payload		#params为构造url传递参数
cookie = cookie			#传递cookie 
allow_redirects = False		#禁用重定向
timeout = number		#设置超时，单位为秒;
proxies=proxies			#代理设置
verify=False #设置忽略ssl证书验证

'''post请求'''
r = requests.post(url)
#可选参数
data=payload		#发送post表单数据，payload为dict类，data会自动编码为表单形式；若想发string，可data=json.dumps(payload)转化
json=payload 		#也可直接用json直接传递 ，内部自动化为json数据
files=files		#传递多部分编码(Multipart-Encoded)数据，如上传文件files={'file':open("my.xx","rb")}

'''其他：(如delet、put、update等http方法也类似，这里略过)'''
```
响应:
```python {.line-numbers}			

r.status_code		#响应状态
r.headers		#响应头，字典对象
r.encoding		#响应文档html的编码格式,可用 r.encoding="utf-8" 改变编码格式
r.text			#响应内容，为str对象
r.json()		#处理json数据，响应必须是json才能使用，否则报错
r.content		#以字节（bytes）请求响应体(非文档，如图片)
r.raw			#来自服务器的原始套接字响应，确保stream=True，读取方式--> r.raw.read()
r.cookies		#该响应是字典对象,r.cookies.get_dict(),或者for key,value in r.cookies.items():  print(key,value)
r.url			#显示请求的url
```

# 高级用法:

```python {.line-numbers}
'''session'''
#为了保持跟踪会话，每次访问不同页面都要传递cookies会非常麻烦，使用requests提供的session对象轻易解决：

s = requests.Session()	#构造session对象
s.get(url)		
print(s.cookies)


'''证书验证'''
Verify = False   	#默认为True。使用场景：12306类似网站
cert = '证书路径' 	#自己指定本地证书，一般用不到

'''代理'''
proxies = {'http':'http://user:passwd@ip:port'} #指定http的代理
						#若想使用sockes代理： pip install 'requests['socks']'
						# proxies = {'http':'socks://xxxx'}

'''超时'''
timeout = xxx    		#单位为秒

'''认证设置'''
#比如有些网站要登录后才能访问，参数auth
auth = （’user',"passwd")

'''异常处理'''
#requests.exceptions有很多种异常，具体查看requests api
from requests.exceptions import ReadTimeOut,HTTPError,RequestException
try:
	r = requests.get(url,timeout=xxx)
except ReadtimeOut:
	print('ReadTimeOut')
except RequestException:
	print('RequestsExecption')

```


# 参考：

* [python-requests中文手册](http://docs.python-requests.org/zh_CN/latest/index.html)
* [python3网络爬虫开发实战](https://germey.gitbooks.io/python3webspider/3.2-%E4%BD%BF%E7%94%A8Requests.html)



























