# _*_ coding:utf-8 _*_
# @Time    :2019/10/29 13:53
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :combat-4.py

# 目的：冒烟和回归

# 接口自动化不需要挑测试用例运行，需要全部运行，而且接口自动化运行的很快

# UI自动化需要挑选冒烟用例,如200个测试用例,可能只选了50个冒烟

# unittest挑选用例比较麻烦，所以这里可以使用pytest

# 使用打标签的方式来筛选

# 标签功能-pytest(单元测试框架)

# pytest:基于unittest只上的单元测试框架
# pytest和unittest的区别？
# 1.自动发现测试模块和测试方法
# 测试用例不一定要放测试类中
# 2.断言使用assert+表达式即可（表达式中加and or等）
# 3.可以设置会话级（从运行测试用例开始到结束，在main模块中会集合多个文件的测试用例）、模块级（.py文件）、类级（setupClass、teardownClass）
# 、函数（测试用例）级的fixtures（数据准备+清理工作），
# 数据准备+清理工作 就是 unittest中的前置和后置，且数据准备+清理工作不写在测试用例中，而是单独放在一个conftest.py文件中
# 可以多个测试类同用一个数据准备+清理工作
# 4.有丰富的插件库，目前在600个以上--pytest可以与很多库集成，如allure,pytest可以与allure集成，展示更多好看的测试报告，unittest不可以

# 安装pytest：pip install pytest
# 安装html报告的插件：pip install pytest-html

# pytest插件的地址：http://plugincompat.herokuapp.com/

# 还有个nose单元测试框架，用的很少
# pytest在某些情况下可以执行unittest和nose的测试用例

# pytest有个要求，所有的python模块都要放在python包中
# 只要换了文件路径、位置等，就要清掉文件中的pytest缓存，如带有pycache，pytest_cache等

# 1.自动发现测试模块和测试方法:
# 第二种：以test_开头的函数名，意思是，因为pytest中测试用例可以不放在测试类中，直接放在外面，
# 作为函数，所以这句话所识别的测试用例就是这种情况

# 在测试用例前面打标签（表示这个类中某个测试用例有打的这个标签）：
# 第一步：引入pytest--import pytest
# 第二步：在需要打标签的测试用例前面加上标签-- @pytest.mark.标记名，如@pytest.mark.smoke

# 在测试用例前面也可以打多个标签，放多个@pytest.mark.标记名即可

# 在测试类前面打标签（表示整个类中的测试用例都有打的这个标签）：
# 第一步：引入pytest--import pytest
# 第二步：在需要打标签的测试类前面加上标签-- @pytest.mark.标记名，如@pytest.mark.smoke

# pytest是有命令行的，直接在控制台处点击Terminal,输入pytest，
# 就会在当前目录下搜索测试用例，并自动运行全部测试用例

# 如何运行测试用例?
# 1.在命令行中，输入pytest -m smoke,smoke为打的标签名
# 2.写一个main模块
# if __name__ == '__main__':
#     pytest.main(["-m","smoke"])

# 运行多个标记的测试用例，如运行有标签为smoke和demo的测试用例：
# 1.pytest -m smoke and demo
# 2.if __name__ == '__main__':
#     pytest.main(["-m","smoke and deml"])
# 运行多个标记的测试用例，如运行有标签为smoke或demo的测试用例：
# 1.pytest -m smoke or demo
# 2.if __name__ == '__main__':
#     pytest.main(["-m","smoke or deml"])

# pytest的参数化不是用ddt了













