# 有点儿难啊！ 兄弟！
import requests
from lxml import etree

class dongman:
    def __init__(self):
        # self.name = name
        self.url = "https://manhua.dmzj.com/rexuegaoxiao/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 提取数据及下一个url，用到etree
    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        # 使用xpath方法
        a_list = html.xpath("/html/body/div[3]/div[2]/div[1]/div[4]/ul/li/a")

        content_list = []
        for a in a_list:
            item = {}
            item["title"] = a.xpath("./text()")[0] if len(a.xpath("./text()")) > 0 else None
            item["href"] = a.xpath("./@href")[0] if len(a.xpath("./@href")) > 0 else None
            item["img_list"] = self.get_img_list(item["href"])  # 详情页url
            content_list.append(item)
            print(item)
        return content_list

    def get_img_list(self, detal_url): # 获取帖子的图片
        return 'https://manhua.dmzj.com' + detal_url

    def get_img(self, content_list):
        n = 1
        for content in content_list:
            image_first = self.parse_url(content["img_list"]+'#@page={}'.format(n))
            print(content["img_list"]+'#@page={}'.format(n))
            html = etree.HTML(image_first)
            # print(image_first)
            print(etree.tostring(html).decode())
            photo = html.xpath("//*[@id='center_box']/img/@src")
            print(photo)


    def save_img(self, content_list):
        pass

    def run(self):
        # 构建url
        # 发送请求 获取响应
        html_str = self.parse_url(self.url)
        # 提取全部url及数据
        content_list = self.get_content_list(html_str)
        self.get_img(content_list)


if __name__ == '__main__':
    Dongman = dongman()
    Dongman.run()