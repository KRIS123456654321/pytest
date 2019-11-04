# _*_ coding:utf-8 _*_
# @Time    :2019/5/21 14:42
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :class_19.py

# 什么是配置文件？？为什么要做配置文件？？：将所有的代码和配置都变成模块化可配置化，这样提高了代码的重用性，不要每次都去修改代码内部
# 如：1.好多地方都需要用同一个参数，这时最后配置化，这样改动一处就可以了
# 2.如果是就经常会变化的变量，也可以做这个配置，但要与参数化区分开
# 3.从测试环境切换到开发环境，如在数据库的配置文件中，修改host的值（IP或域名），如在ip地址的配置文件中，把IP改为要切换的环境IP
# 4.某些值取得是配置文件中的值，要修改某些值时，只有改配置文件即可，不需要改代码
# 5.配置文件与Excel之间的联系，如从配置文件中读取到要获取Excel表格中的第几行的数据，拿到是第几行

# 新建一个配置文件，配置文件是.conf或.cfg或.ini或.properties结尾，配置文件的格式如下：
# 第一步：右键--选择NEW--选择File--输入文件名.conf或文件名.cfg或文件名.ini或文件名.properties，文件类型可以有很多种，
# 就算是txt类型也可以，只要是.conf或.cfg或.ini或.properties后缀即可
# 第二步：在配置文件中，输入配置的内容，配置内容的格式是区域名（section）、键值对（options）、键值对值（value），值为字符串可以不需要引号
# [db] # db是section（即区域名、标签名），是标签的符号，里面是标签名，标签名是自己命名的，格式是标识符
# db_name='test' # 键值对，db_name是options，test是value值，db_name是自己命名的，test是字符串，可以不加引号
# db_user=python15 # 键值对，db_user是options，python15是value值
# db_passwd=python # 键值对，db_passwd是options，python是value值
# db_port=3306 # 键值对，db_port是options，3306是value值
#
# [excel] # excel是标识符，自己命名的
# excel_name=test.xlsx
# row=12
# res=True

# 后面读取的配置文件放在config.conf文件中
# config.conf文件中的内容如下：
# [db]
# db_name='test'
# db_user=python15
# db_passwd=python
# db_port=3365
# db_port_1=123.7
#
# [excel]
# excel_name=test.xlsx
# row=12
# res=True
#
# [person_info]
# name=简
# list=['男','女']

# 读取配置文件内容：要利用python自带的configparser模块引用ConfigParser这个类，这个库是自带的，不需要安装
# from configparser import ConfigParser
# cf=ConfigParser() # 实例化类

# 打开配置文件
# read()：打开配置文件，read函数的参数有文件路径、编码方式
# 相对路径：配置文件放在与当前文件同一个路径时，要用相对路径
# 绝对路径：配置文件放在与当前文件不在同一个路径时，要用绝对路径，如在当前文件的上级文件中
# 编码方式：配置文件的右下角有个编码方式，显示的编码方式是什么，也就是说你想要打开的文件是什么编码方式，
# 你去打开这个文件时就要用什么编码方式打开，这里打开配置文件的编码方式就是什么，如utf-8、gbk、二进制
# 防止配置文件中含有中文等字符
# cf.read('config.conf',encoding='gbk')

# 读取方式：所有的读取方式都是基于section来读取的
# 读取所有的section，读取的内容会放在列表中
# secs=cf.sections()
# print(secs) # ['db', 'excel', 'person_info']

# 读取某一个section下面的所有options
# 读取的内容会放在列表中
# ops=cf.options(secs[0])
# ops_1=cf.options('db') # 如果知道section的标签名，则可以直接输入标签名
# print(ops) # ['db_name', 'db_user', 'db_passwd', 'db_port', 'db_port_1']
# print(ops_1)# ['db_name', 'db_user', 'db_passwd', 'db_port', 'db_port_1']

# 读取某一个section下面的某个options具体的值
# 读取的内容不管是什么类型都会变成字符串：读取的值可以是任何类型
# opstr=cf.get(secs[0],ops[0])
# opstr_1=cf.get(secs[0],'db_user')# 如果知道options的值，则可以直接输入options的值
# print(opstr,type(opstr)) # 'test' <class 'str'>，配置文件中字符串加了引号，读取出来也会有引号，
# 这里引号是数据内容而不是作为字符串的标志
# print(opstr_1,type(opstr_1)) # python15 <class 'str'>

# 读取int类型的值：读取的值本身要是int，不然会报错
# opsint_old=cf.get(secs[0],ops[3]) # 获取到的是字符串
# opsint=cf.getint(secs[0],ops[3]) # 获取到的是int
# print(type(opsint_old),opsint_old,type(opsint),opsint) # <class 'str'> 3365 <class 'int'> 3365

