# _*_ coding:utf-8 _*_
# @Time    :2019/6/24 10:54
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :config.py

import configparser
from jiekou.common import contants #获取文件地址的模块
class ReadConfig:
    '''完成配置文件的读取'''
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(contants.global_file) # 先加载global
        switch=self.config.getboolean('switch','on')
        if switch: # 开关打开时，使用online的配置
            self.config.read(contants.online_file,encoding='gbk')
        else: # 开关关闭时，使用test的配置
            self.config.read(contants.test_file,encoding='gbk')
    def get(self,section,option):
        return self.config.get(section,option)

config=ReadConfig()
# print(config.get('api','pre_url'))
if __name__ == '__main__':
    config=ReadConfig()
    print(config.get('api','pre_url'))