# _*_ coding:utf-8 _*_
# @Time    :2019/6/14 15:29
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :home_sendEmail.py

import ssl
from smtplib import  SMTP,SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

email_servers={
    '163.com':{'smtp':{'host':'smtp.163.com','port':25,'ssl_port':465}},
    'qq.com':{}
}
context=ssl.create_default_context()

def parse_mail(mailname):
    server_name=mailname.split('@')
    # 判断邮件服务商的输入是否符合要求
    if len(server_name)==1:
        raise TypeError('email format error')
    # 获取邮件服务商的后面内容，如163.com,防止出现输入错误，如12@1212@163.com
    server_name=server_name[-1]
    # 判断邮件服务商是否在可以登录的邮件服务商的范围内
    if server_name not in list(email_servers.keys()):
        raise NameError('No this email server')
    server=email_servers.get(server_name,'')
    return server

class MyMail():
    # 初始化账号和密码，并登录服务商
    def __init__(self,mailname,pwd,ssl=True):
        self.mailname=mailname
        server=parse_mail(mailname).get('smtp','')
        if ssl==True:
            # SMTP_SSL 端口号不为25，如465，可以用SMTP_SSL
            self.server=SMTP_SSL(server.get('host'),server.get('ssl_port'),context=context)
        else:
            # SMTP
            self.server = SMTP(server.get('host'), server.get('port'))
        self.server.login(mailname,pwd)

    # 获取邮件正文内容
    def mail_msg(self,msg,type='html',subject=''):
        msg=MIMEText(msg,type)
        msg['Subject']=subject
        return msg

    # 发送邮件
    def send_mail(self,to,msg,files=None,type='plain',subject=''):
        total=MIMEMultipart()
        total['Subject']=subject
        body=self.mail_mag(msg,type=type,subject=subject)
        total.attach(body)
        # 判断附件是否为空None，是否为空列表[]
        if files and isinstance(files,list):
            # 可能上传多个附件，进行遍历
            for filename in files:
                file=MIMEApplication(open(filename,'rb').read())
                file.add_header('Content-Disposition','attachment',filename=filename)
                total.attach(file)
        return self.server.sendmail(self.mailname,to,total.as_string())

if __name__ == '__main__':
    msg='''
    测试为空，
    原因不多讲，
    你看着办吧
    '''
    mail=MyMail('892336120@qq.com','K13579',ssl=False)
    mail.send_mail('968569874@qq.com',msg,['测试.txt','demo.txt'],subject='给你小心心')


































