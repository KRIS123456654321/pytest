# _*_ coding:utf-8 _*_
# @Time    :2019/10/21 14:10
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :login_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_project.PO_V1.PageLocators.login_page_locator import LoginPageLocator as loc
from selenium_project.PO_V1.Common.basepage import BasePage

# 一个用例，一次浏览器的打开和结束
class LoginPage(BasePage): # J继承BasePage
    # 属性

    # driver对象不能在功能类中创建，这样操作会导致每调用一次就重新打开一次浏览器，应该在测试用例中创建,然后传入功能类中
    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()

    # 登录功能
    def login(self,user,passwd):
        # 等待，只需要等待一个出现即可，这几个元素都是静态加载的
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.user_loc))
        # 输入用户名，输入密码，点击登录
        # self.driver.find_element(*loc.user_loc).send_keys(user)
        self.input_text(loc.user_loc,"登录页面_输入用户名",user)
        # self.driver.find_element(*loc.passwd_loc).send_keys(passwd)
        self.input_text(loc.passwd_loc,"登录页面_输入密码" ,passwd)
        # self.driver.find_element(*loc.login_button_loc).click()
        self.click_element(loc.login_button_loc,"登录页面_点击登录按钮")
        # 登录结果的断言在用例中写

    # 获取表单错误信息
    def get_error_msg_from_loginForm(self):
        # loc=(By.XPATH,'//div[@class="form-error-info"]')
        # 获取错误信息也可以合并写到一起
        # loc=(By.XPATH,'//div[@class="form-error-info" or @class="layui-layer-content"]')
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.error_notify_from_loginForm))
        # 获取文本封装的关键字中，没有加入元素等待可见，这里要再调用等待元素的方法
        self.wait_eleVisible(loc.error_notify_from_loginForm,"登录页面_表单区域错误信息")
        # return self.driver.find_element(*loc.error_notify_from_loginForm).text
        return self.get_element_text(loc.error_notify_from_loginForm,"登录页面_表单区域错误信息")

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        # loc = (By.XPATH, '//div[@class="layui-layer-content"]')
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_notify_from_pageCenter))
        # 获取文本封装的关键字中，没有加入元素等待可见，这里要再调用等待元素的方法
        self.wait_eleVisible(loc.error_notify_from_pageCenter,"登录页面_页面中间错误信息")
        # return self.driver.find_element(*loc.error_notify_from_pageCenter).text
        return self.get_element_text(loc.error_notify_from_pageCenter,"登录页面_页面中间错误信息")














