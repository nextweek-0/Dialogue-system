import re
import requests
from bs4 import BeautifulSoup
import urllib


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return

# 爬取网上回答
def pachong_answer(question):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    url = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q={}'.format(urllib.parse.quote(question))
    try:
        try:
            demo = getHTMLText(url)
            soup = BeautifulSoup(demo, 'html.parser')
            baike_url = soup.find_all('a', attrs={'class': "mh-more-detail"})
            if len(baike_url) == 0:
                baike_url = soup.find_all('a', attrs={'class': "detail"})
            baike_url = baike_url[0]['href']
            baike_demo = requests.get(baike_url, headers=headers).content.decode('utf-8')
            baike_soup = BeautifulSoup(baike_demo, 'html.parser')
            answer = baike_soup.find_all('div', attrs={'class': "entry-card-content"})[0].p
            answer = ''.join(answer.find_all(text=True))
            if len(answer) == 0:
                return '换个问题呗'
            return answer
        except:
            demo = getHTMLText(url)
            soup = BeautifulSoup(demo, 'html.parser')
            baike_url = soup.find_all('a', attrs={'class': "detail"})
            if len(baike_url) == 0:
                return '请换一种提问方式'
            baike_url = baike_url[0]['href']
            baike_demo = requests.get(baike_url, headers=headers).content.decode('utf-8')
            baike_soup = BeautifulSoup(baike_demo, 'html.parser')
            answer = baike_soup.find_all('div', attrs={'class': "card_content"})[0]
            answer = ''.join(answer.find_all(text=True))
            if len(answer) == 0:
                return '换个问题呗'
            return answer
    except:
        return '我不会哎'

# print(pachong_answer('刘备'))

# print(len(None))
