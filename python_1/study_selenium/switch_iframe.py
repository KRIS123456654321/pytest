# _*_ coding:utf-8 _*_
# @Time    :2019/9/22 17:40
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :switch_iframe.py

# iframe是html里面嵌套一个html
# DOM对象定位只针对一个html页面，即当前的html，id也是唯一，xpath定位出来的也是唯一的，
# 而iframe是html里面嵌套另一个html，所以要先切换到iframe中，才能定位iframe中的元素

# 这里只是记录了iframe切换的重要步骤，具体代码整体操作后面作业会讲解
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baiaidu.com")
# 第一步：确认你要操作的元素是否在iframe中，可以通过F12来查看
# 第二步：确认iframe的特征，有几个iframe，有什么属性

# 第一种方式：
# 第三步：等待iframe是可用的
# 第四步：切换操作，切换到要使用的iframe中
# frame方法中，可以传三个参数，index（下标）或name（属性）或webelement（元素定位的对象）
# driver.switch_to.frame(4) # 参数传递index下标，下标好像是从1开始，具体可以自己试下，一般不会用这种方式
# driver.switch_to.frame("login_frame_qq") # 参数传递name（属性），有这个name属性，则用它更方便
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]')) # 参数传递webelement（元素定位的对象）
# 第五步：进入了iframe里面的html页面，主页面了，然后查找元素，操作元素

# 第二种方式：
# 第三步：确认iframe可用，并切进iframe
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
# 第四步：进入了iframe里面的html页面，主页面了，然后查找元素，操作元素


































