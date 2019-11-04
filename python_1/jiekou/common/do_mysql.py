# _*_ coding:utf-8 _*_
# @Time    :2019/6/27 11:52
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :do_mysql.py

# 把获取数据库的操作封装成类
import pymysql
class DoMysql:
    '''完成与MySQL数据库的一个交互'''
    def __init__(self): # 初始化，创建连接及查询页面
        host='test.lemonban.com'
        user='test'
        password='test'
        port=3306
        # 连接数据库
        self.mysql=pymysql.connect(host=host,user=user,password=password,port=port)
        # 新建游标，即新建查询页面
        self.cursor=self.mysql.cursor() # 从数据库返回的数据是个元组
        # self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 从数据库返回的数据是个字典
    def fetch_one(self,sql): # 当查询数据只有一条
        self.cursor.execute(sql)
        self.mysql.commit() # 每次执行sql，强制查询最新的数据库
        return self.cursor.fetchone() # 返回结果
    def fetch_all(self,sql): # 当查询数据有多条
        self.cursor.execute(sql)
        self.mysql.commit()  # 每次执行sql，强制查询最新的数据库
        return self.cursor.fetchall() # 返回结果
    def close(self):
        self.cursor.close() # 关闭游标，即关闭查询
        self.mysql.close() # 关闭数据库连接

if __name__ == '__main__':
    mysql=DoMysql()
    result=mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    mysql.close()
