# _*_ coding:utf-8 _*_
# @Time    :2019/10/22 14:37
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :login.py

from selenium.webdriver.common.by import By

class LoginPageLocator:
    # 用户名输入框
    user_loc=(By.XPATH,'//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH,'//input[@name="password"]')
    # 登录按钮
    login_button_loc = (By.TAG_NAME,'button')
    # 提示框-登录表单区域
    error_notify_from_loginForm = (By.XPATH, '//div[@class="form-error-info"]')
    # 提示框-页面中间区域
    error_notify_from_pageCenter = (By.XPATH, '//div[@class="layui-layer-content"]')





















