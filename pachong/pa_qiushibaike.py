import requests
from lxml import etree


class Qiushibaike:
    def __init__(self):
        self.next_url = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

    def get_url_list(self):
        return [self.next_url.format(i) for i in range(2, 14)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self,html_url):
        html = etree.HTML(html_url)
        div_list = html.xpath("//div[@class='col1 old-style-col1']/div")
        content_list =[]
        for div in div_list:
            item = {}
            item['content'] = div.xpath(".//*[@class='content']/span/text()")
            # item['content'] = [i.sub('', '\n') for i in item['content']]
            item['content'] = [i.replace('\n', '') for i in item['content']]
            item['author_gender'] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            item['author_gender'] = item['author_gender'][0].split(" ")[-1].replace("Icon", "") if len(item["author_gender"]) > 0 else None
            item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None
            item["author_img"] = div.xpath(".//*[@class='author clearfix']//img/@src")
            item["author_img"] = item["author_img"][0] if len(item["author_img"]) > 0 else None
            content_list.append(item)
        return content_list

    def save_content(self,content):
        for i in content:
            print(i)


    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_url = self.parse_url(url)
            content_list = self.get_content_list(html_url)
            self.save_content(content_list)


if __name__ == '__main__':
    qiubai = Qiushibaike()
    qiubai.run()