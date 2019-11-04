# _*_ coding:utf-8 _*_
# @Time    :2019/10/21 15:03
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_login.py

# 测试用例=页面对象（提供功能）+ 测试数据

# 测试登录：2个页面，登录页面 + 首页
# 登录页面：登录功能（输入+点击）、获取页面错误信息
# 首页：存在 我的账户 这样的一个元素

# 每一条用例都要打开一次浏览器，有点浪费时间，但是自动化是先追求稳定再考虑时间
# 用例之间要保持独立性，不能因为上一条用例失败，导致下一条用例也失败

from selenium import webdriver
import unittest
import  ddt
from selenium_project.PO_V1.PageObjects.login_page import LoginPage
from selenium_project.PO_V1.PageObjects.index_page import IndexPage
from selenium_project.PO_V1.TestDatas import login_datas as ld
from selenium_project.PO_V1.TestDatas import Comm_Datas as cd
import logging
import pytest
from selenium_project.PO_V1.Common.logger import get_logger

logging=get_logger('log_invest')

# 用例三步曲：前置、步骤、断言

# 每一条用例都要打开一次浏览器，有点浪费时间，但是自动化是先追求稳定再考虑时间
# 下面有个节约时间的版本，但是会导致用例之间不独立的弊端，具体是否使用，看当时的用例情况
@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 前置-打开网页，启动浏览器
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()  # 窗口最大化
        self.driver.get("{}/Index/login.html".format(cd.base_url))

    # 正常用例-登录 + 首页
    @pytest.mark.smoke # 添加标签，选择有标签的用例执行
    def test_login_success(self):
        # logging.info("用例1-正常场景-登录成功-使用到测试数据")
        # 步骤-登录操作-登录页面- 18684720553 python
        LoginPage(self.driver).login(ld.success_data["user"],ld.success_data["passwd"]) # 测试对象+测试数据
        # url跳转,driver.current_url获取当前页面的URL
        self.assertEqual(ld.success_data["check"],self.driver.current_url)
        # 断言-页面是否存在-“我的账户”元素
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())

    # 异常用例-无密码
    @ddt.data(*ld.wrong_datas)
    def test_login_failed_by_wrong_datas(self,data):
        # 步骤-登录操作-登录页面-密码为空 18684720553
        LoginPage(self.driver).login(data["user"],data["passwd"])  # 测试对象+测试数据
        # 断言-页面的提示
        self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())


    # # 异常用例-无用户名
    # def test_login_failed_by_no_user(self):
    #     # 步骤-登录操作-登录页面-用户名为空 python
    #     LoginPage(self.driver).login('', 'python')  # 测试对象+测试数据
    #     # 断言-页面的提示为：“请输入手机号码”
    #     self.assertEqual("请输入手机号",LoginPage(self.driver).get_error_msg_from_loginForm())

    # # 异常用例-手机号错误
    # def test_login_failed_by_wrong_user_formater(self):
    #     # 步骤-登录操作-登录页面-用户名错误  1867744 python
    #     LoginPage(self.driver).login('1867744', 'python')  # 测试对象+测试数据
    #     # 断言-页面的提示为：“请输入正确的手机号”
    #     self.assertEqual("请输入正确的手机号",LoginPage(self.driver).get_error_msg_from_loginForm())

    # 异常用例-用户名未注册/密码错误
    @ddt.data(*ld.fail_datas)
    def test_login_failed_by_fail_datas(self,data):
        # 步骤-登录操作-登录页面-密码为空 18684720553
        LoginPage(self.driver).login(data["user"],data["passwd"])  # 测试对象+测试数据
        # 断言-页面的提示
        self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_pageCenter())

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()

# 优化版,节约时间,一直在一个页面运行的用例,可以不需要每次都打开浏览器,直接按F5刷新一下即可
# 特征：异常用例,一直在一个页面运行的用例
# 结论：可以进行时间优化，可以不需要每次都打开浏览器,直接按F5刷新一下即可
# 弊端：一旦中间有个用例失败了，如跳转到别的页面了，那么后面的用例就执行不了了，就影响了别的用例运行，
# 这就违背了用例要保持独立性的原则
# 第一步：把前置方法和后置方法改为只执行一次的方法
# 第二步：添加一个每执行一次用例就会自动执行的后置方法进行页面刷新操作
# 第三步：先执行在一个页面操作的异常用例，再执行登录成功后，需要跳转到新页面的用例
# @ddt.ddt
# class TestLogin(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         # 前置-打开网页，启动浏览器
#         cls.driver=webdriver.Chrome()
#         cls.driver.maximize_window()  # 窗口最大化
#         cls.driver.get("{}/Index/login.html".format(cd.base_url))
#
#     # 正常用例-登录 + 首页
#     def test_login_2_success(self):
#         # 步骤-登录操作-登录页面- 18684720553 python
#         LoginPage(self.driver).login(ld.success_data["user"],ld.success_data["passwd"]) # 测试对象+测试数据
#         # url跳转,driver.current_url获取当前页面的URL
#         self.assertEqual(ld.success_data["check"],self.driver.current_url)
#         # 断言-页面是否存在-“我的账户”元素
#         self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
#
#     # 异常用例-无密码
#     @ddt.data(*ld.wrong_datas)
#     def test_login_0_failed_by_wrong_datas(self,data):
#         # 步骤-登录操作-登录页面-密码为空 18684720553
#         LoginPage(self.driver).login(data["user"],data["passwd"])  # 测试对象+测试数据
#         # 断言-页面的提示
#         self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())
#
#     # 异常用例-用户名未注册/密码错误
#     @ddt.data(*ld.fail_datas)
#     def test_login_1_failed_by_fail_datas(self,data):
#         # 步骤-登录操作-登录页面-密码为空 18684720553
#         LoginPage(self.driver).login(data["user"],data["passwd"])  # 测试对象+测试数据
#         # 断言-页面的提示
#         self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_pageCenter())
#
      # 刷新页面
#     def tearDown(self):
#         # 刷新当前页面，每执行完一个用例就会自动执行一次
#         self.driver.refresh()
#
#     # 关闭浏览器
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()




















