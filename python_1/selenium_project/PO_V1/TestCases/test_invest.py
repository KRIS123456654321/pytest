# _*_ coding:utf-8 _*_
# @Time    :2019/10/23 15:33
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_invert.py

# 拿投资需求举例:

# 用例：
# 正常投资：投资金额为1000
# 异常用例：
# # 这四个异常场景比较简单,可以选择写一下,当然不写也没关系:
# 1.投资为10，提示“要为100的整数倍”
# 2.投资为12，提示“要为10的整数倍”
# 3.投资为非数字，提示“要为1的整数倍”
# 4.投资为0/负数/含空格，提示“请整数填写投标金额”

# # 这两个异常场景比较复杂,可以选择不写,有空可以写下:
# 5.投资数>标总可投额，提示“购买标的金额不能大于标总金额”
# 充值10万，创建一个借款9万块的标
# 6.投资数>可用余额 且 标可投大于投资数，提示“购买标的金额不能大于可用余额”
# 你只有10万，你要投20万，标的可投为200万
# 创建一个标为200万，你去投20万

# 前置（准备工作-可以走接口）、步骤（用户页面操作）、断言（用户页面操作）

# 前置-通过代码来创建前置-尽量少的依赖环境数据（1.防止环境变更，导致数据不可用 2.数据库数据被清理，导致数据没有了）：
# 只需要执行，生成前提条件，不需要验证
# 1.登录
# 2.要有可投的标-有可投的余额
# （可以自己加标，保证此条件成立，这里通过接口/sql进行加标，效率更快，最后用完，要通过接口/sql把加标的数据删除）
# 3.用户余额充足-充值5000块
# （第一种：不管是否余额充足，直接自己充值，保证此条件成立，这里通过接口/sql进行充值，效率更快）
# （第二种：钱>=投资金额，补充，钱<投资金额，就充）

# 步骤：
# 1.首页-选第一个标
# 2.投资页面-输入金额进行投资

# 断言：
# 1.个人页面-个人余额少的部分=投资前的金额-投资后的金额
# 2.投资记录
# 3.标的可投金额-投资金额=投资之后的金额

# 步骤中是否需要加数据库检测？
# 自动化最关心的就是步骤和断言，而这两个都是在用户页面操作的，所以最好不要去涉及到数据库和接口来操作，
# 不然还要做自动化干嘛

# 前置中是可以通过接口来操作的，前置是准备工作，通过接口/sql，效率会更快

# 接口当中会涉及到多表关联，所以需要涉及到数据库

import unittest
from selenium import webdriver
from selenium_project.PO_V1.TestDatas import Comm_Datas as CD
from selenium_project.PO_V1.TestDatas import invest_datas as ID
from selenium_project.PO_V1.PageObjects.login_page import LoginPage
from selenium_project.PO_V1.PageObjects.index_page import IndexPage
from selenium_project.PO_V1.PageObjects.bid_page import BidPage
from selenium_project.PO_V1.PageObjects.user_page import UserPage
import logging
import time
import ddt
import pytest
from selenium_project.PO_V1.Common.logger import get_logger

logging=get_logger('log_invest')

@ddt.ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化浏览器会话
        logging.info("用例类前置：初始化浏览器，登录前程贷系统")
        # 打开浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # 窗口最大化
        cls.driver.get(CD.web_login_url)
        # 登录成功
        LoginPage(cls.driver).login(CD.user,CD.passwd)
        # 首页选择第一个投标
        IndexPage(cls.driver).click_invest_button()
        cls.bid_page=BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        logging.info("用例类后置：关闭浏览器，清理环境")
        # 关闭浏览器
        cls.driver.quit()

    def tearDown(self):
        logging.info("每一个用例后置，刷新当前页面")
        self.driver.refresh()
        time.sleep(0.5)

    @pytest.mark.smoke  # 添加标签，选择有标签的用例执行
    def test_invest_1_success(self):
        logging.info("投资用例：正常场景-投资成功")
        # 标页面-获取投资前的个人余额
        useMoney_beforeInvest=self.bid_page.get_user_money()
        # 标页面-输入投资金额，点击投标按钮
        self.bid_page.invest(ID.success["money"])
        # 标页面-投资成功弹出框，点击查看并激活按钮
        self.bid_page.click_activeButton_on_success_popup()
        # 验证
        # 个人页面-获取用户当前余额
        userMoney_afterInvest=UserPage(self.driver).get_user_leftMoney()
        # 1.余额：投资前获取一下，投资后再获取一下，求差值，如果等于投标成功
        assert  ID.success["money"] == int(float(useMoney_beforeInvest)-float(userMoney_afterInvest))
        # PS:自动化测试独立账号
        # 2.个人页面-投资记录获取

    @ddt.data(*ID.wrong_format_money)
    def test_invest_0_failed_by_No100(self,data):
        logging.info("投资用例：异常场景-投资金额为非100的整数")
        # 标页面-获取投资前的的个人金额
        userMoney_beforeInvest=self.bid_page.get_user_money()
        # 标页面-输入投资金额，点击投标按钮
        self.bid_page.invest(data["money"])
        # 获取提示信息
        errorMsg=self.bid_page.get_errorMsg_from_pageCenter()
        # 刷新
        self.driver.refresh()
        # 获取用户余额
        userMoney_afterInvest=self.bid_page.get_user_money()
        # 断言
        assert errorMsg == data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest






















