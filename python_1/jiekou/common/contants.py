# _*_ coding:utf-8 _*_
# @Time    :2019/6/20 15:58
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :contants.py

# 在项目结构不改变的情况下，获取所要引用的文件地址
# 前提是：项目结构不能改变
# 把这个项目放在任何地方的，引用文件的路径都可以不用修改
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取当前文件的项目根目录
# print(base_dir) # D:\file\python\python_1\jiekou

# 根据当前文件的根目录，再根据根目录找到根目录下的文件地址
case_file=os.path.join(base_dir,'data','cases.xlsx') # 获取data包中cases.xlsx表格数据的绝对路径地址
# print(case_file) # D:\python_code\jiekou\data\cases.xlsx

global_file=os.path.join(base_dir,'config','global.conf') # 获取data包中global.conf配置文件的绝对路径地址
# print(global_file) # D:\python_code\jiekou\config\global.conf

online_file=os.path.join(base_dir,'config','online.conf') # 获取data包中online.conf配置文件的绝对路径地址
# print(online_file) # D:\python_code\jiekou\config\online.conf

test_file=os.path.join(base_dir,'config','test.conf') # 获取data包中test.conf配置文件的绝对路径地址
# print(test_file) # D:\python_code\jiekou\config\test.conf

log_dir=os.path.join(base_dir,'log') # 获取data包中log打印日志的包的绝对路径地址
# print(log_dir) # D:\file\python\python_1\jiekou\log






















