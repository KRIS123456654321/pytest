# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 14:54
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :basepage.py

# 封装关键字：把元素的操作封装关键字，并添加集成实时异常捕获、失败截图、执行日志

# 也可以把重复使用的业务流程也封装成关键字，放在别的包的模块中

import logging
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_project.PO_V1.Common.dir_config import screenshot_dir
from selenium_project.PO_V1.Common.logger import get_logger

# logging=get_logger('log_invest')

class BasePage:
    # 包含了PageObjects当中，用到所有的selenium底层的方法，
    # 还可以包含通用的一些元素操作，如alert、iframe、windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录，实现失败截图
    def __init__(self,driver):
        self.driver=driver

    # 等待元素可见
    def wait_eleVisible(self,loc,img_doc="",timeout=30,frequency=0.5):
        logging.info("等待元素{}可见".format(loc))
        try:
            # 起始等待的时间 datetime
            start=datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("开始等待时间点：{},结束等待时间点：{}，等待时长为：{}".format(start,end,end-start))
        except:
            # 日志
            logging.exception("等待元素可见失败：") # 日志的一个级别，更加详细的日志信息
            # 截图-哪一个用例哪一个页面哪一个操作导致的失败
            self.save_web_screenshot(img_doc)
            raise # 需要添加raise，不然失败后，没有抛出异常，unitest无法捕获失败异常，
            # 就会一直执行下去，直到断言

    # 查找元素
    def get_element(self,loc,img_doc=""):
        '''
        :param loc: 元素定位，以元组的形式（定位类型，定位时间）
        :param img_doc: 截图说明，例如：登录页面_输入用户名
        :return: WebElement对象
        '''
        logging.info("查找 {} 中的元素 {}".format(img_doc,loc))
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            #日志
            logging.exception("查找元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 点击元素
    # 为什么不把等待、查找、操作都放在一个函数中？
    # 1.有的元素不需要等待操作，如登录的账号和密码，只要账号存在即可，密码不需要，密码只需要调用“先找元素”
    # 2.每一步我们都需要写日志，捕获异常，写在一起的话，不好捕获异常
    # 3.有的元素只需要存在即可，不需要可见，即只需要调用“先找元素”，如点击和输入内容时要可见的才能操作，获取属性值、文本值只要存在即可，
    # 不需要可见，因为没有对它做实质性的操作
    # 所以一般操作的函数中是不会调用“等待元素”，而是当需要的时候，单独在页面功能中再调用
    # 下面的点击和输入文本都是需要元素可见的，所以函数中直接调用了“等待元素”
    def click_element(self,loc,img_doc,timeout=30,frequency=0.5):
        '''
        实现了，等待元素可见，找元素，然后再去点击元素
        :param loc:
        :param img_doc:
        :return:
        '''
        # 等待元素可见
        self.wait_eleVisible(loc, img_doc,timeout,frequency)
        # 先找元素
        ele=self.get_element(loc,img_doc)
        # 再操作，点击元素
        logging.info("点击元素{}".format(loc))
        try:
            ele.click()
        except:
            # 日志
            logging.exception("点击元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 文本输入
    def input_text(self,loc,img_doc,*args):
        self.wait_eleVisible(loc,img_doc)
        # 先找元素
        ele=self.get_element(loc,img_doc)
        # 再操作，文本输入
        logging.info("给元素{}输入文本内容：{}".format(loc,args))
        try:
            ele.send_keys(*args)
        except:
            # 日志
            logging.exception("元素输入操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的属性值，不需要调用“等待元素”，只需要元素存在即可
    def get_element_attribute(self, loc, attr_name,img_doc):
        # 先找元素
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            attr_value=ele.get_attribute(attr_name)
            logging.info("获取元素{}的属性{}值为：{}".format(loc, attr_name,attr_value))
            return attr_value
        except:
            # 日志
            logging.exception("获取元素属性失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的文本值，不需要调用“等待元素”，只需要元素存在即可
    def get_element_text(self, loc, img_doc):
        # 先找元素
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            text = ele.text
            logging.info("获取元素{}的文本值为：{}".format(loc,text))
            return text
        except:
            # 日志
            logging.exception("获取元素文本值失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 实现网页截图操作
    def save_web_screenshot(self,img_doc):
        # 在本地存储时间，不支持20180806.12:45:44，不支持冒号，可以写成20180806.124544
        now=time.strftime("%Y-%m-%d %H-%M-%S")
        filepath='{}_{}.png'.format(img_doc,now)
        # 图片根目录 + 页面功能_时间.png
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logging.info("网页截图成功，图片存储在：{}".format(screenshot_dir + "/" + filepath))
        except:
            logging.exception("网页截屏失败！")
            raise

    # windwows切换
    def switch_window(self):
        # 等待可用的window并切换-webDriverWait
        pass
    # iframe切换
    def switch_iframe(self,iframe_reference):
        # 等待可用的iframe并切换-webDriverWait
        pass
    # select下拉列表

    # 上传操作
















