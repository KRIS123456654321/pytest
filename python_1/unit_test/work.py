# _*_ coding:utf-8 _*_
# @Time    :2019/5/29 17:25
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :work.py

import unittest
import requests
from ddt import ddt,data,unpack
login_url='http://vip.test.qiaofangyun.com/login.jsp?companyUuid=largecustomer_test_companyUuidfortest'
param=({'login_url':login_url,'params':{'deptId':'20778','empUuid':'efbaca1f-7326-4102-8eab-2ed0f572c6d9'}},
       {'login_url':login_url,'params':{'deptId':'20779','empUuid':'07ced1bc-17b8-4f2f-abd3-4ca584a33a80'}},
       {'login_url':login_url,'params':{'deptId':'20778','empUuid':'efbaca1f-7326-4102-8eab-2ed0f572c6d1'}},
       {'login_url':login_url,'params':{'deptId':'20779','empUuid':'07ced1bc-17b8-4f2f-abd3-4ca584a33a81'}})
@ddt
class getClass(unittest.TestCase):
    @data(*param)
    @unpack
    def test_True_1(self,login_url,params):
        expected=200
        resp = requests.get(login_url, params=params).status_code
        print('响应结果：{}'.format(resp))
        self.assertEqual(expected,resp)

suite=unittest.TestSuite()
suite.addTest(getClass('test_True_1'))
with open('home_test.text','w') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=0)
    runner.run(suite)