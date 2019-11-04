# _*_ coding:utf-8 _*_
# @Time    :2019/10/18 11:30
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :work.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window() # 窗口最大化
driver.implicitly_wait(20)
driver.get("https://www.ketangpai.com/User/login.html")

# 登录课堂派
driver.find_element_by_xpath("//input[@name='account']").send_keys("15884567545")
driver.find_element_by_xpath("//input[@name='pass']").send_keys("xc104070")
driver.find_element_by_xpath('//div[contains(@class,"pt-login")]//a[text()="登录"]').click()

# 等待用户id出现
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID,'user')))

# 如果有公告弹框，则需要关闭公告弹框（注意弹框的id带数字，考虑id是变动的）
try:
    close_ele=driver.find_element_by_xpath('//*[contains(@class,"layui-layer-page")]//div[@class="pop-title"]//a[@class="close"]')
except:
    pass
else:
    close_ele.click()

# 进入所在班级
locator=(By.XPATH,'//div[@id="viewer-container-lists"]//a[@title="Python全栈第15期"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()

# 进入作业
locator=(By.XPATH,'//div[@id="third-nav"]//a[text()="作业"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()

# 随机选择一个已批发的作业，查看成绩
locator=(By.XPATH,'//a[text()="查看成绩"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
score_eles=driver.find_elements(*locator)
# 随机生成一个数
index=random.randint(0,len(score_eles)-1)
# # 随机选择一个【查看成绩的】的元素进入
score_eles[index].click()

# 查看成绩是多少
locator=(By.XPATH,'//p[contains(@class,"score")]//span')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
score=driver.find_element(*locator).text
print("随机找的一个作业，作业成绩为：{}".format(score))

# 获取作业中，被分享的同学名称
stu_eles=driver.find_elements_by_xpath('//p[@class="share-name"]')
print('本次作业被分享的学员昵称为：')
for ele in stu_eles:
    print(ele.text)

# 切换到作业讨论，并发表你的评论
driver.find_element_by_xpath('//a[text()="作业讨论"]').click()
locator=(By.XPATH,'//div[contains(@class,"input-click")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click() # 点击，把输入区域展示出来

comment_loc=(By.XPATH,'//textarea[@class="comment-txt"]') # 在输入区域中找到可以输入评语的输入框
WebDriverWait(driver,10).until(EC.visibility_of_element_located(comment_loc))
driver.find_element(*comment_loc).send_keys("作业已提交了，欧耶！！")
driver.find_element_by_xpath('//div[@class="add-comment"]//a[text()="确定"]').click()

# 点击同学，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才显示出来）
driver.find_element_by_xpath("//*[@id='return-course']").click() # 返回班级首页
stu_loc=(By.XPATH,'//a[text()="同学121"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(stu_loc))
driver.find_element(*stu_loc).click() # 点击同学链接，进入学员页面

all_loc=(By.XPATH,'//li[contains(@class,"all")]') # 点击全部同学
WebDriverWait(driver,20).until(EC.visibility_of_element_located(all_loc))
driver.find_element(*all_loc).click()

stu_loc=(By.XPATH,'//div[@class="all-list"]//p[@class="studentavatar"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(stu_loc))
time.sleep(1) # 有多个列表元素，第一个出现后，需要再等其他的元素出现

stu_eles=driver.find_elements_by_xpath('//div[@class="all-list"]//li')
index=random.randint(1,len(stu_eles)-1) # 随机学生下标
print(index)
stu_mail=stu_eles[index].find_element_by_class_name("mail").get_attribute("title")
print(stu_mail)
stu_eles[index].click()
time.sleep(2)
driver.save_screenshot("111.png") # 截图

# 发消息标志框的定位表达
print('//div[@class="all-list"]//li//p[@title="{}"]/following-sibling::a'.format(stu_mail))

ee=driver.find_element_by_xpath('//div[@class="all-list"]//li//p[@title="{}"]/following-sibling::a'.format(stu_mail))
ActionChains(driver).move_to_element(ee).click(ee).perform() # 鼠标操作

# ee.click() # 点击聊天标志
# ElementNotVisibleException:Message：element not interactable

msg_loc=(By.XPATH,'//textarea[@class="ps-container"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(msg_loc))
driver.find_element(*msg_loc).send_keys("我是小姐姐，你信吗？？",Keys.CONTROL,Keys.ENTER) # 点击同学链接，进入学员页面

# 在同学当中，使用右上角的搜索功能，输入任意一个学生的id，搜索学生信息
driver.find_element_by_xpath('//a[contains(@class,"layui-layer-ico")]').click() # 关闭聊天框
search_loc=(By.XPATH,'//div[contains(@class,"input-box")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(search_loc))
search_ele=driver.find_element_by_xpath("//div[contains(@class,'input-box')]//input") # 查找右上角的搜索框
search_ele.send_keys("1509",Keys.ENTER)
driver.save_screenshot("搜索的学生信息.png")












