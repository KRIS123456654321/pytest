# _*_ coding:utf-8 _*_
# @Time    :2019/10/25 9:55
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :invest_page_locator.py

from selenium.webdriver.common.by import By

class InvestPageLocator:
    # 获取可投标余额
    money_input = (By.XPATH,'//input[contains(@class,"invest-unit-investinput")]')
    # 点击投标
    invest_button = (By.XPATH,'//button[contains(@class,"height_style")]')
    # 点击查看并激活
    active_button_on_successPop=(By.XPATH,'//div[@class="layui-layer-content"]//button')
    # 投资失败—中间提示
    invest_failed_popup=(By.XPATH,'//div[@class="text-center"]')
    # 关闭投资失败
    invest_close_failed_popup_button=(By.XPATH,'//a[@class="layui-layer-btn0"]')