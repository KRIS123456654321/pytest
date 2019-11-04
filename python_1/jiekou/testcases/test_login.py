# _*_ coding:utf-8 _*_
# @Time    :2019/6/20 16:57
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :unit.py

# 为什么要用unittest单元测试？
# 1.方便出具体的统计测试结果的测试报告。如几条通过，几条失败，失败原因是什么

# 测试用例原则：简单，好维护，不要有太多逻辑
# 原因：因为接口测试不通过时，首先是要排查自己的代码是否有问题，然后再看接口是否有问题，测试用例代码逻辑太复杂，
# 还得一个个debug排查，这样就太麻烦了，所以要以逻辑简单，好维护为准

# 测试用例如何分类写接口测试？
# 疑问：测试用例是单个放还是放在一个类里面？同一个接口的测试用例是否放在一个里面？
# 同一个接口的测试用例场景比较多时，是否分场景把类似的场景放在一个类里面？
# 结果：按分类标准来划分，找出规律把相似的放在一起，如果是相似的或者比较简单的话，就可以放在一个类里面执行所有的测试用例

# 断言失败会抛出异常，可以用try...except AssertionError as ...，具体使用可以参考下面的测试用例

import unittest
from jiekou.common.request_home_1 import HTTPRequest2
from jiekou.common import testcase
from jiekou.common import contants
from ddt import ddt,data

@ddt
class LoginTest(unittest.TestCase):
    excel = testcase.DoExcel(contants.case_file, 'login')  # 打开Excel测试用例表格
    cases = excel.get_cases()  # 获取Excel里面的测试用例数据
    def setUp(self): # 做前置工作的方法，自带的方法，运行测试用例时会自动执行，不需要调用，每次执行测试用例test_login前，都会调用一次，
        # 这里cases中有四条测试用例，所以会执行四次，即执行一次前置方法，再执行一次测试用例，再执行一次后置方法，然后依次循环四次
        self.http_request=HTTPRequest2()
    @data(*cases)
    def test_login(self,case): # 测试用例
        resp = self.http_request.request(case.method, case.url, case.data)  # 发起requests请求，得到响应结果
        # 断言失败会抛出异常，这里可以用try...except...
        try:
            self.assertEqual(case.expected,resp.text) # 断言
            self.excel.write_result(case.case_id+1,resp.text,'PASS') # 断言成功
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL') # 断言失败
            raise  e
    def tearDown(self):  # 做后置工作的方法，自带的方法，运行测试用例时会自动执行，不需要调用，每次执行测试用例test_login后，都会调用一次，
        # 这里cases中有四条测试用例，所以会执行四次，即执行一次前置方法，再执行一次测试用例，再执行一次后置方法，然后依次循环四次
        self.http_request.close()

# 为了解决执行四条测试用例，只调用一次前置方法，一次后置方法，即先调用前置方法，然后执行四条测试用例，再调用后置方法
# 把前置方法和后置方法变成类方法
@ddt
class LoginTest(unittest.TestCase):
    excel = testcase.DoExcel(contants.case_file, 'login')  # 打开Excel测试用例表格
    cases = excel.get_cases()  # 获取Excel里面的测试用例数据
    @classmethod
    def setUpClass(cls): # 做前置工作的方法，自带的方法，运行测试用例时会自动执行，不需要调用，第一次执行测试用例test_login前，会调用一次，
        # 这里cases中有四条测试用例，只会开始执行一次
        cls.http_request=HTTPRequest2()
    @data(*cases)
    def test_login(self,case): # 测试用例
        resp = self.http_request.request(case.method, case.url, case.data)  # 发起requests请求，得到响应结果
        # 断言失败会抛出异常，这里可以用try...except...
        try:
            self.assertEqual(case.expected,resp.text) # 断言
            self.excel.write_result(case.case_id+1,resp.text,'PASS') # 断言成功
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL') # 断言失败
            raise  e
    @classmethod
    def tearDownClass(cls):  # 做后置工作的方法，自带的方法，运行测试用例时会自动执行，不需要调用，所有测试用例test_login执行完后，会调用一次，
        # 这里cases中有四条测试用例，只会最后执行一次
        cls.http_request.close()































