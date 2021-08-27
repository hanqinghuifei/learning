import requests
import json


class doubanSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        self.start_url ="https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=ios&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=1629970613072"


    def prase_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        print(response.content.decode())
        return response.content.decode()


    def get_content_list(self, get_url):
        json_str = json.loads(get_url)
        print(json_str)
        print(type(json_str))

        # 取subject_collection_items的值
        total = json_str["total"]
        content_list = json_str["subject_collection_items"]
        return content_list, total


    def save_data(self, content_list):
        with open("douban.txt", "a", encoding="UTF-8")as f:
            for data in content_list:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write("\n")

        print("保存成功")


    def run(self):
        # 构建url
        num = 0
        total = 50
        while num < total+18:
            url = self.start_url.format(num)
            # 发送请求，获取响应
            get_url = self.prase_url(url)
            # 提取数据
            content_list, total = self.get_content_list(get_url)
            # 保存
            self.save_data(content_list)
            # 发送下一个url
            num += 18

if __name__ == '__main__':
    douban = doubanSpider()
    douban.run()
