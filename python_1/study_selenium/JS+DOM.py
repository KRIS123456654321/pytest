# _*_ coding:utf-8 _*_
# @Time    :2019/10/10 17:02
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :js_scroll.py

# js+DOM操作

# 第一个：js滚动条

# 在页面上，元素是存在，只是不在肉眼可见区域，但是元素是可见的，在html中是存在的，但是由于长宽的问题，
# 需要滚动才能肉眼看到，即可见区域

# 为什么要滚动到可见/可视区域：只有滚动到可见区域才可以进行操作

# 很多系统不需要手动滚动到可见区域，只需要定位到这个元素，就会自动滚动到可见区域，但是有的需要手动滚动到可见区域，
# 才能定位到这个元素，不然会报找不到这个元素

# js滚动条语法：
# 移动到元素element对象的“底端”与当前窗口的“底部”对齐（auguments[0]表示js，element表示js接收的参数，0表示第一个参数element）：
# driver.execute_script("auguments[0].scrollIntoView(false);",element)
# 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐：
# driver.execute_script("auguments[0].scrollIntoView();",element)
# 移动到页面底部：
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 移动到页面顶部：
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

# 还有一种滚动的方式：scrollIntoViewIfNeeded，自己会判断是否需要滚动，
# 定位的元素需要滚动则会滚动，不需要滚动则会不滚动，可以自己百度一下如何使用

# 滚动操作，滚动的元素只有一个，所以参数也只有一个，一般来说滚动元素，只会有一个元素进行滚动，如果是其他操作，可能会要多个参数

# 有多个参数时，可以这样使用，auguments[0]第一个参数ele，auguments[1]第二个参数num2，auguments[2]第三个参数num3
# driver.execute_script("arguments[0].scrollIntoView(false);var s=arguments[1] > arguments[2] ",ele,num2,num3)

# 如果要执行js的其他语句，如何操作？所有的js语句都是在execute_script中执行
# driver.execute_script("需要执行的js语句")，某种操作对应的js的语句可以百度
# 如果要传参，就把需要传入参数的位置使用arguments[0],arguments[1],arguments[2],再在所有的js后面输入对应的参数，
# 有多个js语句，可以放在每个js语句的后面driver.execute_script("需要执行的js语句;需要执行的js语句;")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.baiaidu.com")
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)
# 等待元素可见
locator=(By.XPATH,'//a[]contains(text(),"全部课程_在线 培训 视频 教程_腾讯课程")')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
# 要滚动的元素
ele=driver.find_element_by_xpath('//a[]contains(text(),"全部课程_在线 培训 视频 教程_腾讯课程")')
# 执行js语句，语法是js
# 移动到元素ele对象的“底端”与当前窗口的“底部”对齐
driver.execute_script("arguments[0].scrollIntoView(false);",ele)
# 移动到元素ele对象的“顶端”与当前窗口的“顶部”对齐
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# 移动到页面底部：
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 移动到页面顶部：
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

# 第二种：js日期控件(涉及到执行多个不同的js语句)
# 1.允许你编辑，直接输入日期：使用send_keys()输入
# 2.只能在日历框里去选日期，不允许你直接编辑
# 可以先把这个元素的不可编辑改为可编辑，然后输入日期，再把可编辑改为不可编辑

# 不知道js语句写的对不对，可以在页面的F12中的Console中输入js语句进行操作

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.12306.cn/index/")
js_pha='var a = document.getElementById("train_date");'\
    'a.readOnly=false;'\
    'a.value="2019-07-01";'\
    'document.getElementById("search_one").click();'
driver.execute_script(js_pha)























