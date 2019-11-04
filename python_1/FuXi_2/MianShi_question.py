# _*_ coding:utf-8 _*_
# @Time    :2019/6/14 17:27
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :MianShi_question.py

# # 1.给定一个列表[1,4,5,3,'a',3]，去除其中重复的元素
# 第一种：命令式
# a=[1,4,5,3,'a',3]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b) # [1, 4, 5, 3, 'a']
# 第二种：函数式
# a=[1,4,5,3,'a',3]
# def del_repeat(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b
# print(del_repeat(a)) # [1, 4, 5, 3, 'a']
# # 第三种：用尽量少的代码完成
# a=[1,4,5,3,'a',3]
# set()：可以进行去重，生成的是一个集合，是一个无序且不重复的元素集合
# list():变成列表
# print(list(set(a))) # [1, 3, 4, 5, 'a']

# 2.列表和字符串的相互转换
# 列表转换为字符串：
# a=['t','2','6','a']
# a_str=''
# for i in a:
#     a_str+=str(i)
# print(''.join(a)) # t26a
# 字符串转换为列表：
# b_str='weqweq'
# b=[]
# for i in b_str:
#     b.append(i)
# print(b) # ['w', 'e', 'q', 'w', 'e', 'q']

# 3.字符串去重，加排序
a='12389123512356723'
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b,type(b)) # ['q', 'w', 'e', 'h', 'i', 'u', 'a', 's', 'g', 'd']
print(b.sort())

x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)# [1, 2, 4, 6, 7, 9]

# 4.你的代码遇到bug，你是如何处理的？你在工作中遇到的最困难的是什么？你是怎么解决的?自己解决的问题，能不能解决根本性问题？
# 技术社区：GitHub stackoverflow infoQ
# 在一些技术社区寻找问题，解决当前问题
# 文档  看源码，解决本质问题
# 定位问题：看报错的类型，断点调试

# 5.怎么拷贝列表，默认参数不能为可变类型
# a=['3']
# b=a # b和a是同一个对象，指向的是同一个对象
# c=a[:] # c和a不是同一个对象，a[:]是切片，可以拷贝一个新的对象，所以c和a不是同一个对象
# a.append(10)
# print(a,id(a)) # ['3', 10] 2242000
# print(b,id(b)) # ['3', 10] 2242000
# print(c,id(c)) # ['3'] 1981016

# 6.单例模式的实现：只能生成一个对象
# 通过改变__new__方法，这个方法是用来生成对象的，初始化__init__方法是默认会调用__new__方法，生成对象
class A:
    # 通过这个属性来判断是否生成了一个对象
    a_intance=None
    # 生成对象
    def __new__(cls):
        if cls.a_intance is None:
            # 生成对象
            cls.a_intance = super().__new__(cls) # super()是超继承，super()指的A类的父类，调用A类的父类的__new__方法
            # cls.a_intance = A.__new__(cls) # 不能用A.__new__(cls)，不然会循环一直直接调用A中的__new__方法
            return cls.a_intance
        else:
            return cls.a_intance
    def __init__(self):
        pass
print(A()) # 不管创建多少个对象，都是指的同一个对象
print(A()) # 不管创建多少个对象，都是指的同一个对象
print(A()) # 不管创建多少个对象，都是指的同一个对象















