# _*_ coding:utf-8 _*_
# @Time    :2019/5/23 16:06
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :config_class.py

# 自己写一个配置的类，让别人调用（在PeiZhi.py文件中调用这个封装的类，PeiZhi.py文件的内容放在“配置文件的使用与设计”中）
# 类的功能：打开一个配置文件。读取配置文件的内容
# from configparser import ConfigParser
# class myConfig:
#     def __init__(self,conf_filePath,encoding='utf-8'):
#         # 打开配置文件
#         self.cf=ConfigParser()
#         self.cf.read(conf_filePath,encoding)
#     def get_intValue(self,section,option):
#         return self.cf.getint(section,option)
#     def get_boolValue(self,section,option):
#         return self.cf.getboolean(section,option)
#     def get_strValue(self,section,option):
#         return self.cf.get(section,option)
#     def get_floatValue(self,section,option):
#         return self.cf.getfloat(section, option)
#     def get_sections(self):
#         return self.cf.sections()
#     def get_options(self,section):
#         return self.cf.options(section)























