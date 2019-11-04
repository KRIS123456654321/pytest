# _*_ coding:utf-8 _*_
# @Time    :2019/10/29 15:37
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :conftest.py

# fixture = 前置+后置，前置和后置是写在一起的

# 如果很多用例都有同样的前置和后置，那么我就只实现一个，然后需要的用例去调用就好了

# 不能与unittest的前置后置一起使用

# 机制：与测试用例同级，或者是测试用例的父级，创建一个conftest.py文件
# conftest.py文件里：放所有的前置和后置，不需要用例.py文件主动引入conftest文件，会自动识别，因为文件名称是固定的，只能是conftest.py

# 测试用例中存在模块层级，如TestCases中有多个模块包，包中有多个测试用例模块，
# 而有的测试用例的前置后置还不一样，那么如何使用conftest.py文件？
# 每个模块都可以有自己的conftest文件，子层级也可以有自己的conftest.py文件，用例优先使用自己层级的conftest文件，
# 如果没有自己层级的，再使用父级的，也就是目录中上一级的conftest文件，也就是说可以存在相同的conftest名称的文件，
# 一个conftest文件中是可以放很多fixture的前置后置，不同的测试用例模块可能需要调用不同的前置后置函数
# 当然pytest也可以写在测试用例的模块中，但是与其用这种还不如直接用unittest框架，pytest这种更加灵活，且方便管理

# 怎么定义fixture?
# 定一个函数：包含前置操作和后置操作
# 把函数声明为fixture：在函数前面加上@pytest.fixture(作用级别=默认为function)，作用级别是第一个参数
# 在测试用例中调用

# 前置后置写在一个函数中，如何区别前置后置？
# 在前置后置代码中间加上 yield

# @pytest.fixture中的参数说明：
# scope表示作用级别，默认是function，其他值为class、module、package、session
# autouse表示是否自动使用，默认False，表示这个前置后置是被动的，需要其他的测试用例来主动调用它，如果为True，那么所有的测试用例都要执行这个前置后置

# 一个conftest文件中是可以放很多fixture的前置后置，所以要让测试用例来主动调它，而不是它主动塞给测试用例，即autouse参数要为False

from selenium import webdriver
from selenium_project.PO_V1.TestDatas import Comm_Datas as cd
from selenium_project.PO_V1.PageObjects.login_page import LoginPage
from selenium_project.PO_V1.PageObjects.index_page import IndexPage
from selenium_project.PO_V1.PageObjects.bid_page import BidPage
import pytest
import logging

driver=None # 设置全局变量，方便其他方法使用driver

# fixture的定义，如果有返回值，那么写在yield后面
# 在测试用例中，调用有返回值的fixture函数时，函数名称就是代表返回值，如下面的函数名称open_url就是返回值
# 在测试用例中，函数名称作为用例的参数即可
# class级别，相当于unittest中的setUpClass、tearDownClass功能
@pytest.fixture # 不打括号，默认就是function
def open_url():
    global driver # 修改driver的值，要加上global
    # 前置
    driver=webdriver.Chrome()
    driver.maximize_window()  # 窗口最大化
    driver.get(cd.web_login_url)
    # 返回driver，如果有多个值，可以放在元组中返回
    yield driver  # 用来隔开前置后置，它之前的代码是前置，之后的代码是后置
    # 后置
    driver.quit()

# 在测试用例中使用fixture：
# @pytest.mark.usefixtures("函数名称")

# class级别，相当于unittest中的setUpClass、tearDownClass功能
@pytest.fixture(scope="class")
def invest_fixture():
    global driver  # 修改driver的值，要加上global
    # 初始化浏览器会话
    logging.info("用例类前置：初始化浏览器，登录前程贷系统")
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()  # 窗口最大化
    driver.get(cd.web_login_url)
    # 登录成功
    LoginPage(driver).login(cd.user,cd.passwd)
    # 首页选择第一个投标
    IndexPage(driver).click_invest_button()
    bid_page=BidPage(driver)
    yield (driver,bid_page)
    logging.info("用例类后置：关闭浏览器，清理环境")
    # 关闭浏览器
    driver.quit()

# 刷新页面-需要用到前面方法中的driver
# 用例级别，相当于unittest中的setUp、tearDown功能
@pytest.fixture
def refresh_page():
    yield
    driver.refresh()

# # session级别,不需要引用，会自动执行
@pytest.fixture(scope="session")
def session_action():
    print("会话开始，测试用例开始执行")
    yield
    print("会话结束，测试用例全部执行完成")
































