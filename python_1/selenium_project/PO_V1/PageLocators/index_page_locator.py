# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 10:03
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :index_page_locator.py

from selenium.webdriver.common.by import By

class IndexPageLocator:
    # 第一个投标
    bid_button=(By.XPATH,'//div[@class="b-unit"][1]//div[@class="text-center"]//a')