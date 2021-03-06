# selenium 简介：
    是什么？
        ：一个用来做web自动化测试的工具，支持多种浏览器(如：Chrome、Firefox、PhantomJS）。
    做什么？
        ：主要是发一些指令驱动浏览器做各种动作，比如：跳转、点击、输入、下拉等等操作。
    在爬虫中应用？
        ：在爬虫中，应用selenium解决JavaScript渲染问题，因为有些网页是由js渲染的，requests获取后无法执行js来渲染。

# 安装:
```python {.line-numbers}
pip3 install selenium   #安装chromedriver：把chromedriver复制环境变量，如/usr/bin
```

# 基本使用：
```python {.line-numbers}
from selenium import webdriver                  #浏览器驱动对象
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()                    #声明驱动对象
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id('kw')    #百度的input输入框
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)                 #模拟回车键
    wait = WebDriverWait(browser,10)            #调用等待
    #等待某个元素加载，这里等待content_left
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))  
    print(browser.get_cookie)
    print(browser.current_url)
    print(browser.page_source)
finally:
    browser.close()
```

# 查找元素：
```python {.line-numbers}
'''单个元素'''
browser.find_element_by_id('#q')
                     by_css_selector()
                     by_xpath()
                     by_name()
                     by_class_name()
                     by_tag_name()
                     by_link_text()
                     by_partial_link_text()

'''多个元素'''
browser.find_elements_by_id('#q li q')
                      by_xxx(同单个元素一样)

'''通用方式（return list)'''
browser.find_element(By.ID,'#q')            #单个元素，选择器变成大写
browser.find_elements(By.ID,'#q li p')      #多个元素
```

# 元素交互：
```python {.line-numbers} 
browser.get("https://www.taobao.com")
input = browser.find_element_by_id('q')                             #淘宝的搜索输入框
input.send_keys('iphone')                                           #输入iphone
input.clear()                                                       #清空输入框
input.send_keys('ipad')                                             #输入ipad
button = browser.find_element_by_class_name('btn-search')           #输入框的提交按钮
button.click()                                                      #点击提交
```

# 交互动作 actionChains：
```python {.line-numbers}

'''元素交互必须指定特定元素，在某些情况下比如拖拽，需要将动作附加到动作链中串行执行'''
from selenium.webdriver import ActionChains

browser.get(url)
browser.switch_to.frame('iframeResult')                             #查找到指定frame内并切入进去
source = browser.find_element_by_css_selector('#draggable')         #查找frame内要拖拽的元素
target = browser.find_element_by_css_selector('#droppable')         #查找frame内要装载的元素
actions = ActionChains(browser)                                     #建立动作链对象
actions.drag_and_drop(source,target)                                #初始化
actions.perform()                                                   #开始执行动作，把draggable拖拽到droppable
```

# frame:
```python {.line-numbers}
'''
frame在网页里经常用到，frame相当于一个独立的网页
当browser切入子frame时，是无法查找子frame之外的元素的，这时需要用到切换到父frame查找
'''
browser.switch_to_frame('iframeResult')           #从父frame可以切换到子frame
browser.switch_to_parent_frame()                  #从子frame切换到父frame,无需参数
```

# 元素信息获取：
```python {.line-numbers}
browser.get(url)
p = browser.find_element_by_name('xxx')
print(p.get_attribute('class'))                           #获取属性
print(p.text)                                             #获取文本
print(p.id)                                               #获取id
print(p.location)                                         #获取位置，x和y轴
print(p.tag_name)                                         #获取标签名
print(p.size)                                             #获取 height width

'''cookie操作'''
print(browser.get_cookies())                              #获取cookies
browser.add_cookie({'name':'lisa','age':18})              #添加cookie
browser.delete_all_cookie()                               #删除cookie
```

# 异常处理
```python {.line-numbers}
'''浏览器有各种异常，比较难处理,查看官方api了解各种异常'''
try:
    browser.get(url)
except TimeoutException:
    print("time out")
try:
    browser.find_element_by_css_seletor("xxx")
except NoSuchElementExeception:
    print("no element")
```

# 前进和后退：
```python {.line-numbers}
browser.get(url_1)
browser.get(url_2)
browser.get(url_3)
browser.back()          #回到url2
browser.forward()       #回到url3
```

# 等待:
```python {.line-numbers}
'''
selenium加载js时不一定会完全加载完，这时候需要添加一些时间来等待。等待分为显示和隐式。
隐式等待:
    设置一段时间（默认为0），当webDriver没有找到元素时，则此后等待继续查找（若找到则不等待），
    超过这段时间还找不到元素，则抛出查找不到元素异常。
显式等待：
    设置一个等待时间和等待条件，在等待时间内达到某个条件则跳出等待，否则继续等到设置的时间段，然后抛出异常。
'''

#隐式等待
browser.implicitly_wait(10)
browser.get(url)            
input = browser.find_element_by_css_seletor("q")   #如果网速特别漫这个元素没有被加载出来，则会等待10s
#显示等待
browser.get(url)
wait = webDriverWait(browser,10)
input = wait.until.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clicBy.CSS_SELETOR,'btn-search')))
print(input,button) 
#其他一些条件等等
title_is            #标题是xxx
alter_is_present    #出现警告窗口
title_contain       #标题包含某文字
```

# 执行js：
```python {.line-numbers}
browser.execute_script('传入的js代码')
```

# 选项卡管理（浏览器的标签页）：
```python {.line-numbers}
'''通过执行js来实现新建标签页'''
browser.get(url_1)                                          #请求一个url也就打开了一个新标签
browser.execute_script('window.open()')                     #再打开一个空的标签页
print(browser.window_handles)                               #输出当前浏览器标签页的信息
browser.switch_to_window(browser.window_handles[1])         #切换到空的那个标签页
browser.get(url_2)                                          #在空的标签页访问另一个url
browser.switch_to_window(browser.window_handles[0])         #切换回第一个标签页
```

# 小结：
1. selenium需要配合浏览器一起使用,需要安装对应浏览器的webdriver。
2. 使用场景：web页面由js动态渲染，并且无法分析拿到后台api，这时只能靠浏览器渲染后获取数据。
3.  selelnium+browser这种方式做爬虫非常低效，尽量避开使用。
# 参考
* [selenium-python中文文档](https://selenium-python-zh.readthedocs.io/en/latest/)
* [《python3网络爬虫开发实战》](https://germey.gitbooks.io/python3webspider/7.1-Selenium%E7%9A%84%E4%BD%BF%E7%94%A8.html)
* [崔广宇：爬虫和反爬虫现状解析](https://gitbook.cn/books/590be8980067927e7860e96e/index.html)
* [python爬虫的一些总结](http://ningning.today/2015/10/04/python/Python%E7%88%AC%E8%99%AB%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93/)




















                            



    