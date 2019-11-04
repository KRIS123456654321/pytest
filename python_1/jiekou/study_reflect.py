# _*_ coding:utf-8 _*_
# @Time    :2019/6/24 18:29
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :study_reflect.py

class People:
    number_eye=2 # 类属性
    def __init__(self,name,age):
        self.name=name # 对象属性，不同的对象，name属性值不同
        self.age=age # 对象属性，不同的对象，age属性值不同

if __name__ == '__main__':
    p=People('mongo',18)
    # print(People.number_eye) # 类引用
    # print(p.number_eye) # 实例化对象引用
    # print(p.name) # 实例化对象引用

# 类的反射：可以动态的查看 增加 删除 更改类或实例的属性
# 判断是否有某属性
print(hasattr(People,'number_leg')) # False，判断是否有number_leg这个属性，如果有返回True，如果没有返回False
print(hasattr(People,'number_eye')) # True，判断是否有number_leg这个属性，如果有返回True，如果没有返回False
# 添加类属性number_leg，如果有该类属性，则会覆盖属性的值，如果没有，则会添加这个属性
setattr(People,'number_leg',2)
print(hasattr(People,'number_leg')) # True
print(People.number_leg) # 2
# 添加实例属性dance，如果有该实例属性，则会覆盖属性的值，如果没有，则会添加这个属性
setattr(p,'dance',True)
print(p.dance) # True
# 获取类属性
print(getattr(People,'number_leg')) # 2，如果没有这个属性，则会报AttributeError错
# 获取实例属性
print(getattr(p,'dance')) # True，如果没有这个属性，则会报AttributeError错
# 删除实例属性
delattr(p,'dance')
# print(getattr(p,'dance')) # 会报错，前面已经把dance属性删除了













