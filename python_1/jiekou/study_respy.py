# _*_ coding:utf-8 _*_
# @Time    :2019/6/24 11:07
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :study_respy.py

# 开始引用正则表达式：
# 原因：加标接口的表格中有3个标识，在测试用例中就分3个if判断了3个标识，这种方式不好，因为如果有100个标识，不可能去写100个判断，这样的代码显然是不好的，
# 解决方式：找到相同的地方，然后使用正则表达式来进行判断

# 正则表达式：匹配一系列符合某个句法规则的字符串
# 分为原本字符、元字符
# 原本字符：原来是什么样，就定义为什么样，与我们在字符串或字典等中查找是一样的

# 解析正则表达式的模块：re，这个是python自带的

# 解析正则表达式的过程就是查找，如果找到则返回找到的信息，如果没有找到，则返回None

# search方法表示只要找到就返回，只找第一个，如果找到则返回的是Match object，如果没有找到则返回的是None，
# search方法中的参数：pattern-要匹配的正则表达式, string-在哪个数据上进行匹配, flags表示匹配模式，如是否区分大小写等

# findall方法表示找到所有符合条件的再返回，如果找到则返回的是列表，如果没有找到则返回的是空列表[]，
# findall方法中的参数：pattern-要匹配的正则表达式, string-在哪个数据上进行匹配, flags表示匹配模式，如是否区分大小写等

# match方法：表示从字符串的开头位置开始匹配，只要找到就返回，只找第一个，如果找到则返回的是Match object，如果没有找到则返回的是None
# match方法中的参数：pattern-要匹配的正则表达式, string-在哪个数据上进行匹配, flags表示匹配模式，如是否区分大小写等

# 原本字符：原来是什么样，就定义为什么样，与我们在字符串或字典等中查找是一样的
# import re
# data='{"mobilephone":"normal_user","pwd":"normal_pwd","title":"normal_user"}'
# p="normal_user" # 正则表达式
# # search表示只要找到就返回，只找第一个
# m=re.search(p,data)
# print(m) # <_sre.SRE_Match object; span=(16, 27), match='normal_user'>,16表示查找的p的所在开始位置，27表示查找的p的所在结束位置，match表示所找到的正则表达式
# # findall表示找到所有符合条件的再返回，返回的是列表
# ms=re.findall(p,data)
# print(ms) # ['normal_user', 'normal_user']

# 正则表达式的规则：
# 1.()表示一个组，可以用它来标记一个表达式组的开始和结束
# 2..表示可以匹配任意单个字符，汉字，字母，符号，数字，注意单个就是一个
# 3.+表示至少匹配一次
# 4.\d表示匹配任意单个数字
# 5.?表示最多匹配一次
# 6.*表示匹配0次或者多次

# 元字符，没有使用正则表达式组()
# import re
# data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# p="#.#" # 正则表达式，.表示匹配单个的任意字符
# ms1=re.search(p,data)
# ms2=re.findall(p,data)
# print(ms1) # None
# print(ms2) # []
# p="#.*#" # 正则表达式，*表示匹配0次或者多次
# ms1=re.search(p,data)
# ms2=re.findall(p,data)
# print(ms1) # <re.Match object; span=(16, 50), match='#normal_user#","pwd":"#normal_pwd#'>
# print(ms2) # ['#normal_user#","pwd":"#normal_pwd#']
# p="#.*?#" # 正则表达式，?表示最多匹配一次
# ms1=re.search(p,data)
# ms2=re.findall(p,data)
# print(ms1) # <re.Match object; span=(16, 29), match='#normal_user#'>
# print(ms2) # ['#normal_user#', '#normal_pwd#']

# import re
# data='hello world'
# p="hello" # 正则表达式
# # match表示从字符串的开头位置开始匹配，即开头位置就得符合匹配内容，不然就找不到，会报None
# m=re.match(p,data)
# print(m) # <re.Match object; span=(0, 5), match='hello'>
# p="world" # 正则表达式
# ms=re.match(p,data)
# print(ms) # None

