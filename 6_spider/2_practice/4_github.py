'''
理解：模拟登录的原理
''''

import requests

cookies = {
    'has_recent_activity': '1',
    '_octo': 'GH1.1.1476296714.1539146950',
    'logged_in': 'no',
    '_gh_sess': 'MHMwNXJ2YTB1NUlLRURFM3poVlVRWWNjbTJDTTlRZFhVRnFQQmJMNnVPMjlKU09BVFU2ZGMwL3VydnF2V3A5ZGZzSTM1UHJ1OHYrOUorOWNhdlI0VTZ6Wmk3ejUxNzhxdHh4b2hZQUc1WXN4NVFVVEFlL3A0alpNTUtJbFR5ODZ5TXQwcDZhMVlScXdoV0xncE9nWFkya3UwSUFEL0RuRmJJaHpDeGx2Z2FOaVU4UU9pV1dGRjdnUS9uamJidnVPOVBqcDlxaU5LNFJnZWJYOXN1bkpuY0ZDOFpKY1JDdW1UR2M5Y3ZjN0R2K21neDJXcGF1WVNQRWJlcWlIVlRYczg3Y0JsQmpKZEorTjNxVnFvNlc2RGVvK1k3b3FhYk5TeHFrdHZ0bnJWTk1KZENES3JTb3ZWbUtkZlhQQzVIQVQtLUJ5ZmgwZnh1WDVETnp0ckdEcGRmOEE9PQ%3D%3D--257dbb5f405c9cd5fde72cbd1c3e263cee966160',
    'tz': 'Asia%2FShanghai',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://github.com',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

data = {
  'commit': 'Sign in',
  'utf8': '\u2713',
  'authenticity_token': 'ptZsmIbd6yMFB/A208W5uU7LWhwSC+7Op/DgSzXRFqGWYiD8BDcYGpZpucCAzx99HmyRPMg6sEq6hLh6nSY6rA==',
  'login': 'xiaoyupang.email@gmail.com',
  'password': 'G@xiaoyu1994'
}
session = requests.Session()
r1 = session.post('https://github.com/session', headers=headers, cookies=cookies, data=data)
