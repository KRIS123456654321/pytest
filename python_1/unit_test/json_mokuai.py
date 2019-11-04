# _*_ coding:utf-8 _*_
# @Time    :2019/6/3 11:38
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :123.py

# json

import json
str='{"name":"huahua","age":"18"}'

# json转化为字典
a=json.loads(str)
print(type(a)) # <class 'dict'>
# 字典转化为json
b=json.dumps(a)
print(type(b)) # <class 'str'>