# _*_ coding:utf-8 _*_
# @Time    :2019/5/26 16:18
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :unit_test_01.py

# 写测试用例:用case模块中的TestCase类
import unittest
from unit_test.math_method import MathMethod
# 继承case模块中的TestCase类，使用TestCase类中的方法，不要覆盖TestCase类中的方法，这样才能使用TestCase类中的方法了
class TestMathMethod(unittest.TestCase): # 测试类
    # TestCase类中没有测试用例方法，所以要自己加
    # 写测试用例的方法：方法名一定要用test开头,
    # 否则运行时，unittest框架无法识别这个是测试用例方法，也就不会把这个当做用例来执行，
    # 只是正常当做方法来运行而已，不会算在测试用例里面
    # 只写测试用例，然后直接右键运行，这种情况下：方法中不能传参，因为运行时是直接右键运行的，不能通过写调用方法的代码来调用，所以没法通过调用方法来传参
    def test_add_two_zero(self): # 第二个执行这个方法
        expected=0 # 期望值
        res=MathMethod().add(0,0) # 实际值
        # 断言
        self.assertEqual(expected,res)
    def test_add_positive_negative(self): # 第一个执行这个方法
        expected=-2 # 期望值
        res=MathMethod().add(1,-3) # 实际值
        # 断言
        self.assertEqual(expected,res)

class TestSub(unittest.TestCase): # 测试类
    def test_001(self):
        expected=0 # 期望值
        res=MathMethod().sub(0,0) # 实际值
        # 断言
        self.assertEqual(expected,res)
    def test_002(self):
        expected=-2 # 期望值
        res=MathMethod().sub(1,-3) # 实际值
        # 断言
        self.assertEqual(expected,res)

# 直接右键运行测试用例：
# 1.只写测试用例，然后直接右键运行，这种情况下：方法中不能传参，因为运行时是直接右键运行的，不能通过写调用方法的代码来调用，所以没法通过调用方法来传参
# 2.鼠标放在类外来运行：右键-运行显示为Run 'unittests in unit_test_case.py',会执行所有类中的所有方法名为test开头的测试用例
# 3.鼠标放在类上或类中但在方法外来运行：右键-运行显示为Run 'unittests for unit_test_case.TestMathMethod',会执行鼠标所在类中的所有方法名为test开头的测试用例
# 4.鼠标放在方法内或方法上来运行：右键-运行显示为Run 'unittests for unit_test_case.TestMathMethod.test_add_two_zero.',会执行鼠标所在方法名为test开头的测试用例，
# 如果该方法不是test开头，则不会当做测试用例来执行，而是当普通的执行方法，且右键运行的显示也是不同的

# 测试用例的方法和普通类方法的区别：
# 1.测试用例的方法是以test开头的，普通类方法则不需要以test开头
# 2.测试用例的方法右键运行显示为Run 'unittests + ...'，普通类方法右键运行显示为Run ' ...'，
# 3.加了test开头，unittest框架才会识别这个是测试用例方法，当做测试用例来执行
# 4.不加test开头，unittest框架不会把这个当做测试用例来执行，只是正常当做方法来运行而已，不会算在测试用例里面

# 测试用例方法的执行顺序：根据SACII编码来确认执行顺序的，A的SACII编码为65，a的SACII编码为97，B的SACII编码为66，b的SACII编码为98,依次类推
# 可以在方法中通过打印信息来看先执行的那个方法
# 如：test_add_two_zero方法 和 test_add_positive_negative方法，会有优先执行第二个test_add_positive_negative方法
# 原因：test_add_two_zero和test_add_positive_negative中的test_add_一样可以不进行比较，然后比较test_add_后面的第一个字母，
# p的SACII编码在t的SACII编码的前面，所以先执行test_add_positive_negative

# 要想按照从上到下的方法顺序来执行，可以把方法名改为test_001和test_002












