# _*_ coding:utf-8 _*_
# @Time    :2019/6/3 14:19
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :fuxi.py

# 变量：
# 1.命名要有意义
# 2.函数命名一般会有下划线_
# 3.类命名一般会以驼峰的形式，如UserName  或 userName
# 4.全局变量命名一般是全部大写，如global USERNAME,不要随意修改
# 5.eval():val函数有很大的副作用，轻易不要用
# 删除数据库，删除整个系统，做一些非常危险的攻击性行为
# eval('print("hello")')
# eval()可以把字符串转成表达式并执行，就可以利用执行系统命令，删除文件等操作
# 如：用户任意输入
# eval("__import__('os').system('ls /Users/chunming.liu/Downloads/')")
# 那么eval()之后，会发现当前文件夹文件都会展现在用户前面，这句话相当于执行了
# os.system('ls /Users/chunming.liu/Downloads/')
# 那么继续输入：eval("__import__('os').system('cat /Users/chunming.liu/Downloads/tls_asimov_cert.pem')")
# 代码都给人看了
# 再来一条删除命令，文件消失，比如：
# eval("__import__('os').system('rm /Users/chunming.liu/Downloads/车辆转发测试.png')")
# 所以用eval，一方面享受他的灵活性，同时也要注意安全性

# 面试题1：range的特性
# range():range是个类，不是函数，range是与列表非常相似的数据结构，是个可迭代的对象
# print(type(range(1,2))) # <class 'range'>

# 数据类型：
# 1.str：字符串是不可变类型，即不能修改字符串的某个值
# str='myclass'
# # str[2]='s'  # 会报错
# 2.int
# 3.float
# 4.boolean：条件判断或者逻辑控制的依据，多种运算形式的返回值，如if while语句等都是判断真假的
# 5.list：有顺序的容器，可变类型
# 6.dict：没有顺序的，可变类型
# 7.tuple：经常用来解包，只有一个元素要加逗号，如(1,)，不可变类型

# 面试题2：可以修改字符串的数据吗？
# 字符串是不可变类型，即不能修改字符串的某个值
# str='myclass'
# # str[2]='s'  # 会报错

# 逻辑控制，流程控制，控制流程：
# 条件：if ...elif...else:
# 遍历：for...in...:
# while：continue  break

# 函数：
# 1.参数：形式参数 实际参数 位置参数 关键字 默认参数 动态参数
# *args  **kwargs,,可以自己命名为*a  **b **kw,,
# 2.返回值：return 默认为None
# 3.作用：1.用来封装一段可以重复运行的代码  2.可以提供代码的可读性

# 面试题3：可变参数作为函数的默认值，写出结果并提出改进计划
# 可变类型：list dict ,不可变类型：str int float tuple
# def add(a,mylist=[]): # 列表mylist会存放在__defaults__里面，所以后面继续添加的时候，就会在存放的mylist的基础上往后添加
#     mylist.append(a)
#     return mylist
# # 列表mylist会存放在__defaults__里面，所以后面继续添加的时候，就会在存放的mylist的基础上往后添加
# print(add.__defaults__) # ([],),一开始是空列表
# print(add(4)) # [4]，这里默认参数已经变成了[4]
# print(add.__defaults__) # ([4],)
# print(add(5)) # [4,5]，因为默认参数已经变成了[4]，再加5，就变成了[4,5]
# print(add(6,['a'])) # ['a',6],这里传了实际参数mylist，所以mylist变成了['a']，再加6，就变成了['a',6]
# print(add.__defaults__) # ([4, 5],)
# print(add(7)) # [4,5.7]，因为之前默认参数已经变成了[4,5]，再加7，就变成了[4,5,7]

# 改进计划1：
# 调用的时候传实际参数:
# def add(a,mylist=[]):
#     mylist.append(a)
#     return mylist
# print(add(1,[]))  # [1]，传入[]作为mylist的实际参数
# print(add(8,[])) # [8]，传入[]作为mylist的实际参数

# 改进计划2：在函数中判断mylist是不是空列表，如果是则新定义一个mylist为空的变量，这里新定义的mylist，
# 包括后面操作的mylist，都是这是新定义的mylist，而不是函数中的默认参数
# def add(a,mylist=[]):
#     if not mylist: # 改进的代码，如果mylist为空,则走if，if mylist表示mylist不为空则走if，所以if not mylist表示mylist为空则走if
#     # 调用这个函数时，如果不传mylist的值，那么mylist变成了[]，所以就会走这个if语句
#         mylist=[] # 新定义一个变量名为mylist，值为[]，这里的mylist与函数中的mylist不是同一个变量
#     mylist.append(a) # 这里操作的是新定义的mylist
#     return mylist  # 这里操作的是新定义的mylist
# print(add.__defaults__) # ([],)
# print(add(4)) # [4]
# print(add.__defaults__) # ([],)
# print(add(5)) # [5]
# print(add(6,['a'])) # ['a',6]
# print(add.__defaults__) # ([],)
# print(add(7)) # [7]

