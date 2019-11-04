# _*_ coding:utf-8 _*_
# @Time    :2019/10/21 15:03
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_login.py

# 写一个pytest版本的使用fixture前置后置的登录测试用例：
# pytest版本的使用fixture前置后置不能与unittest一起使用，不兼容

# pytest版本的登录测试用例中加上一个pytest_smoke标签，用来与unittest版本的登录、投标的测试用例区分开来，
# unittest版本的登录、投标的测试用例的标签为smoke，保证待会运行时不运行unittest版本的登录、投标的测试用例，
# 只运行pytest版本的登录测试用例中加了pytest_smoke标签的测试用例

from selenium_project.PO_V1.PageObjects.login_page import LoginPage
from selenium_project.PO_V1.PageObjects.index_page import IndexPage
from selenium_project.PO_V1.TestDatas import login_datas as ld
import pytest
from selenium_project.PO_V1.Common.logger import get_logger

logging=get_logger('log_invest')


@pytest.mark.pytest_login_smoke
@pytest.mark.parametrize("a,b,c",[(1,3,4),(10,35,45),(22.22,22.22,44.44)])
def test_add(a,b,c): # 第一组数据：a=1,b=3,c=4
    res=a+b
    assert res==c

@pytest.mark.pytest_login_smoke
@pytest.mark.parametrize("x",[0,1])
@pytest.mark.parametrize("y",[2,3])
def test_foo(x,y): # 第一组数据：a=1,b=3,c=4
    print(x,y) # 运行后的结果为：0,2  0,3  1,2  1,3

# @ddt.ddt
# class TestLogin(unittest.TestCase):
# 使用函数名称为open_url的fixture
@pytest.mark.usefixtures("open_url")
class TestLogin:

    # 异常用例-无密码
    # @ddt.data(*ld.wrong_datas)
    # @pytest.mark.pytest_login_smoke
    @pytest.mark.parametrize("data",ld.wrong_datas) # data是参数名，可以自己定义，wrong_datas数据前面不需要加*，会自己解包数据
    def test_login_failed_by_wrong_datas(self,data,open_url):
        # 步骤-登录操作-登录页面-密码为空 18684720553
        LoginPage(open_url).login(data["user"],data["passwd"])  # 测试对象+测试数据
        # 断言-页面的提示
        assert data["check"]==LoginPage(open_url).get_error_msg_from_loginForm()

    # 正常用例-登录 + 首页
    # 添加标签，选择有标签的用例执行
    def test_login_success(self,open_url): # open_url=driver,也就是调用的前置后置函数open_url返回的driver,
        # 如果返回的open_url是多个值，那么直接使用open_url[index]来取值
        LoginPage(open_url).login(ld.success_data["user"],ld.success_data["passwd"]) # 测试对象+测试数据
        # 断言-url跳转,driver.current_url获取当前页面的URL
        # self.assertEqual(open_url.current_url,ld.success_data["check"])
        assert open_url.current_url == ld.success_data["check"]
        # 断言-页面是否存在-“我的账户”元素
        # self.assertTrue(IndexPage(open_url).check_nick_name_exists())
        assert IndexPage(open_url).check_nick_name_exists()

    # # 异常用例-用户名未注册/密码错误
    # @ddt.data(*ld.fail_datas)
    # def test_login_failed_by_fail_datas(self,data):
    #     # 步骤-登录操作-登录页面-密码为空 18684720553
    #     LoginPage(self.driver).login(data["user"],data["passwd"])  # 测试对象+测试数据
    #     # 断言-页面的提示
    #     self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_pageCenter())


    # def setUp(self):
    #     # 前置-打开网页，启动浏览器
    #     self.driver=webdriver.Chrome()
    #     self.driver.maximize_window()  # 窗口最大化
    #     self.driver.get("{}/Index/login.html".format(cd.base_url))
    #
    # # 关闭浏览器
    # def tearDown(self):
    #     self.driver.quit()





















