# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 13:58
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :user_page.py

from selenium_project.PO_V1.Common.basepage import BasePage
from selenium_project.PO_V1.PageLocators.user_page_locator import UserPageLocator as loc

class UserPage(BasePage):

    def __init__(self,driver):
        self.driver=driver

    # 获取个人详情页的可投标金额
    def get_user_leftMoney(self):
        self.wait_eleVisible(loc.left_money, "标页面_获取总余额")
        left_money=self.get_element_text(loc.left_money,"标页面_获取总余额的文本值")
        length=len(left_money)-2
        return left_money[0:length:1] # 只取字符串中的前面的数字，上面拿到的文本值是数字+元