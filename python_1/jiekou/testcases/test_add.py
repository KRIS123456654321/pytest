# _*_ coding:utf-8 _*_
# @Time    :2019/6/24 9:59
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_add.py

# import unittest
# from jiekou.common.request_home_1 import HTTPRequest2 # 获取发起请求requests的模块
# from jiekou.common import testcase # 获取表格数据且写入表格数据的模块
# from jiekou.common import contants # 获取文件路径的模块
# from ddt import ddt,data
# from jiekou.common.config import config
# @ddt
# class AddTest(unittest.TestCase):
#     excel = testcase.DoExcel(contants.case_file, 'add')  # 打开Excel测试用例表格
#     cases = excel.get_cases()  # 获取Excel里面的测试用例数据
#     @classmethod
#     def setUpClass(cls): # 只执行一次，开始执行测试用例test_login前，调用一次
#         cls.http_request=HTTPRequest2()
#     @data(*cases)
#     def test_login(self,case): # 测试用例
#         case.data=eval(case.data) # 变成字典
#         # 需要先判断是否有这个key，再判断是否有这个value值，不能只判断是否有这个value值，
#         # 因为第二条测试用例中没有那个key，就无法获取那个key对应的那个值，所以报错
#         # 判断字典中是否含有mobilephone这个key
#         if case.data.__contains__('mobilephone') and case.data['mobilephone']=='normal_user':
#             # 获取配置文件中的值，赋值为表格中的mobile_phone
#             case.data['mobilephone']=config.get('data','normal_user')
#         if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
#             case.data['pwd'] = config.get('data', 'normal_pwd')
#         if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
#             case.data['memberId'] = config.get('data', 'loan_member_id')
#         print(case.data)
#         resp = self.http_request.request(case.method, case.url, case.data)  # 发起requests请求，得到响应结果
#         # 断言失败会抛出异常，这里可以用try...except...
#         print(resp.text)
#         try:
#             self.assertEqual(str(case.expected),resp.json()['code']) # 断言
#             self.excel.write_result(case.case_id+1,resp.text,'PASS') # 断言成功
#         except AssertionError as e:
#             self.excel.write_result(case.case_id+1,resp.text,'FAIL') # 断言失败
#             raise  e
#     @classmethod
#     def tearDownClass(cls):  # 只执行一次，执行完所有的测试用例test_login完成后，调用一次
#         cls.http_request.close()

# 开始引用正则表达式：
# 原因：加标接口的表格中有3个标识，在测试用例中就分3个if判断了3个标识，这种方式不好，因为如果有100个标识，不可能去写100个判断，这样的代码显然是不好的，
# 解决方式：使用正则表达式来进行判断，把那3个标识设为符合正则表达式的规范
import unittest
from jiekou.common.request_home_1 import HTTPRequest2 # 获取发起请求requests的模块
from jiekou.common import testcase # 获取表格数据且写入表格数据的模块
from jiekou.common import contants # 获取文件路径的模块
from ddt import ddt,data
from jiekou.common import context
@ddt
class AddTest(unittest.TestCase):
    excel = testcase.DoExcel(contants.case_file, 'add')  # 打开Excel测试用例表格
    cases = excel.get_cases()  # 获取Excel里面的测试用例数据
    @classmethod
    def setUpClass(cls): # 只执行一次，开始执行测试用例test_login前，调用一次
        cls.http_request=HTTPRequest2()
    @data(*cases)
    def test_login(self,case): # 测试用例
        # 在请求之前替换参数化标识的值
        case.data=context.replace(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)  # 发起requests请求，得到响应结果
        # 断言失败会抛出异常，这里可以用try...except...
        print(resp.text)
        try:
            self.assertEqual(str(case.expected),resp.json()['code']) # 断言
            self.excel.write_result(case.case_id+1,resp.text,'PASS') # 断言成功
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL') # 断言失败
            raise  e
    @classmethod
    def tearDownClass(cls):  # 只执行一次，执行完所有的测试用例test_login完成后，调用一次
        cls.http_request.close()
