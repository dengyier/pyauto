
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt').content
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# print(soup.prettify())
tags = soup.find_all('div',class_ ='result')
print(tags)