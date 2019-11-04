# _*_ coding:utf-8 _*_
# @Time    :2019/6/17 15:18
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :home_1.py

# 写两个类，一个要传cookie，一个不要传cookie，可以完成不同的HTTP请求，并返回响应结果
import requests
from jiekou.common.config import config # 获取配置文件中的地址模块中的对象
# 要传cookie的HTTPRequest类，使用不同的session会话，会自动关闭会话，不需要手动关闭会话
class HTTPRequest:
    '''
    使用这类的request方法去完成不同的HTTP请求，并返回响应结果
    '''
    def request(self,method,url,data=None,json=None,cookies=None):
        method=method.upper() # 强制转大写
        # 参数要传字典形式
        # 判断传的参数是否为字符串，如果是则转换成字典
        if type(data) == str:
            data=eval(data)
        # 拼接url把配置文件中获取的地址与表格中的地址进行拼接
        url = config.get('api', 'pre_url') + url
        if method =='GET':
            resp = requests.get(url,params=data,cookies=cookies)
        elif method =='POST':
            if json:
                resp = requests.post(url,json=json,cookies=cookies)
            else:
                resp = requests.post(url,data=data,cookies=cookies)
        else:
            print('UN-support method')
        return resp
# 不要传cookie的HTTPRequest2类，使用相同的session会话，不会自动关闭会话，需要手动关闭会话
class HTTPRequest2:
    def __init__(self):
        # 打开session会话
        self.session=requests.sessions.session()
    def request(self,method,url,data=None,json=None):
        method = method.upper()  # 强制转大写
        # 参数要传字典形式
        # 判断传的参数是否为字符串，如果是则转换成字典
        if type(data) == str:
            data=eval(data)
        # 拼接url把配置文件中获取的地址与表格中的地址进行拼接
        url = config.get('api', 'pre_url') + url
        if method=='GET':
            resp =self.session.request(method=method,url=url,params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            print('UN-support method')
        return resp
    def close(self):
        # 关闭会话
        # 不能在上面的request方法中调用关闭方法，因为这里登录和充值接口调用的是同一个session，如果登录完成就关闭了，那么在充值的时候就不能自动使用登录返回的cookie了，所以要在所有接口都在这个会话中完成后，再关闭
        # 如果不关闭会话的话，当使用这个会话测的接口多时，资源没有得到释放，会占内存
        self.session.close()

if __name__ == '__main__':
    # 使用要传cookie的HTTPRequest类
    http_request=HTTPRequest()
    # 调用登录接口
    url = '/member/login'
    params = {
        'mobilephone': '15810447878',
        'pwd': '123456'
    }
    resp=http_request.request('POST',url,data=params)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)
    # 调用充值接口
    url = '/member/recharge'
    params = {
        'mobilephone': '15810447878',
        'amount': '1000'
    }
    resp=http_request.request('POST',url,data=params,cookies=resp.cookies)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)

    # 使用不要传cookie的HTTPRequest2类
    http_request2=HTTPRequest2()
    # 调用登录接口
    url = '/member/login'
    params = {
        'mobilephone': '15810447878',
        'pwd': '123456'
    }
    resp2=http_request2.request('POST',url,data=params)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)
    # 调用充值接口
    url = '/member/recharge'
    params = {
        'mobilephone': '15810447878',
        'amount': '1000'
    }
    resp2=http_request2.request('POST',url,data=params)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)
    http_request2.close()

























