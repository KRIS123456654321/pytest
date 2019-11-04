# _*_ coding:utf-8 _*_
# @Time    :2019/5/27 17:07
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :unit_date.py

# 测试用例数据的复用性：失败的方案如下

# 导入unittest模块：
import unittest
from unit_test.math_method import MathMethod

# 写测试用例：
class TestMathMethod(unittest.TestCase):
    # 只写测试用例，然后直接右键运行，这种情况下：方法中不能传参，因为运行时是直接右键运行的，不能通过写调用方法的代码来调用，所以没法通过调用方法来传参
    # 原来的方式：
    # def test_add_two_zero(self):
    #     expected=0 # 期望值
    #     res=MathMethod().add(0,0) # 实际值
    #     # 断言
    #     self.assertEqual(expected,res)
    # def test_add_positive_negative(self): # 第一个执行这个方法
    #     expected=-2 # 期望值
    #     res=MathMethod().add(1,-3) # 实际值
    #     # 断言
    #     self.assertEqual(expected,res)
    # 解决方案一：失败
    # def test_add_two_zero(self,expected,a,b):
    #     res=MathMethod().add(a,b) # 实际值
    #     # 断言
    #     self.assertEqual(expected,res)
    # def test_add_positive_negative(self,expected,a,b): # 第一个执行这个方法
    #     res=MathMethod().add(a,b) # 实际值
    #     # 断言
    #     self.assertEqual(expected,res)
    # 解决方案二：成功
    def test_add_two_zero(self):
        expected=self.expected # 期望值
        res=MathMethod().add(self.a,self.b) # 实际值
        # 断言
        self.assertEqual(expected,res)
    def test_add_positive_negative(self): # 第一个执行这个方法
         expected=self.expected # 期望值
         res=MathMethod().add(self.a,self.b) # 实际值
         # 断言
         self.assertEqual(expected,res)

# 加载测试用例
suite = unittest.TestSuite()
# 原来的方式：
# suite.addTest(TestMathMethod('test_add_two_zero'))
# suite.addTest(TestMathMethod('test_add_positive_negative'))
# 解决方案二：成功，但是要改源码，这种方案不好
# suite.addTest(TestMathMethod('test_add_two_zero',0,0,0))
# suite.addTest(TestMathMethod('test_add_positive_negative',-2,1,-3))
# 解决方案二：再延伸，但是要改源码，这种方案不好
# test_date=[[0,0,0],[-2,1,-3]]
# for item in test_date:
#     suite.addTest(TestMathMethod('test_add_two_zero',item[0],item[1],item[2]))
# 解决方案二：再延伸，但是要改源码，这种方案不好
test_date = [[0, 0, 0], [-2, 1, -3]] # 把数据放到Excel表格中去读取
for item in test_date:
    suite.addTest(TestMathMethod('test_add_two_zero', item[0], item[1], item[2]))

# 运行测试用例并产生测试报告
with open('test_1.text','w') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=0)
    runner.run(suite)

# 测试用例数据的复用性：失败的方案如下
# 原因：当有很多条测试用例时，如果每一条都是一个一个的写测试用例并加载并执行，会很浪费时间，
# 那么这时候就可以把那些测试用例中相似的测试用例不同的变量进行参数化：
# 解决方案一：在测试用例方法中传参
# 在每个测试用例方法中，把不同的值的变量进行参数化，作为方法的参数来传递
# 结果：失败，因为unittest框架不能通过写调用方法的代码来调用测试用例方法，所以无法传参，而是通过实例化对象来调用，所以可以在实例化对象的初始化方法中传参
# 解决方案二：在TestCase源码中的初始化方法中通过传参加入对象属性
# 在一个一个加载测试用例方法时，把不同的值的变量进行参数化，
# 传递给测试用例类TestMathMethod的父级类TestCase的初始化方法中作为参数，
# 要修改测试用例类TestMathMethod的父级类TestCase的初始化方法，在这个方法中，加入要传递的参数，并初始化为对象的属性，
# 然后在测试用例方法中把变量改为对象的属性来接收初始化时创建的对象属性
# 再延伸：
# 在解决方案二的基础上，当用不同的数据去调用一个测试用例方法多次时，
# 要写多行代码去调用，也很麻烦，所以可以把数据放在列表中，循环去读取
# 再延伸：
# 这时可以考虑把列表中的数据方法Excel表格中，通过读物Excel表格中的数据来循环去读取
# 结果：成功，但是要改源码，这种方案不好，而且如果有多个参数，就得加多个，且每次都要改，而且如果其他地方要用这个方法，就不能用了