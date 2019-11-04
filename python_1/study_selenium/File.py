# _*_ coding:utf-8 _*_
# @Time    :2019/10/10 18:12
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :File.py

# 上传操作：
# 第一种：如果是input可以直接输入路径，直接使用send_keys()
# 第二种：非input标签的上传，则需要借助第三方工具
# 工具1：Autolt/autoitv3，我们去调用其生成的au3或exe文件，支持pc客户端，还需要学习其语法，
# python自动化代码还得打包成exe，再去调用其exe文件，成本高，不建议使用
# 工具2：SendKeys第三方库（目前值支持到2.7版本），用的时候可能会出问题，不建议使用
# 网址：https://pypi.python.org/pypi/SendKeys
# 工具3：Python pywin32库，识别对话框句柄，进而操作，工具pywin32和spy++
# 工具4：pyautoit，与Autolt对接的python自己的库pyautoit

# 工具pywin32和spy++

# 如何安装Python pywin32？pip install pypiwin32，或者在pycharm工具中安装
# 安装定位系统控件的工具：WinSpy

# window的控件如何识别，如上传窗口？有对应的window系统工具来识别，如WinSpy
# app的控件如何识别，如上传窗口？有对应的app系统工具来识别

# 左键长按不松，然后移到想要定位的位置，识别到元素的信息后，一般通过text或class来定位

# 通过系统工具来识别，找出需要定位的元素的一层层的所有父级元素的class和text值，直到文件弹框的祖父元素，
# 然后再一层层的从祖父元素开始往下查找到要定位的元素，具体如下面的例子
# 下面的例子的层级关系是（按class值，即类名，来展示层级关系）：
# 文件输入路径：Edit->ComboBox->ComboBoxEx32->#32770
# 打开按钮：Button->#32770

# 如何结合selenium的代码一起使用？
# 在写selenium代码的模块直接引用上传文件的代码模块，然后再直接调用upload函数，在调用前要先sleep1-2秒等待上传窗口出现
# 如：
# 前面是selenium代码，并已经引用了上传文件的代码模块
# 假设点了某个元素，导致windows上传窗口出现
# import time
# time.sleep(2)
# upload("D:\\111.png")
# time.sleep(1) # 上传完后，可以等待1-2秒
# 等待元素可见
# 再进行元素操作

# 实际上selenuim是操作浏览器，win32是调用windows窗口的

# driver和windows是完全不相干的东西，你做你的事情，我做我的事情，只是会按代码的顺序来执行

import win32gui
import win32con

# 前提是：windows上传窗口已经出现，当然这里需要，sleep1-2秒等待上传窗口出现
def upload(filePath,browser_type='chrome'):
    # 不同的浏览器，上传文件的一级窗口（祖先）的文本是不一样的，谷歌的文本是“打开”
    if browser_type=='chrome':
        title='打开'
    else:
        title=''

    # 找元素，一层层的从祖父元素开始往下查找到要定位的元素
    # 一级窗口，“#32770”表示元素的class值，“打开”为元素的title值
    dialog=win32gui.FindWindow("#32770",title)
    # 二级窗口，dialog表示父级窗口，0表示从第一个子窗口开始遍历所有的子窗口，ComboBoxEx32表示元素的class值，None表示元素的text值，
    # 有值则显示值，无值则显示None
    ComboBoxEx32=win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    # 三级窗口
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    # 四级窗口，编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)
    # 四级窗口，打开按钮
    button = win32gui.FindWindowEx(dialog, 0, "Button","打开(&0)")

    # 操作
    # 往编辑当中，输入文件路径，发送文件路径
    # edit表示定位的元素，win32con.WM_SETTEXT、None都是固定的传参，filePath表示要上传的文件路径，
    # 必须是完整的文件路径，需要带上前面的哪个盘下的哪个文件下的。。。
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filePath)
    # 点击打开按钮，dialog表示定位的祖父元素，win32con.WM_COMMAND、1都是固定的传参，button表示定位的元素
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

upload("D:\\111.png")














