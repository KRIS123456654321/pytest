# _*_ coding:utf-8 _*_
# @Time    :2019/5/26 16:18
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :math_method.py

class MathMethod:
    def add(self,a,b):
        return (a+b)
    def sub(self,a,b):
        return (a-b)

if __name__ == '__main__':
    print(MathMethod().add(0,0)) # 0
    print(MathMethod().add(1,-3)) # -2