# 改进计划3：在改进计划2的基础上，把函数中mylist的默认值改为None，把可变参数列表变为不可变参数
# def add(a,mylist=None):
#     if not mylist:
#         mylist=[]
#     mylist.append(a)
#     return mylist
# print(add.__defaults__) # (None,)
# print(add(4)) # [4]
# print(add.__defaults__) # (None,)
# print(add(5)) # [5]
# print(add(6,['a'])) # ['a',6]
# print(add.__defaults__) # (None,)
# print(add(7)) # [7]

# if not功能解析：
# 字符串为空  整数为0  list为[]  None  dict为{} tuple为()
# a=0
# if not a: # 如果a为空，则走if
#     print("a为空")

# 类和对象：
# 1.__init__：初始化函数，会自动调用__new__创建并返回一个对象给__init__中的self
# 2.__new__：新建一个对象
# 3.类属性和实例属性


# 面试题4：__init__与__new__的区别
# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         return cls

# 面试题5：实现一个单例模式，这个类只能初始化一个对象
# 通过控制对象的生成，即控制__new__方法
# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         pass
# print(Movie('琅琊榜')) # None，修改__new__方法，不生成对象，返回的是None

# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
#     # def __new__(cls, *args, **kwargs):
#     #     pass
# print(Movie('琅琊榜')) # <__main__.Movie object at 0x004B9F50>，不修改__new__方法，生成对象

# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         return cls
# print(Movie('琅琊榜')) # <class '__main__.Movie'>,修改__new__方法，生成类

# 面试题6：类属性和实例属性
# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
# print(Movie('琅琊榜').workers) # []，对象属性
# print(Movie.workers) # ['导演', '演员']，类属性

# class Movie:
#     # workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
# print(Movie('琅琊榜').workers) # []，对象属性
# # print(Movie.workers) # 报错，类属性

# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         # self.workers = []
#         self.name = name
# print(Movie('琅琊榜').workers) # ['导演', '演员']，对象属性
# print(Movie.workers) # ['导演', '演员']，类属性

# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
# # 下面创建的对象都不是同一个对象
# # 新建第一个对象Movie('琅琊榜')
# print(Movie('琅琊榜').workers) # []，对象属性
# print(Movie.workers) # ['导演', '演员']，类属性
# # 新建第二个对象Movie('琅琊榜') ，与上面的一不是同一个对象
# Movie('琅琊榜').workers=['导演']
# # 新建第三个对象Movie('琅琊榜') ，与上面的一和二都不是同一个对象
# print(Movie('琅琊榜').workers) # []，对象属性
# print(Movie.workers) # ['导演', '演员']，类属性
#
# class Movie:
#     workers = ['导演', '演员']
#     def __init__(self, name):
#         self.workers = []
#         self.name = name
# movie=Movie('琅琊榜')
# # 下面的movie都是同一个对象
# print(movie.workers) # []，对象属性
# print(Movie.workers) # ['导演', '演员']，类属性
# # 修改movie对象的workers值
# movie.workers=['导演']
# # 输出修改后workers的值
# print(movie.workers) # ['导演']，对象属性

# os.path 路径

# 异常处理: try...except Exception as e...
# 捕获异常和抛出异常的关系
# try:
#     1/0
#     print('没出错')
# except Exception as e: # 捕获异常
#     print('出错了')
#     raise # 抛出异常

# 文件处理：打开文件后一定要关闭文件
# openpyxl模块：打开文件，最后要close()
# 第一种关闭：close()
# wb=open('file','r',encoding='utf-8')
# wb.close()

# 第二种关闭：try...except...finally,在最后的finally中关闭close()
# try:
#     wb = open('file', 'r', encoding='utf-8')
# except Exception as e: # 捕获异常
#     print('出错了')
#     raise # 抛出异常
# finally:
#     wb.close()

# 第三种关闭：上下文管理器
# with open(...) as filename:
#     pass

# logging日志：loggere

#  配置文件

# 单元测试unittest：
# TestCase--创建用例   TestSuite--收集用例容器   loader--添加模块，类
# addTest--添加对象  TextTestRunner  HTMLTestRunner

# ddt：测试用例方法名要test开头
# @ddt.ddt--装饰类   @ddt.data(*)--装饰测试用例   @ddt.unpack--装饰测试用例

# Excel：1.workbook  2.sheet  3.cell,对象，要通过cell.value取值，要字符串进行转换




























