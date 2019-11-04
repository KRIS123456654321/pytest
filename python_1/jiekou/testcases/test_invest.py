# _*_ coding:utf-8 _*_
# @Time    :2019/6/27 11:13
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_invest.py

# 如何解决接口之间的依赖，接口之间的数据传递?
# 有的接口的测试用例，需要依赖于别的接口产生的数据
# 有的接口的测试用例，需要先登录才能操作
# 通过获取数据库中的值，利用类的反射，存放为类的属性值，然后要用的时候，取其值来作为测试用例中的参数数据
# 如：一个测试用例中的参数，需要使用另一个测试用例执行后，在数据库中自动创建的某个id，这时就需要获取数据库中的数据来作为参数数据
# 例如：投资接口的测试用例

# 要从数据库中执行sql获取数据，可以把sql也放在表格中，方便维护
# 执行sql原因一：接口之间的数据传递，从数据库中获取值作为测试用例的参数
# 1.把要执行的sql放在表格中，如果有多条，可以放在字典中存放
# 2.获取表格中sql的数据
# 3.执行测试用例时，在发起请求前，判断该条测试用例是否要执行sql，有sql则连接数据库获取sql值，并取需要的字段值
# 4.可以把获取的字段值通过类的反射存放在一个类中
# 5.在获取接口的参数值的过程中，取存放的类的属性值

# # 执行sql原因二：数据库校验，通过执行测试用例前后获取数据库的值来校验数据库
# 在请求前通过数据库获取某个字段值，在请求后通过数据库获取某个字段的值，可以用来判断发起请求后，
# 数据库的数据操作是否正确，该条测试用例测试是否通过
# 如：进行充值，充值前获取余额，充值后获取余额，判断充值前的余额+充值的余额是否等于充值后的余额
# 1.把要执行的sql放在表格中，如果有多条，可以放在字典中存放
# 2.获取表格中sql的数据
# 3.执行测试用例时，在发起请求前，判断该条测试用例是否要执行sql，有sql则连接数据库获取sql值，并取需要的字段值
# 4.可以把获取的字段值通过类的反射存放在一个类中
# 5.在获取接口的参数值的过程中，取存放的类的属性值
# 6.在请求成功后，可以再次判断是否要执行sql，然后进行一系列操作（具体根据接口测试场景来写逻辑）
# 7.第二次执行数据库的时候，要强制查询最新的数据库，可以在连接数据库取值的那个do_mysql模块中的类中加commit

# 从数据库返回的数据为字典：
# 从数据库返回的数据是个元组，不好取字段值且有的时候要取多个字段值而不止一个两个，
# 所以可以让从数据库返回的数据是个字典，就比较好取了，具体怎么做可以看连接数据库取值的那个do_mysql模块中的类

import unittest
from jiekou.common.request_home_1 import HTTPRequest2 # 获取发起请求requests的模块
from jiekou.common import testcase # 获取表格数据且写入表格数据的模块
from jiekou.common import contants # 获取文件路径的模块
from ddt import ddt,data
from jiekou.common import context # 获取使用正则表达式替换参数化数据的模块
from jiekou.common import do_mysql # 获取数据库中的数据模块
@ddt
class AddTest(unittest.TestCase):
    excel = testcase.DoExcel(contants.case_file, 'invest')  # 打开Excel测试用例表格
    cases = excel.get_cases()  # 获取Excel里面的测试用例数据
    @classmethod
    def setUpClass(cls): # 只执行一次，开始执行测试用例test_login前，调用一次
        cls.http_request=HTTPRequest2()
        cls.mysql=do_mysql.DoMysql()
    @data(*cases)
    def test_invest(self,case): # 测试用例
        # 在请求之前替换参数化标识的值
        case.data=context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)  # 发起requests请求，得到响应结果
        # 断言失败会抛出异常，这里可以用try...except...
        print(resp.text)
        try:
            self.assertEqual(str(case.expected),resp.json()['code']) # 断言
            self.excel.write_result(case.case_id+1,resp.text,'PASS') # 断言成功
            # 判断加标成功后，查询数据库，取到loan_id，并放在context模块中的类Context里面，作为第三个接口中的loan_id参数值
            if resp.json()['msg'] == '加标成功':
                sql='select * from future.loan where memberid = 89246 order by id limit 1'
                loan_id=self.mysql.fetch_one(sql)[0]
                print('标的id：',loan_id)
                # 保存到类属性里面
                setattr(context.Context,'loan_id',str(loan_id)) # loan_id转换成字符串，因为接口参数传的是字符串类型
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL') # 断言失败
            raise  e
    @classmethod
    def tearDownClass(cls):  # 只执行一次，执行完所有的测试用例test_login完成后，调用一次
        cls.http_request.close()

