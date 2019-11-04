# _*_ coding:utf-8 _*_
# @Time    :2019/10/10 15:29
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :keyword.py

# 键盘输入：send_keys()，可以结合组合键操作，使用Keys类

# 组合键的输入，使用Keys类，如输入框输入内容+键盘enter，Keys类中有很多键盘操作的方法
# 前提是支持这样的组合键，才可以这样操作，不然就得点击对应的按钮了，如enter键

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baiaidu.com")
# 组合键的输入，使用Keys类，如输入框输入内容+键盘enter，Keys类中有很多组合键的键盘操作方法
# 组合键，如：数字0-9，上下左右，清除，进入enter等
# 前提是支持enter键，才可以这样操作，不然就得点击对应的按钮了
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)

# send_keys()去输入内容，提交的时候，有的时候页面提示内容为空？
# 解决办法：
# 第一种：通过dom对象去设置它的value值，要使用js语句
# 第二种：先点位输入框点击一下，再定位输入框输入内容

















































