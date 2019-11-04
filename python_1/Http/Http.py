# _*_ coding:utf-8 _*_
# @Time    :2019/6/10 15:51
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :port_test.py

# 项目的各个文件含义以及存放规范：
# 1.项目：指的是最前面的文件夹
# 2.主入口main：一般都会放在项目的根目录下，不会再任何包内，而是直接在项目下面，方便运行
# 如python_code就是一个项目，也是个文件夹
# 3.包：包含_ini_文件，一般用来存放各种不同功能的模块，也就是各种.py文件，可以用来区分代码功能
# 4.模块：.py文件，一般模块都是供别人使用的，如在其他模块中导入某种模块，并可以使用模块内容

# 接口：interface
# 如：USB--硬件接口   耳机--硬件接口
# www.baidu.com--不是接口
# 地址--URI：后面对应的是api（函数或类），这种地址对应的api叫做web api
# 函数--不一定是接口，只有能被外部调用的公有函数才是接口，私有函数是不能被外部调用的，所以不是接口
# 函数--APIS：Application programming interface,应用程序可编程接口
# UI--user interface，用户接口
# 相同功能：用来做适配、桥梁、中介，不同的系统之间本来是无法进行交互的，有了接口后，他们就可以沟通了

# URI与URL的区别：具体请百度
# URI = Universal Resource Identifier 统一资源标志符
# URL = Universal Resource Locator 统一资源定位符
# URN = Universal Resource Name 统一资源名称
# URI分为三种，URL or URN or （URL and URI）
# URL代表资源的路径地址，而URI代表资源的名称。
# 通过URL找到资源是对网络位置进行标识，如：
# http://example.org/absolute/URI/with/absolute/path/to/resource.txt
# ftp://example.org/resource.txt
# 通过URI找到资源是通过对名称进行标识，这个名称在某命名空间中，并不代表网络地址，如：
# urn:issn:1535-3613

# HTTP请求：自己百度吧，老师讲课太差太乱！！！
# 域名  IP地址---通过http协议来解析，http协议中有TCP/IP协议
# 把域名解析为ip

# 网页按F12，查看网络中的http请求：请求地址就是域名，远程地址就是IP地址

# 服务端：后端，处理请求，被动接收方
# 客户端：前端，发送请求，主动请求方，如浏览器，手机app，硬件

# 退货进行操作模拟HTTP请求：
# 1.填单 2.包裹 3.顺丰，申通
# 1.填单-收货地址：域名-请求地址  IP地址-远程地址
# 2.快递：请求方法，get post delete head patch options
# 3.请求头header：说明信息-请求地址 请求方法等
# 消息头中的user-agent：用户代理，如谷歌浏览器访问则是谷歌浏览器，苹果手机访问则是苹果手机
# 如果服务器不允许火狐访问，那么可以修改user-agent为谷歌，这叫做篡改消息头，在爬虫中用的很多

# 接口地址由域名地址+接口地址

# 面试题1：http协议 tcp/ip协议：三次握手  四次挥手

# 面试题2：get请求  post请求的区别
# 参考地址：https://www.cnblogs.com/logsharing/p/8448446.html

# 一封信:你到家了?  请求体

# get  请求可以包含请求参数,请求参数如同包裹

# 请求体  如同包裹

# cookie!=缓存
# cookie：http是无状态的，记性不好，记不住事，要cookie来记住
# 1.请求一个网址    派发一个会员卡 cookie
# 2.保存  浏览器会自动保存cookie  目标网站 cookie值 cookie类型
# 3.请求目标  自动带上cookie

# 响应

# 请求内容:我要去你家,给我准备10斤小龙虾
# 请求发送
# 发送回信:小龙虾已经备好
# 结果:我信是否发送出去?没有收到?不想回信?快递自己收了?
# http:不管什么结果,都会发送一个回信给请求方---响应信息,响应body主体
# 状态码(http内部管理机制):200    拿到快递--10000 装车了--10001  中转--10002
# 常见状态码:
# 200 返回正常,只能表示前端发送成功了,并不能表示这是服务器要的或者服务器处理好了,可以正常走下一步
# 304 服务端资源无变化，可使用缓存资源
# 400 请求参数不合法
# 401 未认证
# 403 服务端禁止访问该资源
# 404 服务端未找到该资源
# 500 服务端异常

# 面试题:cookie  session  token的区别
# cookie 浏览器保存在本地的信息,会保存session
# session 服务器处理的信息
# token  令牌 口令  随时带在身上  动态的  跨平台的,如小程序的token可以用来当做对应的公众号的token

# 面试题:手机端的http请求和浏览器的http请求的区别
















