# _*_ coding:utf-8 _*_
# @Time    :2019/7/28 18:19
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :study_mock.py

# 定义Mock类：
# class Mock(spec=None,side_effect=None,return_value=DEFAULT,name=None)
# secp参数：一般用在单元测试，模拟一个不存在的对象

# mock模拟方法调用的时候，不用加圆括号,模拟的方法就是开发的接口
# mock模拟接口的返回做单元测试，任何语言写的接口都可以使用mock来完成
# mock模拟java的对象，则要使用mockito或者Jmock等相对应的框架来完成

# mock的使用如下：
# import requests
# from unittest import mock
# # 调用接口的方法
# def request_baidu():
#     resp=requests.get('http://www.baidu.com')
#     print(resp.text)
#     print(resp.status_code)
#     return resp.status_code
# # 使用mock模拟request_baidu方法，不关心request_baidu方法中的接口执行过程，只关心传入的参数、返回的结果
# request_baidu=mock.Mock(return_value=500)
# # 调用request_baidu方法，会直接执行mock.Mock(return_value=500)，不会去执行request_baidu方法，因为已经被mock模拟了
# print(request_baidu())

# 支付测试场景：
# 1.支付成功
# 2.支付失败
# 3.超时，成功
# 4.超时，失败
# 5.超时，超时
import unittest
from unittest import mock
from study_mock import payment
class PaymentTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_success(self):
        '''支付成功'''
        pay=payment.Payment()
        # 模拟方法调用的时候，不用加圆括号,模拟的方法就是开发的接口
        # 模拟接口的返回，任何语言写的接口都可以使用mock来完成，
        # 模拟java的对象，则要使用mockito或者Jmock来完成
        # 使用mock模拟接口返回
        pay.requestOutofSystem=mock.Mock(return_value=200) # mock模拟requestOutofSystem方法中调用的接口返回
        resp=pay.doPay(user_id=1,card_num='439019098',amount=200)
        self.assertEqual('success',resp)
        # 断言接口的行为
        # 是否只被调用过一次
        pay.requestOutofSystem.assert_called_once()
        # 是否只被调用过一次,且传参要一致
        pay.requestOutofSystem.assert_called_once_with('439019098',200)
    def test_fail(self):
        '''支付失败'''
        pay=payment.Payment()
        pay.requestOutofSystem=mock.Mock(return_value=500)
        resp=pay.doPay(user_id=2,card_num='439019908',amount=20000)
        self.assertEqual('fail',resp)
    def test_timeout_success(self):
        '''超时后成功'''
        pay=payment.Payment()
        # side_effect是可迭代可遍历的，进行循环,第一次模拟返回超时，再调用一次时，模拟返回成功
        pay.requestOutofSystem=mock.Mock(side_effect=[TimeoutError,200])
        # 还没被调用，返回的是Fail
        print('是否被调用',pay.requestOutofSystem.called)
        resp=pay.doPay(user_id=2,card_num='439019908',amount=20000)
        # 查看mock对象的属性
        # 已经被调用，返回的是True
        print('是否被调用',pay.requestOutofSystem.called)
        print('调用次数', pay.requestOutofSystem.call_count)
        print('调用参数', pay.requestOutofSystem.call_args)
        self.assertEqual('success',resp) # 最后是成功的
    def test_timeout_fail(self):
        '''超时后失败'''
        pay =payment.Payment()
        # side_effect是可迭代可遍历的，进行循环,第一次模拟返回超时，再调用一次时，模拟返回失败
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = pay.doPay(user_id=2, card_num='439019908', amount=20000)
        self.assertEqual('fail', resp) # 最后是失败的
    def test_timeout_timeout(self):
        '''超时后超时'''
        try:
            pay = payment.Payment()
            # 每次模拟调用requestOutofSystem方法，返回都是超时
            pay.requestOutofSystem = mock.Mock(side_effect=TimeoutError)
            resp = pay.doPay(user_id=2, card_num='439019908', amount=20000)
        # 捕获第二次模拟返回的异常
        except TimeoutError as e:
            self.assertTrue(e) # 最后是超时的
    def tearDown(self):
        pass




























