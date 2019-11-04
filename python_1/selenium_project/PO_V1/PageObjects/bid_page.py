# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 11:05
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :invest_page.py

from selenium_project.PO_V1.PageLocators.invest_page_locator import InvestPageLocator as loc
from selenium_project.PO_V1.Common.basepage import BasePage

class BidPage(BasePage):

    # 继承的BasePage类中有初始化driver方法
    # def __init__(self,driver):
    #     self.driver=driver

    # 投资
    def invest(self,money):
        # 在输入框当中，输入金额
        self.input_text(loc.money_input,"标页面_金额输入框",money)
        self.click_element(loc.invest_button,"标页面_提交投资操作")

    # 获取用户余额
    def get_user_money(self):
        self.wait_eleVisible(loc.money_input,"标页面_获取用户余额")
        return self.get_element_attribute(loc.money_input,"data-amount","标页面_获取用户余额的属性值")

    # 投资成功的提示框-点击查看并激活
    def click_activeButton_on_success_popup(self):
        self.click_element(loc.active_button_on_successPop,"标页面_投资成功的提示框")

    # 错误提示框-页面中间
    def get_errorMsg_from_pageCenter(self):
        self.wait_eleVisible(loc.invest_failed_popup,"标页面_投资失败提示框")
        msg = self.get_element_text(loc.invest_failed_popup,"标页面_投资失败的提示框内容")
        self.click_element(loc.invest_close_failed_popup_button,"标页面_关闭投资失败的提示框")
        return msg

    # 获取提示信息-投标按钮上的
    def get_errorMsg_from_investButton(self):
        pass