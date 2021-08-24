'''
爬虫流程
模拟浏览器，向服务器发送http请求，服务器接收到请求，返回数据
思路
1.打开书籍详情，返回详情页的所有数据
2.请求并成功那大详情页数据之后，筛选数据
3.保存到本地
'''

'''
筛选数据步骤：
    1提取所有小说章节名称
    2提取所有小说章节a标签中的值，对主域名做字符串拼接
    3二次请求主域名进入书籍内容页
    4在小说内容中提取小说内容数据
    5保存数据
'''
import requests
from bs4 import BeautifulSoup
# pip install lxml     lxml美化显示格式



# 获取网站相应数据
response = requests.get('http://biquw.com/book/94/').text
soup = BeautifulSoup(response, 'lxml')

data_list = soup.find('ul')
for book in data_list.find_all('a'):
    # print('{}:{}'.format(book.text, 'http://www.biquw.com/book/94/'+book['href']))
    book_url = 'http://www.biquw.com/book/94/' + book['href']
    data_book = requests.get(book_url).text
    soup = BeautifulSoup(data_book, 'lxml')
    data = soup.find('div', {'id': 'htmlContent'}).text
    print(data)

    with open('/Users/leon/Desktop/rr/venv/xiaoshuo.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')

    if book_url == 'http://www.biquw.com/book/94/73174.html':
        break









