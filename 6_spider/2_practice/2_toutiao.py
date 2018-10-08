'''分析ajax 抓取今日头条街拍图片'''

import requests
from requests import RequestException
import json
import re
import time

x = 0
class Toutiao:
    def __init__(self):
        self._headers = {
            'authority': 'www.toutiao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cookie': 'tt_webid=6609203078057461262; tt_webid=6609203078057461262; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=166491e30ed452-08f4128769ff6a-3c7f0257-100200-166491e30ee61; tt_webid=6609203078057461262; csrftoken=919bd60a2e36efbade63cb66116afcd2; __tasessionId=q6wix21rr1538901079793; CNZZDATA1259612802=966679360-1538820661-https%253A%252F%252Fwww.google.com%252F%7C1538896834',
        }
        self._page_url = 'https://www.toutiao.com/search_content/'
        self._gallery_url = 'https://toutiao.com'

    # one page get 20 gallery
    def page_get(self,offset):
        payload = {
            'offset':offset,
            'format':'json',
            'keyword':'街拍',
            'autoload': 'true',
            'count': 20,
            'cur_tab': 3,
            'from': 'gallery'
        }
        try:
            page = requests.get(url=self._page_url,params=payload,headers=self._headers)
            if page.json()['data']:
                return page.json()
            else:
                print('offset 溢出，已爬完')
                return None
        except RequestException:
            print('requests page_get() error')
            return self.page_get(offset)

    #解析page，获得20个相集的url地址和title，返回相集list
    def page_parse(self,page):
        if page:
            '''test '''
            global x 
            x += len(page['data'])
            gallery_list = []
            for gallery in page['data']:
                if 'title' in gallery and 'source_url' in gallery:
                    gallery_list.append(
                        {
                            'title':gallery['title'],
                            'source_url':gallery['source_url']
                        }
                    )
            return gallery_list
        else:
            return None

    #获得每个相集里面的相片的url，每个相集的url个数不定，返回单个相集的相片url list
    def gallery_get_url(self,source_url):
        try:
            html = requests.get(url=self._gallery_url + source_url,headers=self._headers)
            if html.status_code == 200:
                pattern = re.compile('JSON.parse\((.*?)\)',re.S)
                try:
                    data = pattern.findall(html.text)[0]
                    #匹配到的字符串是js能解析的json，包含转义，需要两次json.loads,尼玛神奇了
                    if data:
                        try:
                            data = json.loads(data)
                            data = json.loads(data)
                            url_list = []
                            for urls in data['sub_images']:
                                url_list.append(urls['url'])
                            return url_list
                        except:
                            print('json error')
                            return None
                except:
                    print("regrex error")
                    return None
        except RequestException:
            print('requests gallery_get_url() error')
            return self.gallery_get_url(source_url)

    #把每个相集的url list和title整合成字典，作为最小单元存储
    def gallery_item(self,gallery_list):
        if gallery_list:
            for gallery in gallery_list:
                url_list = self.gallery_get_url(gallery['source_url'])
                yield {
                    'title':gallery['title'],
                    'url':url_list
                }
                

    #存储一个相集
    def store(self,item):
        if item:
            print(item)
            with open('jiepai.json','a',encoding='utf-8') as f:
                f.write(json.dumps(item,ensure_ascii=False) + '\n')

    #一个offset流程
    def main(self,offset):
        page = self.page_get(offset)
        gallery_list = self.page_parse(page)
        if gallery_list:
            for item in self.gallery_item(gallery_list):
                self.store(item)

    def __call__(self):
        offset = 0
        while True:
            pad = self.page_get(offset)
            if pad:
                self.main(offset)
                offset += 20
            else:
                print('done!,offset:',offset-20)
                break

if __name__ == '__main__':
    toutiao = Toutiao()
    toutiao()
    print('\n','total gallery:',x)

    
    



