# _*_ coding:utf-8 _*_
# @Time    :2019/10/24 11:32
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :invest_datas.py

# 投资成功
success={'money':1000}

# 投资失败投标置灰，非100整数倍且大于100，非100整数倍且小于100，字母，符号
no10=[{'money':456,'check':'请输入10的整数倍'},
      {'money':54,'check':'请输入10的整数倍'},
      {'money':'a','check':'请输入10的整数倍'},
      {'money':'$','check':'请输入10的整数倍'},
      ]

# 投资失败弹框提示，负数100整数倍金额，0，空格，100整数倍且小于100，投标的
wrong_format_money=[{'money':-10,'check':'请正确填写投标金额'},
      {'money':0,'check':'请正确填写投标金额'},
      {'money':' ','check':'请正确填写投标金额'},
      {'money':50,'check':'投标金额必须为100的倍数'},
      ]





















