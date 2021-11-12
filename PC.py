import requests
from bs4 import BeautifulSoup
import re

urls = 'https://weibo.com/'
strurl = requests.get(urls)
soup = BeautifulSoup(strurl.text,'lxml')
print(soup)
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
for item in data:
    result ={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
    print(result)