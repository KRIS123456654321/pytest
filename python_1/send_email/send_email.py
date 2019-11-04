# _*_ coding:utf-8 _*_
# @Time    :2019/6/3 17:54
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :send_email.py

# 发送邮件：使用模块smtplib，相当于自定义客户端来发送邮件
# 发送邮件使用的协议：不是http，而是pop3 或 smtp

# 手工发送邮件：
# 1.选择发送邮件的服务商，如网易  QQ
# 2.登录
# 3.编写邮件
# 4.发送

# 发送邮件使用的协议：pop3 smtp
import smtplib
from configparser import ConfigParser
# 输入邮件服务商，这里以使用smtp协议的邮箱为例
# 初始化参数host：host表示SMTP服务器，不同的邮件发送服务商，都有不同的host名称，一般都是在域名前面加上smtp,如www.163.com的host为smtp.163.com
# 因为相当于自定义客户端来发送邮件，所以host可以在邮件地址中找到客户端输入的地址
# 初始化参数port：不同的邮件发送服务商，都有不同的端口号，但一般的邮件端口号默认都是25
server=smtplib.SMTP('smtp.163.com',25) # 初始化邮件服务商
# 登录
# 获取配置文件login.cfg中的账号name 密码pwd
cf=ConfigParser()
cf.read('login.cfg',encoding='gbk')
name=cf.get('login','name')
pwd=cf.get('login','passwd')
server.login(name,pwd)
# 发送邮件
# 发送内容的格式必须如下：From表示发送人，Subject表示邮件主题，再空一格，然后写内容
msg = '''\\
From: huahua
Subject: test

This is a test '''
server.sendmail(name,'S892336120@163.com',msg)
# 退出
server.quit()

# 运行中出现550,User has no permission'的解决办法：这里拿www.163.com（host：smtp.163.com）来举例
# 原因：当传入发送邮箱正确的用户名和密码时，总是收到到：550 User has no permission这样的错误，
# 其实我们用python发送邮件时相当于自定义客户端根据用户名和密码进行登录，然后使用SMTP服务发送邮件，但新注册的163邮件默认是不开启客户端授权验证的（对自定的邮箱大师客户端默认开启），
# 因此登录总是会被拒绝，验证没有权限
# 解决办法：进入163邮箱，进入设置-POP3/SMTP/IMAP-客户端授权密码，选择开启即可

# 为了防止忘记退出邮箱server.quit()，可以使用上下文管理器
# with smtplib.SMTP('smtp.163.com',25) as server:
#     cf = ConfigParser()
#     cf.read('login.cfg', encoding='gbk')
#     name = cf.get('login', 'name')
#     pwd = cf.get('login', 'passwd')
#     server.login(name, pwd)
#     msg = '''\\
#     From：huahua
#     Subject：test
#
#     This is a test'''
#     server.sendmail(name, 'S892336120@163.com', msg)



































