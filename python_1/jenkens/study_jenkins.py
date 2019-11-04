# _*_ coding:utf-8 _*_
# @Time    :2019/7/11 14:23
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :study_jenkins.py

# Jenkins持续集成：持续集成（Continuous integration，简称CI）指的是，频繁地（一天多次）将代码集成到主干。
# 持续集成的目的：就是让产品可以快速迭代，同时还能保持高质量，它的核心措施是，代码集成到主干之前，必须通过自动化测试，
# 只要有一个测试用例失败，就不能集成。

# Jenkins是基于 Java 开发的一种持续集成工具，用于监控持续重复的工作

# 安装jenkins的另外三种方式：
# 1.在网上下载jenkins.war包，在cmd终端，输入java -jar jenkins.war,会显示是否启动jenkins，但是如果把这行代码关掉，那么
# jenkins就会被关闭，如果想要这个服务一直启动，可以在后面加代码，具体可以百度
# 2.在网上下载jenkins.war包，放在Tomcat的APPlication文件夹中，启动Tomcat，jenkins就会启动，关闭Tomcat，jenkins就会关闭
# 3.下载pgk形式的jenkins，也就是在网上下载jenkins安装的包，把它当做windows的服务，可以在系统管理中的服务中可以看到jenkins，如果jenkins启动不了，可以
# 在服务中进行查看设置，系统管理的服务可以通过左下角的搜索输入服务找到，如同找cmd一样