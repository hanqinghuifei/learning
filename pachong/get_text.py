#coding:utf-8

import requests
from lxml import etree
import os
import time
import random

url = "http://www.xbiquge.la/xiaoshuodaquan/"
class Book(object):
    def first(self):
        response = requests.get(url)
        html = etree.HTML(response.text)  # html 结构化
        First_list = html.xpath('//div[@class="novellist"]/ul/li/a/@href')      # 取得第一个的地址
        First_list_name = html.xpath('//div[@class="novellist"]/ul/li/a/text()')        # 获取第一个名字
        print(First_list_name)
        for first, first_name in zip(First_list, First_list_name):
            if os.path.exists(first_name) == False:    # 判断当前路径下有没有此文件夹
                os.makedirs(first_name)   # 创建文件夹
            self.second(first, first_name)
    def second(self, first, first_name):
        response = requests.get(first)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        Second_list = html.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a/@href')       # 取得每章的地址
        Second_list_name = html.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a/text()')     # 获取每章的名字
        for second, second_name in zip(Second_list, Second_list_name):
            print(second)
            self.third(second, second_name, first_name)
    def third(self, second, second_name, first_name):
        a = first_name
        b = second_name
        response = requests.get("http://www.xbiquge.la" + second)
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)
        Third_list = "\n".join(html.xpath('//div[@class="content_read"]/div[@class="box_con"]/div[@id="content"]/text()'))  # 获取章节
        file_name = first_name + "\\" + second_name + ".text"
        print("正在写入文件" + file_name)
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(Third_list)



book = Book()
time.sleep(random.random()*3)
book.first()
