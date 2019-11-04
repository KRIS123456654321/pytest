# _*_ coding:utf-8 _*_
# @Time    :2019/8/15 17:15
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :mianshi_2.py

# 面试编程题：
# n为任意大于1的整数
# n=5,输出：
#     *
#    ***
#   *****
#    ***
#     *
# n=6,输出：
#     *
#    ***
#   *****
#   *****
#    ***
#     *
# 编程题解析：
# 行数=输入的数
# 星号的个数
# 星号+空格=输入的数
# 前面空格个数=后面空格个数，（输入的数-星号个数)//2=单边空格个数
def print_img(n):
    # 前半部分
    for i in range(1,n+1,2):
        img = ' '*((n-i)//2)+"*"*i
        print(img)
    if n%2==0: # 偶数行
        s=n-1
    else: # 奇数行
        s=n-2
    # 后半部分
    for i in range(s,0,-2):
        img = ' '*((n-i)//2)+"*"*i
        print(img)

if __name__ == '__main__':
    # inp=input('请输入~~~')
    print_img(5)


