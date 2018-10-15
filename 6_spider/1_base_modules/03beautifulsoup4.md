# BeautifulSoup简介：
    是什么？
        ：一个灵活又方便使用的网页解析工具。

# 网页解析？
网页由html的众多标签组成，因此解析网页分为两步：
```python

 1.精准定位到标签 (那么如何精确定位标签呢：依靠标签名和标签属性值)
 2.从标签提取内容（内容一般存储在两个位置中：标签内容和标签属性值，比如<p>\<a href="www.douban.com">豆瓣电影</a></p>） 
```
BeautifulSoup分为三部分：1.标签选择器、2.css选择器、3.标准选择器（结合了1和2）




# 使用：
```python {.line-numbers}
import requests
import lxml
from bs4 import BeautifulSoup as bs

response = requests.get(url)
response.encoding = 'utf-8'
html = bs(response,'lxml')

'''标签选择器（只会返回一个匹配结果）'''
html.p              #选择元素
html.p.a.text       #提取标签内容
html.p.a['href']    #提取标签属性值

'''css选择器(通过select()方法，return list)'''
html.select('.css_class .other_class')  #类 class选择器
html.select('#only_id')                 #id选择器
html.select('ul li p  a')               #也可以用css选择器筛选标签

html.select('ul').attrs['id']           #获取属性
html.select('ul').get_text()            #获取内容

'''标准选择器:主要有find() 和 find_all()
find返回一个，因此整个beautifulsoup要重点掌握的只有find_all ,返回list
'''
html.find_all('p')                                  #返回所有p标签
html.find_all(attrs={'id':'only_id'})               #查找标签中css的id为only_id的标签
html.find_all('p',attrs={'class':re.compile("^h")}) #还可以使用正则匹配
html.find_all('p',attrs={'class':True})             #含有class属性的p标签即可
```

# 小结：
1. 整个beautifulsoup其实只要重点掌握find_all()方法。
    

# 参考：
* [如何抓取web页面——by Binuxの杂货铺](https://binux.blog/2013/09/howto-crawl-web/)
* [《python3网络爬虫开发实战》](https://germey.gitbooks.io/python3webspider/4.2-BeautifulSoup%E7%9A%84%E4%BD%BF%E7%94%A8.html)
* [BeautifulSoup全面总结](https://zhuanlan.zhihu.com/p/35354532) 

* [Beautiful Soup 4.4.0 文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)