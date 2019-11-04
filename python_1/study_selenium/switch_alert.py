# _*_ coding:utf-8 _*_
# @Time    :2019/9/30 14:02
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :switch_alert.py

# alert弹出框切换
# 第一种：web页面中的html页面元素，即DOM对象，可以通过F12查找到的元素，等到弹出框出现，操作里面元素

# 第二种：alert弹框，不是html元素，如JS脚本中的alert,这个alert弹出框不是html元素中的
# 第一步：切换--不是html，这个弹出框不是html里面的，所以要切换到弹出框
# 第二步：弹出框选择确定或者选择取消

# 第三种：web页面中的html页面元素，自动弹出，自动消失，一般这种弹框都是开发设置好的显示时间，想要捕获它，
# 可以把查找元素的轮询时间设置短点，如0.1秒，WebDriverWait(driver,20，0.1).until()
# 如何定位这个自动消失的弹框？

# 如何输入图形验证码？
# 一般是用万能验证码或者测试环境关闭验证码的功能，这只是个很简单的功能，没必要花费时间在这个上面，进行比对是很麻烦的
# 或者也可以去数据库查询，一般验证码会入库，可以直接去数据库查询入库的验证码，然后输入即可，
# 如果是简单的那种4个数字的验证码，有一个库可以使用，自己去百度一下

# 如何扫码绑定？
# 不好弄，跳过吧

# selenuim中的元素，有四个基本的操作：
# 1.点击操作：click()
# 2.键盘输入操作：send_keys()
# 3.获取文本：WebElement对象.text
# 4.获取属性：WebElement对象.get_attribute(属性名称)
# 如：
# ele=driver.find_element_by_id("press")
# ele.get_attribute("class") # 获取class值
# ele.click() # 点击元素

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baiaidu.com")
# 导致alert弹框出现
driver.find_element_by_id("press").click()
# 等待
WebDriverWait(driver,20).until(EC.alert_is_present()) # 等待alert出现了
# 切换
alert=driver.switch_to.alert()
# 弹出框选择确定
print(alert.text) # 可获取弹出框的文本
alert.accept()
# 弹出框选择取消
# alert.dismiss()
# 在弹出框输入内容
# alert.send_keys()
# 进行后续的其它元素操作
















