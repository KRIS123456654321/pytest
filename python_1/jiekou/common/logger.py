# _*_ coding:utf-8 _*_
# @Time    :2019/6/28 16:18
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :test_log.py

# 添加日志的用处：
# 1.不管执行多少次代码，日志都会一直保存，而print到控制台，每次执行都会替换前一次的输出
# 2.可以根据不同的日志信息，定义不同的级别，然后指定不同渠道的输出级别，来决定什么样的信息在哪里显示

# 默认输出渠道：在控制台
# 默认输出级别：error级别以及error级别以上
# info：记录测试过程，如测试什么时候开始，什么时候结束，测试的前置是什么，测试的后置是什么等
# debug：记录请求的数据，如请求的url请求的data请求的响应结果等

# import logging
# logger=logging.getLogger()
# logger.info('测试开始啦')
# logger.error('测试报错了')
# logger.debug('测试数据')
# logger.info('测试结束')

# 如何知道当前打印的log是在什么地方调用的，什么时候调用的？
# 1.通过给log一个名字来设置不同的log，用于多个文件使用不同的log记录，同一个文件的不同的地方使用不同log记录，具体使用如下

# import logging
# logger=logging.getLogger('case') # 通过给log一个名字（如case）来设置不同的log，用于多个文件使用不同的log记录，
# # 同一个文件的不同的地方使用不同log记录，就能知道这个log是在什么地方调用的，什么时候调用的
# logger.setLevel('DEBUG') # 设置总的输出级别，相当于大开关
#
# fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s:%(lineno)d]'
# formatter=logging.Formatter(fmt=fmt) # 设置输出内容的格式
#
# console_handler=logging.StreamHandler() # 设置输出渠道为控制台
# console_handler.setLevel('DEBUG') # 设置输出到控制台的输出级别，相当于小开关
# console_handler.setFormatter(formatter) # 设置输出到控制台的输出内容格式
#
# file_handler=logging.FileHandler('case.log',encoding='utf-8') # 设置输出渠道为文件
# file_handler.setLevel('INFO') # 设置输出到文件的输出级别，相当于小开关
# file_handler.setFormatter(formatter) # 设置输出到文件的输出内容格式
#
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
#
# logger.info('测试开始啦')
# logger.error('测试报错了')
# logger.debug('测试数据')
# logger.info('测试结束')

# 写一个打印日志的类：为了使不同的文件可以打印日志，同一个文件的不同的地方可以打印日志，且通过设置日志名，
# 来知道当前打印的log是在什么地方调用的，什么时候调用的
import logging
from jiekou.common import contants
from jiekou.common.config import config
def get_logger(name):
    logger=logging.getLogger(name) # 设置log名字
    logger.setLevel('DEBUG') # 设置总的输出级别，相当于大开关

    fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s:%(lineno)d]'
    formatter=logging.Formatter(fmt=fmt) # 设置输出内容的格式

    console_handler=logging.StreamHandler() # 设置输出渠道为控制台
    # 把日志级别放在配置文件里面配置
    lever=config.get('lever','console_lev')
    console_handler.setLevel(lever) # 设置输出到控制台的输出级别，相当于小开关
    console_handler.setFormatter(formatter) # 设置输出到控制台的输出内容格式

    file_handler=logging.FileHandler(contants.log_dir+'/'+name+'.log',encoding='utf-8') # 设置输出渠道为文件
    # 把日志级别放在配置文件里面配置
    lever=config.get('lever','log_lev')
    file_handler.setLevel(lever) # 设置输出到文件的输出级别，相当于小开关
    file_handler.setFormatter(formatter) # 设置输出到文件的输出内容格式

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    logger=get_logger('case') # 传日志名
    logger.info('测试开始啦')
    logger.error('测试报错了')
    logger.debug('测试数据')
    logger.info('测试结束')