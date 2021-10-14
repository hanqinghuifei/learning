import requests
from lxml import etree

class gongzuo:
    def __init__(self):
        self.url = "https://beta.heartbeatgo.com/index.php?route=product/search&stock=0&search=%20&page=&page={}&category=0&sort=1"

    def run(self):
        kong_list = []
        for i in range(1, 58):
            url_list = self.parse_url(self.url.format(i))
            div_list = self.etree_url(url_list)
            kong_list.extend(div_list)
        print(len(kong_list))
        self.etree_content_url(kong_list)

    def parse_url(self, url):
        response = requests.get(url)
        return response.content.decode()

    def etree_url(self, url_lis):
        html = etree.HTML(url_lis)
        div_list = html.xpath("//div[@class='new_list']/ul/li/a/@href")
        return div_list

    def etree_content_url(self, content_url):
        for url in content_url:
            url_1 = self.parse_url(url)
            html = etree.HTML(url_1)
            src_list = html.xpath("//img[contains(@src,'coupon.png')]/@src")
            src_list = src_list[0] if len(src_list) > 0 else ''
            if src_list != '':
                print(url)
            else:
                pass

if __name__ == '__main__':
    gz = gongzuo()
    gz.run()
