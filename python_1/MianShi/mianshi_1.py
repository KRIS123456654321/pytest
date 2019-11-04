# _*_ coding:utf-8 _*_
# @Time    :2019/8/14 18:12
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :mianshi_1.py

# 面试编程题：对用户输入的数据进行分离，把数字，字母，汉字，符号分离开
# 如：s='我的名字是ths,今年18岁'
# 第一种方式：使用string函数
import string
# print(string.digits) # 获取数字
# print(string.ascii_letters) # 获取字母
# print(string.punctuation) # 获取标点符号
# print(' '.isspace()) # p判断字符串中是否是空格
def find(s):
    digit=[]
    letter=[]
    punctuation=[]
    chinese=[]
    for ss in s:
        if ss in string.digits: # 判断是否是数字
            digit.append(ss)
        elif ss in string.ascii_letters: # 判断是否是字母
            letter.append(ss)
        elif ss in string.punctuation or ss.isspace(): # 判断是否是符号
            punctuation.append(ss)
        else:
            chinese.append(ss)
    print("数字：{0}".format(''.join(digit)))
    print("拼音：{0}".format(''.join(letter)))
    print("符号：{0}".format(''.join(punctuation)))
    print("中文：{0}".format(''.join(chinese)))
if __name__ == '__main__':
    inp=input('请输入~~~')
    find(inp)

# 第二种方式：使用正则表达式
import re
# num="\d" # 数字
# letter="[a-zA-Z]" # 字母
# chinese="[\u4e00-\u9fff]" # 汉字
# NotNum="^\D" # 非数字
def find_by(s):
    pattern ={"数字":"\d","拼音":"[a-zA-Z]","汉字":"[\u4e00-\u9fff]"}
    for k,v in pattern.items():
        ss=re.findall(v,s)
        print(k+":"+"".join(ss))
        s=re.sub(v,'',s)
    print('符号:{0}'.format(s))

if __name__ == '__main__':
    inp=input('请输入~~~')
    find_by(inp)




















