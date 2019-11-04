# _*_ coding:utf-8 _*_
# @Time    :2019/10/28 16:05
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :user_page_locator.py

from selenium.webdriver.common.by import By

class UserPageLocator:
    # 获取用户详情的可投标金额
    left_money=(By.XPATH,'//li[@class="color_sub"]')