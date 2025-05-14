import os
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver


print('使用前请先翻墙')
a = input('你是否已经翻墙,输入y or n')
if a == 'n':
    os._exit()
print('正在爬取图片，请稍等.......(全部爬取大约需要1-2分钟)')
print('注意查收当前文件夹下的美女图片这个文件夹')
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
urls = []
for a in range(1,25):
    urls.append(f'https://www.3gbizhi.com/meinv/mnxz/index_{a}.html')

#配置浏览器选项
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')


#启动浏览器
driver = webdriver.Chrome(options=options)


#解析网址
def lxml_the_url(urls):
    soups = []
    for url in urls:
        driver.get(url)#发送get请求
        html = driver.page_source  #得到html内容
        soup = BeautifulSoup(html,'lxml')
        soups.append(soup)
    return soups


#得到图片的url
def img_url(urls):
    soups = []
    soups = lxml_the_url(urls)
    img_urls = []
    for soup in soups:
        img_tags = soup.find_all('img')
        img_url = [
                    img.get('src') for img in img_tags 
                    if img.get('alt') and img.get('src') and 'loading-tupian.gif' not in img.get('src')
        ][:5]
        img_urls.extend(img_url)
    return img_urls


#下载图片
def download_img(img_urls):
    if not os.path.exists('美女图片'):        
        os.makedirs('美女图片')
    for i in range(1,121):
        with open(f'美女图片/{i}.jpg','wb') as f:
            img_content = requests.get(img_urls[i-1],headers=header)
            f.write(img_content.content)
            time.sleep(1)


if __name__ == '__main__':
    img_urls = []
    img_urls = img_url(urls)
    download_img(img_urls)
    print('成功爬取所有图片')
    driver.quit()
