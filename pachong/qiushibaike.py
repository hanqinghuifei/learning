

import requests
import re
import json


class Neihan():
    def __init__(self):
        self.start_url = 'https://www.qiushibaike.com/text/'
        self.next_url = "https://www.qiushibaike.com/text/?page={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url_start(self): #发送第一页请求，获取第一页响应
        pass

    def parse_url(self):    # 发送第二页以后的请求，获取响应
        pass

    def parse_content_start(self):
        pass

    def parse_content(self):
        pass






if __name__ == '__main__':
    nh = Neihan()
