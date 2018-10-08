'''
抓取猫眼电影top100，尝试使用re，bs，pyquery三种方式
'''

import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re 
from bs4 import BeautifulSoup 
from pyquery import PyQuery


class Spider():
    def __init__(self):
        self._offset = [i*10 for i in range(10)]
        self._start_url = 'http://maoyan.com/board/4?offset='
        self._headers ={

            'authority': 'maoyan.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'dnt': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://maoyan.com/board',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cookie': '__mta=218012585.1538981667639.1538981673705.1538981686563.3; uuid_n_v=v1; uuid=FE84C6D0CAC611E8AA50ABE1D211078969785635695242E58890BD3D48E0B78C; _csrf=69cdbd5979e5389728ab53687cc9dee410baeaaa5e7474988247cc46d931116a; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=1665274a1e8c8-0ed8111757e5d9-3c7f0257-100200-1665274a1e9c8; _lxsdk=FE84C6D0CAC611E8AA50ABE1D211078969785635695242E58890BD3D48E0B78C; __mta=218012585.1538981667639.1538981667639.1538981673705.2; _lxsdk_s=1665274a1ea-36c-1f7-1e7%7C%7C8',
          }

    def get(self,offset):
        try:
            html = requests.get(url=self._start_url + str(offset), headers=self._headers)
            if html.status_code != 200:
                print('server error:',html.status_code)
                return None
            html.encoding = 'utu-8'
            return html.text

        except RequestException:
            print('requests get error!')
            return None
    
    def parse(self,html):
        '''使用正则'''
        #pattern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?jpg).*?boarditem-click.*?>(.*?)</a></p>' +
        #'.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
        #content = pattern.findall(html)
        #
        #if content != None:
        #    
        #    for  item in content:
        #        yield {
        #            'top':item[0],
        #            'pic':item[1],
        #            'name':item[2],
        #            'actor':item[3],
        #            'time':item[4],
        #            'score':item[5] + item[6]
        #
        #        }


        '''使用bs4'''
        #soup = BeautifulSoup(html,'lxml').select('.board-wrapper')
        #for item in soup[0].find_all('dd'):
        #    if item != None:
        #        
        #        yield{
        #
        #            'index':item.i.get_text(),
        #            'pic':item.select('.board-img')[0]['data-src'].partition('.jpg')[0] + '.jpg',
        #            'name':item.select('.name')[0].get_text(),
        #            'star':item.select('.star')[0].get_text().strip(),
        #            'releasetime':item.select('.releasetime')[0].get_text(),
        #            'score':item.select('.integer')[0].text + item.select('.fraction')[0].text
        #        }
        '''使用pyquery'''
        pq = PyQuery(html)('.board-wrapper')('dd').items()
        for item in pq:
            if item != None:
                yield{
                        'index':item('.board-index').text(),
                        'data-src':item('.board-img').attr('data-src').partition('.jpg')[0] + '.jpg',
                        'name':item('name').text(),
                        'star':item('.star').text().strip(),
                        'releasetime':item('.releasetime').text(),
                        'score':item('.integer').text() + item('fraction').text()
                    }

            else:
                print('parse error!')
                return None

    def store(self,item):
        print(item)
        with open('./maoyan.json','a',encoding='utf-8') as f:
            f.write(json.dumps(item,ensure_ascii=False) + '\n')
            
    def main(self,url):
        html = self.get(url)
        for item in self.parse(html):
            self.store(item)


    def __call__(self):
        #开启多进程
        p = Pool()
        p.map(self.main,self._offset)
        
        
if __name__ == "__main__":
    spider = Spider()
    spider()
 

    
        
    
    
    
    

        
    
        