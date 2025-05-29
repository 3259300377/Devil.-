import os
import requests
import tkinter as tk
import glob
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time


'''下载图片'''
def download_img():
    i = 0
    for name in hero_name:  #遍历每个英雄
        os.makedirs('./王者荣耀/'+name,exist_ok=True)  #创建每个英雄的文件夹
        for j in range(1,11):  #遍历每个皮肤
            hero_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_id[i]) + '/' + str(
                hero_id[i]) + '-bigskin-' + str(j) + '.jpg'
            hero_img = requests.get(hero_url)  #发起该皮肤的下载请求
            if hero_img.status_code==200:  #确保没有无效下载
                with open('./王者荣耀/'+name+'/'+str(j)+'.jpg','wb') as f:  #创建文件下载该皮肤
                    f.write(hero_img.content)
        i+=1


print('即将下载王者荣耀所有皮肤的图片\n大概需要几分钟,请稍等')
print('注意查收当前文件夹下的王者荣耀这个文件夹，里面存放这所有皮肤')
url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)
herolist_json = herolist.json()  #获取json格式的响应
hero_name = list(map(lambda x:x['cname'],herolist_json))  #存放所有的英雄名
hero_id = list(map(lambda x:x['ename'],herolist_json))   #存放英雄对应的id
download_img()
print('下载完成，即将进入抽卡程序')
time.sleep(2)




'''抽卡程序'''
def random_show_pic():  #随机展示图片
   path =  glob.glob('./王者荣耀/*/*.jpg')  #找到所有英雄图片的路径，并返回一个列表
   num = random.randint(0,len(path)-1)  #生成一个随机数
   img = Image.open(path[num])  #打开相应图片
   img.thumbnail((1600,1600))  #缩放图片到1600x1600
   img_tk = ImageTk.PhotoImage(img)  #转换为tkinter可以显示的形式
   lbl_img.config(image=img_tk)  #在标签中显示图片
   lbl_img.image=img_tk   #保持显示


top = tk.Tk()
top.title('随机抽卡小程序')
top.geometry('2560x1600')
btn = tk.Button(top,text='随机抽取',command=random_show_pic)
btn.pack()
lbl_img = tk.Label(top)  #创建一个图片显示标签
lbl_img.pack()
top.mainloop()


