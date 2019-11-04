# _*_ coding:utf-8 _*_
# @Time    :2019/10/23 15:33
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_invert.py

from selenium_project.PO_V1.TestDatas import invest_datas as ID
from selenium_project.PO_V1.PageObjects.user_page import UserPage
from selenium_project.PO_V1.Common.logger import get_logger
import logging
import pytest

logging=get_logger('log_invest')

@pytest.mark.pytest_invest_smoke
def test_print2():
    print('123456789')

@pytest.mark.usefixtures("invest_fixture") # class级别的前置后置，相当于unittest中的setUpClass、tearDownClass功能
@pytest.mark.usefixtures("refresh_page") # 用例级别的前置后置，相当于unittest中的setUp、tearDown功能
class TestInvest:
    # 正常投资
    @pytest.mark.pytest_invest_smoke  # 添加标签，选择有标签的用例执行
    def test_invest_1_success(self,invest_fixture):
        print('正常投资')
        logging.info("投资用例：正常场景-投资成功")
        # 标页面-获取投资前的个人余额
        useMoney_beforeInvest=invest_fixture[1].get_user_money()
        # 标页面-输入投资金额，点击投标按钮
        invest_fixture[1].invest(ID.success["money"])
        # 标页面-投资成功弹出框，点击查看并激活按钮
        invest_fixture[1].click_activeButton_on_success_popup()
        # 验证
        # 个人页面-获取用户当前余额
        userMoney_afterInvest=UserPage(invest_fixture[0]).get_user_leftMoney()
        # 1.余额：投资前获取一下，投资后再获取一下，求差值，如果等于投标成功
        assert  ID.success["money"] == int(float(useMoney_beforeInvest)-float(userMoney_afterInvest))
        # PS:自动化测试独立账号
        # 2.个人页面-投资记录获取

    @pytest.mark.usefixtures("session_action")
    @pytest.mark.pytest_invest_smoke
    def test_print1(self):
        print('abcdefg')

    # @classmethod
    # def setUpClass(cls):
    #     # 初始化浏览器会话
    #     logging.info("用例类前置：初始化浏览器，登录前程贷系统")
    #     # 打开浏览器
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()  # 窗口最大化
    #     cls.driver.get(CD.web_login_url)
    #     # 登录成功
    #     LoginPage(cls.driver).login(CD.user,CD.passwd)
    #     # 首页选择第一个投标
    #     IndexPage(cls.driver).click_invest_button()
    #     cls.bid_page=BidPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     logging.info("用例类后置：关闭浏览器，清理环境")
    #     # 关闭浏览器
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     logging.info("每一个用例后置，刷新当前页面")
    #     self.driver.refresh()
    #     time.sleep(0.5)

    # @ddt.data(*ID.wrong_format_money)
    # def test_invest_0_failed_by_No100(self,data):
    #     logging.info("投资用例：异常场景-投资金额为非100的整数")
    #     # 标页面-获取投资前的的个人金额
    #     userMoney_beforeInvest=self.bid_page.get_user_money()
    #     # 标页面-输入投资金额，点击投标按钮
    #     self.bid_page.invest(data["money"])
    #     # 获取提示信息
    #     errorMsg=self.bid_page.get_errorMsg_from_pageCenter()
    #     # 刷新
    #     self.driver.refresh()
    #     # 获取用户余额
    #     userMoney_afterInvest=self.bid_page.get_user_money()
    #     # 断言
    #     assert errorMsg == data["check"]
    #     assert userMoney_afterInvest == userMoney_beforeInvest






















