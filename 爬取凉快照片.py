from bs4 import BeautifulSoup
import requests
import sys
import os
import time


img_url = []
url = 'https://ent.cri.cn/xiaozhihezuo/20170220/9e975820-8fa9-e232-f9b4-a46872b8bbfb.html'  #妹子的网址
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


def get_img_url():
    response = requests.get(url,headers=header)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,'lxml')
    imgs = soup.find_all('img')
    for img in imgs[1:]:
        img_url.append(img.get('src'))


def download_img():
    if not os.path.exists('girl_picture'):
        os.makedirs('girl_picture')
    for i in range(1,11):
        with open(f'girl_picture/{i}.jpg','wb') as file:
            img_content = requests.get(img_url[i-1],headers=header)
            file.write(img_content.content)
            time.sleep(1)

if __name__== '__main__':
    get_img_url()
    download_img()
    print('success')


