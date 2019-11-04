# _*_ coding:utf-8 _*_
# @Time    :2019/9/10 9:59
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :selenium_72.py

# 元素存在、元素可见、元素可用的区别：
# 元素存在：在页面的html中有该元素，能找到，在页面中不一定可以看见
# 元素可见：在页面的html中有该元素，且在页面中可以看见，但不一定可以操作，只能读，不能点击，输入等
# 元素可用：在页面的html中有该元素，且在页面中可以看见，且可以操作

# 1.强制等待，单位是秒
# 操作页面上的元素，必须等页面的元素加载完成才能进行操作，然而强制等待几秒，并不能保证它一定能在几秒内出现，
# 有可能会超过设置的时间，这样接下来的操作就会抛异常，所以强制等待并不智能，那么试试第二种，智能等待

# 2.智能等待：隐性等待，查找元素，如果你10秒出现了，我就开始下一步操作，但是需要设置上限：比如30秒，超过30秒，就超时TimeoutException
# 等待的范围是元素可见，不能等待窗口切换，判断窗口是否出现，窗口切换是个命令

# 3.智能等待：显性等待，明确的条件（元素可见、窗口存在），等待+条件
# 明确到满足某个条件之后，再去执行下一步操作，轮循等待，每隔几秒看一下条件是否成立，否则继续等待，
# 直到超过设置的最长时间，然后抛出TimeoutException
# 第一步：引入相关的库
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# 第二步：使用WebDriverWait方法设置driver，总等待时长，轮循周期等三个参数，轮循默认时间是0.5秒，再设置条件
# 如：WebDriverWait(driver,30).until() # 轮循默认时间是0.5秒，until()表示某个条件成立
# 或 WebDriverWait(driver,30，1).until_not() # 轮循时间是1秒，until_not()表示某个条件不成立

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# 浏览器会话的开始
driver = webdriver.Chrome()
# 智能等待(隐性等待)：设置全局等待时间，单位是秒，只需要写一次，后面的查找元素代码都会等待30秒
driver.implicitly_wait(30)

driver.get("http://www.baiaidu.com") # get函数会等待静态页面加载完成
# 不需要写智能等待了，找这个元素会等待30秒，30秒之内找到即可，找不到抛出异常
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="ti_login"]').click()
# 当你的操作带来了页面的变化，请一定要等待

# 强制等待：傻傻等待5秒
# 强制等待和智能等待没有前后关系，执行到这了，就会强制等待5秒
# time.sleep(5)

# 智能等待（显性等待）：轮循默认时间是0.5秒，until()表示某个条件成立，until_not()表示某个条件不成立
WebDriverWait(driver,30).until()
EC.visibility_of_element_located('TANGRAM__PSP_10__footerULoginBtn') # 成功返回元素对象，失败返回False

# 不需要写智能等待了，找这个元素会等待30秒，30秒之内找到即可，找不到抛出异常
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

# 关闭当前的窗口
# driver.close()

# 浏览器会话的结束，关闭浏览器关闭了chromedriver
# 在代码调试的时候，可以不加上这句话，在代码调试完成后，要加上这句话
# driver.quit()



























