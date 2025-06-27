from smtplib import SMTP_SSL  #用于建立ssl加密的smtp协议连接
from email.header import Header
from email.mime.text import MIMEText  


def main():
    sender = '3259300377@qq.com'  #发送者
    passwd = 'yrwwnyqaoajwchdh'   #口令
    receiver = '1694399840@qq.com'  #接收者
    message = MIMEText('快叫爹','plain','utf-8')  #生成正文
    message['From'] = '3259300377@qq.com'
    message['To'] = '1694399840@qq.com'
    message['Subject'] = Header('你峰哥牛不牛逼','utf-8')  #生成标题
    smtper = SMTP_SSL('smtp.qq.com',465)  #与qq邮箱建立smtp连接
    smtper.login(sender,passwd)   #登录
    smtper.sendmail(sender,receiver,message.as_string())  #发送邮箱
    print('发送成功')


for i in range(1,7):
    main()