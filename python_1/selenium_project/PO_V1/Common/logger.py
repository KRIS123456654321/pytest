# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 15:15
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :logger.py

import logging
from selenium_project.PO_V1.Common import dir_config
from selenium_project.PO_V1.TestDatas import Comm_Datas
def get_logger(name):
    logger=logging.getLogger(name) # 设置log名字
    logger.setLevel('DEBUG') # 设置总的输出级别，相当于大开关

    fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s:%(lineno)d]'
    formatter=logging.Formatter(fmt=fmt) # 设置输出内容的格式

    console_handler=logging.StreamHandler() # 设置输出渠道为控制台
    # 把日志级别放在配置文件里面配置
    lever=Comm_Datas.console_lev # DEBUG
    console_handler.setLevel(lever) # 设置输出到控制台的输出级别，相当于小开关
    console_handler.setFormatter(formatter) # 设置输出到控制台的输出内容格式

    file_handler=logging.FileHandler(dir_config.logs_dir+'/'+name+'.log',encoding='utf-8') # 设置输出渠道为文件
    # 把日志级别放在配置文件里面配置
    lever=Comm_Datas.log_lev  # INFO
    file_handler.setLevel(lever) # 设置输出到文件的输出级别，相当于小开关
    file_handler.setFormatter(formatter) # 设置输出到文件的输出内容格式

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger