# _*_ coding:utf-8 _*_
# @Time    :2019/11/4 18:15
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :combat-5.py

import pytest

@pytest.fixture
def myfix_1():
    print("----开始  第一个myfix_1----")
    a=True
    yield a
    print("----结束  第一个myfix_1----")

@pytest.fixture
def myfix_2_bigger(myfix_1):
    print("----开始  第2个myfix_2_bigger----")
    print(myfix_1)
    if myfix_1==True:
        c="Yes"
    else:
        c="No"
    yield
    print("----结束  第2个myfix_2_bigger----")

@pytest.mark.demo
def test_demo(myfix_2_bigger): # fixtures的函数名称作为用例参数
    print("----我是测试用例----")
    print(myfix_2_bigger)

