# _*_ coding:utf-8 _*_
# @Time    :2019/8/15 17:39
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :mianshi_3.py

# 传入一个json串，返回一个字典，字典只取出json最底层的数据
# 如果中间有字符串也要进行处理，请以下面的数据为例，请用递归方法实现
# Json：{"a":"aa","b":['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
# 输出：
# Dic:{'a':'aa','c':'cc','d':'dd','e':'ee'}
def str_2_dict(j): # j是一个Json串
    new={}
    if type(j)==str: # 如果是字符串
        j = eval(j)
        print('str:{0}'.format(j))
    if type(j)==list: # 如果是列表
        for item in j:
            d=str_2_dict(item)
            print('list:{0}'.format(d))
            new.update(d)
            print('listnew:{0}'.format(new))
    if type(j)==dict: # 如果是字典
        for k,v in j.items():
            if type(v)==list or type(v)==dict:
                d=str_2_dict(v)
                print('dict:{0}'.format(d))
                new.update(d)
                print('dictnew:{0}'.format(new))
            else:
                new[k]=v
                print('dictnew:{0}'.format(new))
    return new # 返回一个字典
if __name__ == '__main__':
    j='{"a":"aa","b":[\'{"c":"cc","d":"dd"}\',{"f":{"e":"ee"}}]}'
    new=str_2_dict(j)
    print(new)