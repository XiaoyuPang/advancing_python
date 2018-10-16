# PyQuery简介：
    是什么？
        ：强大又灵活的网页解析库。
    VS BeautifulSoup/Regex？
        :正则写起来太麻烦，bs语法难记。只要熟悉jquery，pyquery是很好的代替品。

# 安装：
    pip3 install pyquery


# 初始化:
```python {.line-numbers}
import requests
from pyquery import PyQuery as pq

'''字符串初始化'''
response = requests.get(url)
response.encoding = 'utf-8' 
html = pq(response.text)

'''url初始化'''
html = pq(url="https://www.douban.com")

'''文件初始化'''
html = pq(filename='demo.html')
```
# 基本使用:
1. 标签选择器
```python {.line-numbers}


#获取标签
html('p')                #获取所有p标签

#嵌套选择
html('p h1')             #选择p标签内的h1标签 ，有空格隔开 

#获取多个元素
for i in html('p').items():     #循环获取每一个p标签，需要items()方法
    print(i)   

#获取文本
html('p').text()         #打印所有p标签内的文本，不如p内嵌的p、h1~6的文本，但a之类的非文本标签的文本不会被打印。

#获取html
html('p').html()         #打印除了<p>内的所有内容</p>也就是除了<p>和</p>两个标签

#获取属性值
html('a').attr('href')   #打印a标签的href属性值
```


2. css选择器
```python {.line-numbers}
html('#out.inner')        #没有空格隔开，说明不是嵌套选择，而是查找同时带有out和inner css属性值的标签。
html('#outlook .inner')   #内嵌选择，类似标签的嵌套选择，需要空格隔开
html('#outlook p')         #css选择器和标签选择器一起使用，表示选择id为outlook的标签内的p标签
```

3. DOM操作
```python {.line-numbers}
'''addClass 和 removeClass'''
li = html('#out.inner')
li = removeClass('.inner')     #把inner css属性值从example标签删除
li.addClass('.inner')          #往example标签添加inner css属性值

'''attr 和  css'''
li.attr('name','user')      # 若li标签没有name属性，则为li标签添加name='user'属性值，有的话则覆盖
li.css('font-size','14px')  #若li没有font-size css属性值，则添加style="font-size:14px",有则覆盖

'''remove：'''
p = html('p')
p('h1').remove()    #删除p标签内的h1标签
```
        
# 小结：
1. pyquery比起beautifulsoup的语法要更简介，推荐作为解析网页的第一首选。

# 参考 
* [《Python3网络爬虫开发实战》](https://germey.gitbooks.io/python3webspider/4.3-PyQuery%E7%9A%84%E4%BD%BF%E7%94%A8.html)
* [pyquery: a jquery-like library for python](https://pythonhosted.org/pyquery/#quickstart)
* [如何从 WEB 页面中提取信息——by Binuxの杂货铺](https://binux.blog/2014/07/how-to-extract-data-from-web/)





        


     