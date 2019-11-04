# _*_ coding:utf-8 _*_
# @Time    :2019/10/21 18:14
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :combat-2.py

# PO模式--PageObject:
# 测试用例 = 页面对象 + 测试数据，
# 测试用例与测试对象分离，测试对象就是页面，分层设计
# 测试对象层：元素定位发生变化，页面功能变化或在新增，只要函数名称没变，参数没变，都不需要改测试用例，测试用例的调用方式还是一样的
# 测试用例层：用例步骤、用例数据、测试数据发生变化，不需要改测试对象
# 容易维护，容易扩展

# 写web用例的原则：
# 1.稳定性最重要，可以牺牲时间来提高稳定性（每一条用例都要打开一次浏览器，有点浪费时间，但是自动化是先追求稳定再考虑时间）
# 2.用例要保持独立性,不依赖与其它的用例运行结果（不能因为上一条用例失败，导致下一条用例也失败）
# 3.如果用例的流程很长,可以拆成几个用例,它就不独立（如：审批，申请人-审核1-审核2-审核3）
# 4.尽量少的依赖环境数据（在任何情况下，都自给自足，自己创建条件）
# （1.防止环境变更，导致数据不可用 2.数据库数据被清理，导致数据没有了）


# PageLocators（元素定位层）用于PageObjects（页面对象层）
# PageObjects（页面对象层）用于TestCases（测试用例层）
# TestDatas（测试数据层）用于TestCases（测试用例层）

# 分成设计思想：
# 元素定位层-按照页面来分不同模块写
# 页面对象层-按照页面来分不同模块写
# 测试用例层-按照页面来分不同模块写
# 测试数据层-按照页面来分不同模块写

# 初衷和目的：解放双手，解放时间，提高反馈效果
# 应用场景：冒烟（正常场景，不一定要有断言，只要跑通了就行）
#           回归（全面覆盖-异常场景(有的准备工作很多很麻烦，清理工作也很多，甚至需要人为干预)）

# UI自动化一般都是做正常场景+好实现的异常场景，稳定性好的
# 接口自动化一般是要全部做

# 清理数据一般是通过接口去清理

























