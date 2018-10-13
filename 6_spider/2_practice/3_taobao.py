'''selenium 模拟浏览器抓取淘宝商品类信息
1.了解为什么要用selenium爬取，是否可以不用selenium就可以爬取
2.掌握selenium爬取的流程
3.

'''


from pyquery import PyQuery
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait           #等待
from selenium.webdriver.support import expected_conditions as EC    #触发条件
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Taobao:
    def __init__(self):
        self._cookie = {
            'cookie': 'thw=cn; t=25f8f20687ac8ef27b4b50b0f1ed32b5; cookie2=1bc1fe3eeaba6c7fa74040e94fe7328b; _tb_token_=55ed30ee7b7e3; cna=3cQ4FPyrShICAXBhO5oL7CiN; alitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; tg=0; _m_h5_tk=c243e1a6c8bb60957b1f84b2c7af1513_1539073326149; _m_h5_tk_enc=5599157ddf43b3236944eb1cf7208d0f; enc=WuqSbiVmqiVr04PoLAfBYf%2F5KEakaplXDzgZR089a8SRZbx6IE9BwxqvJJZC8Mdlu1SW10Fr29igqr2noJCgxw%3D%3D; swfstore=135593; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; unb=1600751817; sg=%E7%BE%BD76; _l_g_=Ug%3D%3D; skt=7feb089078ea4f61; cookie1=AQcn7EV97hQVL%2BnJuk4KBOR3GsgBtQReRTEoeJRMuPg%3D; csg=50141950; uc3=vt3=F8dByRqvNdhPgmMmTw8%3D&id2=Uoe0bU9BCifBRQ%3D%3D&nk2=pkStuDoc&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTUzOTA4OTA2MQ%3D%3D; tracknick=%5Cu5E9E%5Cu6F47%5Cu7FBD; lgc=%5Cu5E9E%5Cu6F47%5Cu7FBD; _cc_=WqG3DMC9EA%3D%3D; dnk=%5Cu5E9E%5Cu6F47%5Cu7FBD; _nk_=%5Cu5E9E%5Cu6F47%5Cu7FBD; cookie17=Uoe0bU9BCifBRQ%3D%3D; lastalitrackid=login.taobao.com; JSESSIONID=9E19739AC241F6F419F92C456D4D425F; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTfItCvCtIQow%3D%3D&tag=8&lng=zh_CN; mt=ci=0_1; isg=BExMGnnLeyMAtW_YTNtNDqJrHaO-LdvGvHqz96YNUfeaMew7z5aWv0aL1XGsfSiH; whl=-1%260%260%261539089072164'

        }

        self._url = 'https://s.taobao.com/search?q=iPad' 
        self._chrome = webdriver.Chrome()
        self._wait = WebDriverWait(self._chrome,10)
        
    def parse(self,html):
        pq = PyQuery(html)('.grid g-clearfix .items ')
        for item in pq('.item J_MouserOnverReq  ').items():
            print(item)

        
    def store(self,items):
        pass

    def store_one_page(self,html):
        pass

    def main(self):
        
        try:
            
            self._chrome.get(self._url)
            #等待商品加载完后，解析和存储 第一页的product
            print(self._chrome.page_source)
            self._wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR('.grid g-clearfix')))
            )

            self.parse(self._chrome.page_source)

            #获取index
        except:
            print("requets error")
            
if __name__ == '__main__':
    taobao = Taobao()
    taobao.main()

            



            



    
        
    