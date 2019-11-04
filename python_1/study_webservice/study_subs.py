# _*_ coding:utf-8 _*_
# @Time    :2019/7/28 17:48
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :study_subs.py

# 接口调用实际就是客户端去请求，服务端响应
# import suds
# from suds.client import Client
# # 获取短信验证码
# # 建立一个客户端
# url='http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
# client=Client(url)
# print(client)
# data={"client_ip":"127.0.0.1","tmpl_id":1,"mobile":"15878787878"}
# try:
#     resp=client.service.sendMCode(data) # sendMCode方法要与client打印出来中的方法名一致
#     print(resp) # {retCode = "0",retInfo = "ok"}
#     print(type(resp)) # class类型
#     print("返回码",resp.retCode) # 返回的返回码
#     print("返回信息",resp.retInfo)  # 返回的信息
# except suds.WebFault as e: # 捕获异常
#     print(e.fault.faultstring) # 要拿到“手机号码错误”的信息
#
# # 注册
# url='http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
# data={"verify_code":692653,"user_id":"霹雳娇娃","channel_id":1,"pwd":"123456","mobile":"15878787878","ip":"127.0.0.1"}
# client=Client(url)
# print(client)
# try:
#     resp=client.service.userRegister(data) # sendMCode方法要与client打印出来中的方法名一致
#     print("返回码",resp.retCode) # 返回的返回码
#     print("返回信息",resp.retInfo)  # 返回的信息
# except suds.WebFault as e: # 捕获异常
#     print(e.fault.faultstring) # 要拿到“手机号码错误”的信息

import suds
from suds.client import Client
def ws_request(url,data,method):
    client = Client(url)
    try:
        # 不能直接使用client.service.method(data)，method方法会报错，所以可以用eval函数来把它放在字符串中执行
        resp = eval("client.service.{0}({1})".format(method,data))  # sendMCode方法要与client打印出来中的方法名一致
        msg = resp.retInfo
        print("返回码", resp.retCode)  # 返回的返回码
        print("返回信息", resp.retInfo)  # 返回的信息
    except suds.WebFault as e:  # 捕获异常
        print(e.fault.faultstring)  # 要拿到“手机号码错误”的信息
        msg=e.fault.faultstring
    return msg

url="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
data={"uid":100010710,"true_name":"张三","cre_id":"43041219900729002Z"}
resp=ws_request(url,data,"verifyUserAuth")
print(resp)




















