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
        self._headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    def get(self,url):
        try:
            html = requests.get(url,headers=self._headers)
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
        p = Pool(10)
        p.

        
                      

if __name__ == "__main__":
    spider = Spider()
    spider()
 

    
        
    
    
    
    

        
    
        