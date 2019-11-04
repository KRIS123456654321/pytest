# _*_ coding:utf-8 _*_
# @Time    :2019/6/18 13:51
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :json&dict.py

# 请求数据的各种数据类型&返回响应的数据类型&数据转换：

# 把字符串转换成字典：eval()、json.loads()、json()都可以
# 把字典转换成字符串：json.dumps()

# 发起请求是python，后台数据处理是java，这中间数据要进行转换，才能被python、java识别

# python数据类型与json数据格式的对应关系：
# dict--object  list、tuple--array  str、unicode--string  int、long、float--number
# True--true  False--false  None--null

# json数据格式与python的数据类型的区别：
# 1.json数据格式中所有的字符串都要用双引号
# 2.json数据格式中true、false的首字母要小写
# 3.json数据格式中空为null

# 当json数据格式与python的数据类型互相转换时，相对应的数据类型要进行转换，如json的null转换成python的None

# 入参一般用eval来转换，出参一般用json来做转换
# 在进行数据类型转换的时候，会对转换的数据中的数据类型做判断，转换成功后，数据类型就要按照当前所处的类型的格式显示
# p='{"mobilephone": "15810447878","pwd": None}' # p只是个字符串，所以里面的数据可以是None，也可以是null
# p_dict=eval(p) # 在进行转换的时候，会对转换的数据中的数据类型做判断，p中有None,所以用eval()
# print(p_dict) # {'mobilephone': '15810447878', 'pwd': None}，转换成功后，p_dict会按照当前所处的类型的格式显示

# import json
# p='{"mobilephone": "15810447878","pwd": null}'  # p只是个字符串，所以里面的数据可以是None，也可以是null
# p_dict=json.loads(p) # 在进行转换的时候，会对转换的数据中的数据类型做判断，p中有null,所以用json.loads()
# print(p_dict) # {'mobilephone': '15810447878', 'pwd': None}，转换成功后，p_dict会按照当前所处的类型的格式显示

# 把字符串转换成字典：eval()、json.loads()、json()都可以
# 把字典转换成字符串或者file：json.dumps()
# 把字符串或者file转换成字典：json.loads()

# eval()、json.loads()、json()的使用区别：
# json()：在requests模块中发起请求后的返回响应上进行转换，
# 在进行数据类型转换的时候，会对转换的数据中的数据类型做判断，转换成功后，数据类型就要按照当前所处的类型的格式显示
# 1.json()是requests模块中封装的把json形式的字符串转换成字典的方法，所以只能用在requests模块中发起请求后的返回响应上，
# 因为返回响应返回的是json形式的字符串，且在json中空为null，所以如果字符串中有空，那也是为null，不为None，
# 且json()是根据json的数据类型来做转换的，所以只能用返回响应.json(),不能用eval(返回响应)
# 2.当字符串转换成字典后，null就会变成None，因为转换后，变成了python的数据类型
# 3.json()是requests模块中封装的把json形式的字符串转换成字典的方法，所以不需要导入json
# 比如（具体可以参考上面的测试用例）：
#   resp=request.post(method,url,data)  # resp是返回响应
#   resp_dict=resp.json()  # 把json字符串转换成字典，{"status":1,"code":"10001","data":null,"msg":"登录成功"}
#   print(resp_dict)  # {'msg': '手机号不能为空', 'status': 0, 'data': None, 'code': '20103'}
#   print(resp_dict['status']) # 0

# json.loads()：不在requests模块中发起请求后的返回响应上进行转换，
# 在进行数据类型转换的时候，会对转换的数据中的数据类型做判断，转换成功后，数据类型就要按照当前所处的类型的格式显示
# 1.json.loads()是根据json的数据类型来做转换,在json中空为null，不为None，
# 所以当转换的字符串中含有None时，不能用json.loads()来转换，要用eval(),不含None时，则可以用json.loads()
# 2.当字符串转换成字典后，null就会变成None，因为转换后，变成了python的数据类型
# 3.需要导入json
# 4.json.loads()还能把file转换成字典
# 比如：
# import json
# params='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
# # params_dict=eval(params) # eval()是根据python的数据类型来做转换,在json中空为null，所以不能用eval()，要用json()
# params_dict=json.loads(params)
# print(params) # {"status":1,"code":"10001","data":null,"msg":"登录成功"}
# print(params_dict) # {'status': 1, 'data': None, 'code': '10001', 'msg': '登录成功'}
# print(params_dict['status']) # 1

# eval()：不在requests模块中发起请求后的返回响应上进行转换，
# 在进行数据类型转换的时候，会对转换的数据中的数据类型做判断，转换成功后，数据类型就要按照当前所处的类型的格式显示
# 1.eval()是根据python的数据类型来做转换,在python中空为None，不为null，
# 所以当转换的字符串中含有null时，不能用eval()来转换，要用json()，不含null时，则可以用eval()
# 2.当字符串转换成字典后，None还是None，转换前后，都还是python的数据类型
# 比如：
# import json
# params='{"status":1,"code":"10001","data":None,"msg":"登录成功"}'
# # params_dict=json.loads(params) # json.loads()是根据json的数据类型来做转换,
# # 在python中空为None，所以不能用json.loads()，要用eval()
# params_dict=eval(params)
# print(params) # {"status":1,"code":"10001","data":None,"msg":"登录成功"}
# print(params_dict) # {'status': 1, 'data': None, 'code': '10001', 'msg': '登录成功'}
# print(params_dict['status']) # 1

# 把字典转换成字符串：json.dumps()
# json.dumps()：不在requests模块中发起请求后的返回响应上进行转换
# 1.json.dumps()可以不根据json的数据类型来做转换，因为字典是python的数据类型，空为None，
# 所以也是可以用json.dumps()来转换
# 2.当字典转换成字符串后，None就会变成null，因为转换后，变成了json的数据类型
# 3.需要导入json
# 4.当字典中含有中文时，用json.dumps()转换后，中文会变成一种码
# 5.json.dumps()还能把字典转换成file
# 比如：
# import json
# params={'status': 1, 'data': None, 'code': '10001', 'msg': '登录成功'}
# params_dict=json.dumps(params)
# print(params) # {'code': '10001', 'msg': '登录成功', 'data': None, 'status': 1}
# print(params_dict) # {"code": "10001", "msg": "\u767b\u5f55\u6210\u529f", "data": null, "status": 1}
































