# _*_ coding:utf-8 _*_
# @Time    :2019/6/24 15:46
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :context.py

# 用来存放加标接口测试用例test_invest中一个接口中查询出数据库的数据loan_id作为另一个接口的参数化数据
class Context:
    load_id=None

# 写一个正则表达式的方法，通过获取需要参数化数据的标识，来获取配置文件中该参数对应的数据，并替换参数化数据的标识
import re
import configparser
from jiekou.common.config import config

def replace(data):
    p="#(.*?)#" # 正则表达式
    while re.search(p,data):
        m = re.search(p, data)
        g = m.group(1)  # 获取到参数化数据的标识
        try:
            v = config.get('data', g)  # 根据参数化标识取配置文件中的值
        except configparser.NoOptionError as e: # 如果配置文件中没有，则去Context类中找
            # 利用类的反射
            if hasattr(Context,g):
                v=getattr(Context,g)
                print('标的id：',v)
            else:
                print('找不到参数化的值')
                raise e
        # 替换后的内容，继续用data来接收，方便再次循环使用
        data = re.sub(p, v, data, count=1)  # count默认为0，替换所有的符合正则表达式的字符串
    print('最后替换后的data：',data) # 最后替换后的data：{"mobilephone":"15810447878","pwd":"123456"}
    return data

if __name__ == '__main__':
    replace('#normal_user#')
