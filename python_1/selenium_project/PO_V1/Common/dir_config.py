# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 15:15
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :dir_config.py

import os

# 获取框架顶层目录
base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

logs_dir=os.path.join(base_dir,"Outputs\logs")

# 获取存放失败截图的路径
screenshot_dir=os.path.join(base_dir,"Outputs\screenshots")



















