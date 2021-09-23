import json
import requests
import re
# json.dumps("\u200b",ensure_ascii=False)
class Qb(object):
    def __init__(self):

        self.next_url = "https://www.qiushibaike.com/text/?page={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}


    def parse_url(self,i):
        response = requests.get(url=self.next_url.format(i), headers=self.headers)
        print(response.url)
        dict_ret = response.content.decode()
        content_list = re.findall(r'''content: "(.*?)"''', dict_ret)
        print(content_list)
        print("--------------")


    def run(self):
        for i in range(1, 10):
            self.parse_url(i)


if __name__ == '__main__':
    qb = Qb()
    qb.run()