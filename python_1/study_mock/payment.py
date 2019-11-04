# _*_ coding:utf-8 _*_
# @Time    :2019/7/28 18:40
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :payment.py

import requests
class Payment:
    def requestOutofSystem(self,card_num,amount):
        '''请求第三方支付接口'''
        '''如果在测试用例中使用了mock模拟这个接口的返回，那么就不会执行这个接口的代码'''
        print('调用第三方支付接口*****')
        url='http://third.payment.pay/' # 第三方接口请求地址
        data={"card_num":card_num,"amount":amount} # 请求参数
        response=requests.post(url,data=data)
        print(response)
        return response.status_code # 返回状态码
    def doPay(self,user_id,card_num,amount):
        '''支付:user_id 用户ID card_num 卡号 amount 支付金额'''
        try:
            # 调用第三方支付接口请求进行真实扣款
            resp=self.requestOutofSystem(card_num,amount)
            print('调用第三方支付接口返回结果：',resp)
        except TimeoutError:
            # 如果超时就重新调用一次
            print('重试一次')
            resp=self.requestOutofSystem(card_num,amount)
        if resp==200:
            print("{0}支付{1}成功！！！进行扣款并记录支付记录".format(user_id,amount))
            return 'success'
        elif resp==500:
            print("{0}支付{1}失败！！！进行扣款并记录支付记录".format(user_id,amount))
            return 'fail'