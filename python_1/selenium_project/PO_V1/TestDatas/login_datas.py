# _*_ coding:utf-8 _*_
# @Time    :2019/10/22 11:06
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :login_datas.py

from selenium_project.PO_V1.TestDatas.Comm_Datas import base_url

# 正常登录
success_data={"user":"18684720553","passwd":"python","check":"{}/Index/login.html".format(base_url)}

# 密码为空/用户名为空/用户名格式不正确
wrong_datas=[
    {"user":"18684720553","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"python","check":"请输入手机号"},
    {"user":"186847","passwd":"python","check":"请输入正确的手机号"},
    {"user":"1868472055311","passwd":"python","check":"请输入正确的手机号"}
]

# 用户名未注册/密码错误
fail_datas=[
    {"user":"18600000000","passwd":"python","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","passwd":"python111","check":"帐号或密码错误!"}
]


