# 读取布尔值类型的值：读取的值本身要是bool，不然会报错
# opsbool_old=cf.get(secs[1],'res') # 获取到的是字符串
# opsbool=cf.getboolean(secs[1],'res') # 获取到的是布尔值
# print(type(opsbool_old),opsbool_old,type(opsbool),opsbool) # <class 'str'> True <class 'bool'> True

# 读取float类型的值：读取的值本身要是int或float，不然会报错
# opsfloat_old=cf.get(secs[0],ops[4]) # 获取到的是字符串
# opsfloat=cf.getfloat(secs[0],ops[4]) # 获取到的是float
# print(type(opsfloat_old),opsfloat_old,type(opsfloat),opsfloat) # <class 'str'> 123.7 <class 'float'> 123.7

# 读取的值是列表、字典、元组等，读取出来的数据也是字符串类型
# opslist=cf.get(secs[2],'list')
# print(opslist,type(opslist)) # ['男'，'女'] <class 'str'>

# 把字符串变成列表：用eval()
# opslist_1=eval(opslist)
# print(opslist_1,type(opslist_1)) # ['男', '女'] <class 'list'>

# 利用在config_class.py模块中配置的一个类，并调用，这个模块配置的类放在“配置文件的类封装”笔记中
# from Python_PeiZhiFile.config_class import myConfig
# cf=myConfig('config.conf',encoding='gbk')
# print(cf.get_sections())

# 配置文件的作用举例：
# 1.从测试环境切换到开发环境，如在数据库的配置文件中，修改host的值（IP或域名），如在ip地址的配置文件中，
# 把IP改为要切换的环境IP，如：配置文件参考 peizhi_excel.cfg

# 2.某些值取得是配置文件中的值，要修改某些值时，只有改配置文件即可，不需要改代码，如：配置文件参考 peizhi_excel.cfg

# 配置文件与Excel之间的联系:如从配置文件中读取到要获取Excel表格中的第几行的数据，拿到是第几行
# 如：配置文件参考 peizhi_excel.cfg
# from openpyxl import load_workbook
# from Python_PeiZhiFile.config_class import myConfig
# class OpenpyxlLoad:
#     def __init__(self,ExcelName,SheetName):
#         self.ExcelName=ExcelName
#         self.SheetName=SheetName
#     def ReadData(self):
#         wb = load_workbook(self.ExcelName)
#         sheet=wb[self.SheetName]
#         line = myConfig('peizhi_excel.cfg', encoding='gbk').get_strValue('LINENO', 'line')
#         print(line)
#         B_list=[]
#         for i in range(1, sheet.max_row + 1):  # 控制行 5
#             S_list = []
#             for j in range(1, sheet.max_column + 1):  # 控制列 4
#                 S_list.append(sheet.cell(i, j).value)
#             B_list.append(S_list)
#         final_list=[]
#         if(line=='all'):
#             final_list=B_list
#         else:
#             for i in eval(line):
#                 final_list.append(B_list[i-1])
#         wb.close()
#         return final_list
#     def WriteData(self,hang,lie,date):
#         wb = load_workbook(self.ExcelName)
#         sheet=wb[self.SheetName]
#         sheet.cell(hang,lie,date)
#         wb.save(self.ExcelName)
#         wb.close()
#
# if __name__ == '__main__':
#     OpenpyxlLoad_class=OpenpyxlLoad('python_1bb.xlsx','Sheet')
#     OpenpyxlLoad_class.WriteData(1,2,'345')
#     B_list=OpenpyxlLoad_class.ReadData()
#     print(B_list)

# 如：配置文件参考 peizhi_excel.cfg
# peizhi_excel.cfg配置文件的内容如下：
# [DB]
# host=120.24.235.106
# username=python
# password=python666
# db_name=test
# port=3306
#
# [IP]
# # 测试环境
# ip=119.89.0.45
# # 开发环境
# # ip=119.89.0.66
#
# [LINENO]
# # 控制读取指定行的数据，all表示读取所有行，否则读取指定的行数
# line='all

# 总结：
# 1.为什么要用配置文件？
# 如接口自动化--配置数据库参数/配置用例的运行模式/服务器地址
# 2.配置文件的表达
# 文件格式：.cfg/.conf/.ini/.properties(文件类型可以不一样，只要后缀名是.cfg/.conf/.ini/.properties)
# 编写格式：section  option value，section-区域/块/标签名-格式：[section名字]
# 在section之下：option=value
# 可以有多个section，换行区分
# 3.读取配置数据：用的模块-configparser的ConfigParser类
#    实例化ConfigParser类：cf=ConfigParser()
#    加载配置文件：cf.read(文件名称,编码方式)
#    获取配置数据：获取sections：cf.sections()
#                  获取options：cf.options()
#                  获取value：str/int/bool/float
#                             get(section,option)