# 元字符，使用正则表达式组()，用它来标记一个表达式组的开始和结束，匹配时会以()外的字符开始和结束，但返回的数据不包含()外的字符内容，
# ()外的字符可写可不写，但()外的字符可以用来帮助匹配正则表达式的标识，只匹配以()外的字符开始和结束的字符
# import re
# data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# p="#(.)#" # 正则表达式，.表示匹配单个的任意字符
# ms1=re.search(p,data)
# ms2=re.findall(p,data)
# print(ms1) # None
# print(ms2) # []
# p="#(.*)#" # 正则表达式，*表示匹配0次或者多次
# ms1=re.search(p,data)
# ms2=re.findall(p,data)
# print(ms1) # <re.Match object; span=(16, 50), match='#normal_user#","pwd":"#normal_pwd#'>
# print(ms2) # ['normal_user#","pwd":"#normal_pwd']
# p="#(.*?)#" # 正则表达式，?表示最多匹配一次
# ms1=re.search(p,data)
# ms2=re.findall(p,data)
# print(ms1) # <re.Match object; span=(16, 29), match='#normal_user#'>
# print(ms2) # ['normal_user', 'normal_pwd']

# group方法：获取search方法返回对象内的内容
# 1.返回表达式和组里面的内容，这个组表示的是()内的内容，表达式表示的是整个正则表达式，包括()外的内容
# 2.只返回指定组的内容，这个组表示的是()内的内容，表达式表示的是整个正则表达式，包括()外的内容
# import re
# data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# p="#(.*?)#"
# ms=re.search(p,data)
# print(ms.group(0)) # #normal_user#，返回表达式和组里面的内容
# print(ms.group(1)) # normal_user，只返回指定组的内容

# sub方法表示可以用来查找替换数据，默认会替换所有的符合正则表达式的数据，返回替换后的数据，
# sub方法中的参数：pattern-要匹配的正则表达式, repl-替换匹配的正则表达式的数据,string-在哪个数据上进行匹配,
# count-表示查找替换的次数，默认为0，查找替换所有的，可以自己设置替换的次数,flags表示匹配模式，如是否区分大小写等

# 当表格中有多个参数化数据时，使用search方法：一个一个找，再一个一个替换，search方法返回的是对象
# 只匹配一次，替换一次
# sub方法：表示可以用来查找替换数据
# 通过获取需要参数化数据的标识，来获取配置文件中该参数对应的数据，并替换参数化数据的标识
# import re
# from jiekou.common.config import config
# data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# p="#(.*?)#"
# m=re.search(p,data)
# g=m.group(1) # 获取到参数化数据的标识
# v=config.get('data',g) # 根据key取配置文件中的值
# print(v)
# data_new=re.sub(p,v,data,count=1) # count默认为0，替换所有的符合正则表达式的字符串
# print(data_new) # {"mobilephone":"15810447878","pwd":"#normal_pwd#"},设置count为1，只替换一次，只会替换第一个#normal_user#，不会替换#normal_pwd#

# 当要匹配多次，替换多次，使用search方法和sub方法一个一个匹配并替换的循环来解决
# import re
# from jiekou.common.config import config
# data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# p="#(.*?)#"
# while re.search(p,data):
#     print(data)
#     m = re.search(p, data)
#     g = m.group(1)  # 获取到参数化数据的标识
#     v = config.get('data', g)  # 根据参数化标识取配置文件中的值
#     # 替换后的内容，继续用data来接收，方便再次循环使用
#     data = re.sub(p, v, data, count=1)  # count默认为0，替换所有的符合正则表达式的字符串
#     print(data)
# print('最后替换后的data：',data) # 最后替换后的data：{"mobilephone":"15810447878","pwd":"123456"}


















