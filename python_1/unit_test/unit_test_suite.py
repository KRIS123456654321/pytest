# _*_ coding:utf-8 _*_
# @Time    :2019/5/26 16:27
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :unit_test_suite.py

# 加载测试用例/存储用例的容器：用suite模块中的TestSuite类 或者 用loader模块中的TestLoader类

from unit_test.unit_test_case import * # 导入要加载的测试用例
# import unittest # 这里可以不用导入unittest模块，因为上面导入的写测试用例模块中已经导入过了

# 使用suite模块中的TestSuite类，一个一个的添加到加载测试用例的容器中
# 存储用例的容器suite：创建TestSuite类对象，即实例化TestSuite类
suite=unittest.TestSuite() # 前面要加unittest，是因为这个类是unittest模块中的，而前面的导入只导入了unittest模块，所有要使用这个类，就要加上unittest模块

# 第一种方式：通过一个一个写测试用例的模块中的具体方法来加载测试用例，执行加载的具体测试用例方法
# 添加你要执行的测试用例类中的方法到加载测试用例的容器中：
# 调用TestSuite类中的addTest方法来添加测试用例到suit这个套件里面，测试用例是测试用例类的实例，
# 要加载哪个测试用例就添加哪个测试用例类对象作为addTest方法中的参数,
# 且测试用例类的实例中要加入你要执行的测试用例中的方法名来作为参数
suite.addTest(TestMathMethod('test_add_two_zero')) # addTest是TestSuite类中的方法，TestMathMethod是测试用例中的类
suite.addTest(TestMathMethod('test_add_positive_negative')) # 可以单独添加多个测试用例到加载测试用例的容器中
suite.addTest(TestSub('test_001'))

# 第二种方式：通过加载整个写测试用例的模块来加载测试用例，执行加载的写测试用例的模块中的所有类名中的所有测试用例方法
# 通过使用loader模块中的TestLoader类来创建一个加载器，
# 这个加载器可以通过写测试用例的模块来加载测试用例的模块中的所有测试用例方法，
# 然后再把这个加载器放入TestSuite类的实例化对象的这个suit加载器中,
# 然后再通过导入写测试用例的模块并放入TestLoader类中的loadTestsFromModule方法中作为参数来加载写测试用例模块中的所有测试用例方法
from unit_test import unit_test_case # 导入写测试用例的模块
# 创建用例的加载器：创建TestLoader类对象，即实例化TestLoader类
loader=unittest.TestLoader() # 用例的加载器
suite.addTest(loader.loadTestsFromModule(unit_test_case))

# 第三种方式：通过测试用例的类名来加载测试用例，执行加载的测试用例的类名中的所有测试用例方法
# 通过使用loader模块中的TestLoader类来创建一个加载器，
# 这个加载器可以通过测试用例中的类名来加载测试用例中的类名中的所有测试用例方法，
# 然后再把这个加载器放入TestSuite类的实例化对象的这个suit加载器中,
# 然后再通过导入测试用例中的类名并放入TestLoader类中的loadTestsFromTestCase方法中作为参数来加载测试用例中的类名中的所有测试用例方法
from unit_test.unit_test_case import * # 导入写测试用例的模块
# 创建用例的加载器：创建TestLoader类对象，即实例化TestLoader类
loader=unittest.TestLoader() # 用例的加载器
suite.addTest(loader.loadTestsFromTestCase(TestSub))

# 执行用例并产生测试报告的方式：

# 第一种方式：使用原始的unittest版本
# 执行用例并产生测试报告--unittest版本:用runner模块中的TextTestRunner类，创建一个对象来执行用例
# 执行测试用例后会产生测试报告，默认测试报告打印到控制台console，
# 可通过改变TextTestRunner类中的初始化方法中的stream参数、verbosity参数的值，来指定测试报告写入某个文件，
# 指定测试报告的写入某个文件后，测试报告会显示在指定的文件中，不会显示在控制台了
# stream参数表示写测试报告的位置，默认是None，默认打印到控制台，verbosity参数表示测试报告的详细程度，默认是1，
# verbosity参数有0 1 2三个值，0是最不详细的，2是最详细的
# with open('test.text','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=0) # 指定测试报告写入到test.text文件中
#     runner.run(suite) # 开始执行测试用例：通过TextTestRunner类中的run方法，run方法中加入你要执行的已经加载的测试用例

# 第二种方式：可以下载别人写好的模块，导入进来，再直接查看别人写的方法来调用，如使用HTMLTestRunnerNew版本
# 执行用例并产生html形式的测试报告--HTMLTestRunnerNew版本:
# 导入别人已经写好的生成测试报告的模块HTMLTestRunnerNew，把这个模块放在python安装路径下的lib文件下，
# 就可以直接import HTMLTestRunnerNew导入，不需要一层层的写路径导入，如math_method.py文件的导入路径--unit_test.math_method
import HTMLTestRunnerNew
with open('test.html','wb') as file: # 以网页html形式产生测试报告，所有存放在html形式的文件中,wb表示以文件流的形式写入文件
    # 指定测试报告写入到test.text文件中，verbosity可以不用重新传参
    # HTMLTestRunner方法中stream的默认值是系统输出，可以重新指定生成报告的文件，verbosity的值默认为2，已经是最详细的测试报告结果了，
    # title、description、tester默认值为None，可以自己重新传参修改参数内容
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,title='20190527测试报告',
                                            description='这是加法减法功能验证的测试报告',
                                            tester='花花') # 创建一个对象来执行测试用例
    runner.run(suite) # 执行成功后，会生成test.html文件，
    # 打开方式：1.右键，点击file path，复制路径，再在浏览器打开
    #           2.右键，点击Open in Browser，选择浏览器打开，只有html类型的文件才有这个功能



# 右键运行测试用例：右键运行，还是显示为 Run 'unit_test_suite',即Run '当前文件名'

# 测试报告的显示内容：
# 在不修改TextTestRunner类中的初始化方法中的stream参数、verbosity参数的值时，
# 通过创建TestSuite对象来加载用例并运行时，运行代码后的结果会显示在控制台并且显示内容中会有3种状态，分别是 . E F：
# .表示：一个.通过了一条用例，两个.表示通过了两条用例
# E表示：代码出错
# F表示：用例执行失败
# 如：总共执行3个测试用例，2个成功，1个失败，则会显示为F..




















