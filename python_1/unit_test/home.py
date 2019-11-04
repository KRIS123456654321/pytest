# _*_ coding:utf-8 _*_
# @Time    :2019/5/29 16:44
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :homeWork.py

# 作业：通过请求类，写4条用例，要求利用unittest进行单元测试，并且用3种加载方法去加载测试用例并执行，
# 4条用例中有2个正常用例2个异常用例

# 作业：测试数据结合ddt来使用，出一份测试报告

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
        resp = requests.get(login_url,params=params).status_code
        print('响应结果：{}'.format(resp))
        self.assertEqual(expected,200)


# suite=unittest.TestSuite()
# suite.addTest(getClass("test_True_1"))

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(getClass))

# with open('home_test.text','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)
#     runner.run(suite)

import HTMLTestRunnerNew
with open('home_test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='20190530测试报告',
                                            description='这是登录功能验证的测试报告',
                                            tester='郭郭')
    runner.run(suite)

if __name__ == '__main__':
    unittest.main()


