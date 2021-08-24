import requests
from bs4 import BeautifulSoup



# //*[@id="center_box"]/img
# response = requests.get('https://manhua.dmzj.com/rexuegaoxiao/5427.shtml#@page=2').text
# soup = BeautifulSoup(response, 'lxml')
#
# data_list = soup.find_all('img')
# print(data_list)
for x in range(1, 26):
    vol = str(x).rjust(2, '0')
    print(vol)
    for y in range(1, 193):
        page = str(y).rjust(2, '0')
        response = requests.get('//images.dmzj.com/r/\%E7\%83\%AD\%E8\%A1\%80\%E9\%AB\%98\%E6\%A0\%A1/VOL{}/{}.jpg', format(vol, page))





