# _*_ coding:utf-8 _*_
# @Time    :2019/10/21 15:24
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :index_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium_project.PO_V1.PageLocators.index_page_locator import IndexPageLocator as loc
from selenium_project.PO_V1.Common.basepage import BasePage


class IndexPage(BasePage):
    def __init__(self,driver):
        self.driver=driver
    # 正常登录
    def check_nick_name_exists(self):
        '''
        :return: 存在返回True，不存在返回False
        '''
        # 先保证页面中它周围的静态元素已经存在了，证明了这个页面已经有了，再比对要查找的元素，因为不知道要等待的元素什么时候会出现，
        # 如果等待20秒，但实际上不需要等这么久，这样做时间就太长了
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="关于我们"]')))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False
    # 选择第一个进行投标
    def click_invest_button(self):
        # # 等待投标出现
        # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.bid_button))
        # first_invest=self.driver.find_elements(*loc.bid_button)
        # # 点击第一个投标
        # first_invest[0].click()
        self.click_element(loc.bid_button,"首页_点击第一个抢投标按钮")






























