import requests
from retrying import retry

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

@retry(stop_max_atempt_number=3)
def _parse_url(url, method, data, proxies):
    print('1')


    if method =="POST":
        response = requests.post(url, data=data, headers=headers, proxies=proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies)

    assert response.status_code == 200

    return response.content.decode()



def prase_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)

    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = 'www.baidu.com'
    print(prase_url(url))
