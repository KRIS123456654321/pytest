# _*_ coding:utf-8 _*_
# @Time    :2019/5/26 11:17
# @Author  :xiuhong.guo
# @Email   :892336120@qq.com
# @File    :study_log.py

# 日志：记录程序代码的操作记录，通过日志来查看并定位报错的地方是什么问题
# 用来写日志的模块：logging，，logging模块是python自带的
# log的等级：debug(平常的dubug，非常简单的debug信息)->info(打印信息，相当于print信息)->warning(警告信息)->
# error(错误信息)->critical/fatal(致命的严重的崩溃的信息)，从左到右的等级越来越严重,一般都用critical不用fatal

# 错误示范：比如新建一个名为logging.py的文件，在import logging的时候，会误以为是导入自己创建的logging文件，
# 而导致不能正常使用python自带的logging模块，然而就算这时把logging.py文件的名字改掉，也会仍然报错，
# 因为py脚本每次运行时均会生成.pyc文件；在已经生成.pyc文件的情况下，去修改该文件中的某个东西时，
# 包括代码、文件名等，若代码不更新，运行时依旧会走pyc，所以要删除.pyc文件，重新打开pycharm，再重新运行代码；
# 或者重新新建一个python文件，把logging.py文件里面的代码复制到新建的python文件中，重新运行

# 日志有2个模块：收集（有5种）  输出（有3种）
# 收集（有5种）:啥都收,debug info warning error critical/fatal都收
# 收集中有日志收集器root,或者说是最高级的日志收集器/默认的日志收集器/官方的日志收集器
# import logging
# logging.debug('this is a debug msg') # 不会输出,默认只输出info以上级别,不包含info
# logging.info('this is a info msg') # 不会输出,默认只输出info以上级别,不包含info
# logging.warning('this is a warning msg') # WARNING:root:this is a warning msg,会输出,默认在console打印
# logging.error('this is a error msg') # ERROR:root:this is a error msg,会输出,默认在console打印
# logging.critical('this is a critical msg') # CRITICAL:root:this is a critical msg,会输出,默认在console打印
# 输出（有3种）:只输出info级别以上的,不包含info,即只输出warning error critical/fatal
# 输出中有输出渠道:1.控制台console  2.指定文件file  ,默认是在console打印
# 输出默认的输出级别是只输出info级别以上的,不包含info,即只输出warning error critical/fatal
# 输出的内容比如：
# WARNING:root:this is a warning mesg
# ERROR:root:this is a error mesg
# CRITICAL:root:this is a critical mesg

# 上面的日志内容是log自带的日志收集器和输出渠道，但有的时候我们会想要用别的日志收集器，收集级别，输出渠道，
# 输出级别，指定输出文本渠道，输出文本级别，指定输出格式，那么就要自己定义一个日志收集器，收集级别，输出渠道，
# 输出级别，指定输出文本渠道，输出文本级别，指定输出格式，不自己定义这些，则用的是上面log默认的
# 先新建日志收集器和收集级别，运行后默认输出到console里面,输出的级别按默认的级别来，只输出warning error critical/fatal
# 可以加上输出渠道和输出渠道的级别，再把日志收集器和输出渠道进行拼接，运行后默认输出到console里面,
# 输出的级别取收集级别和输出级别交集，如debug和info的交集是info以及info级别以上,包括info
# 也可以再加上指定输出文本渠道和输出文本渠道的级别,再把日志收集器和指定输出文本渠道进行拼接，
# 运行后默认输出到指定输出文本渠道里面，输出的级别取收集级别和指定输出文本渠道级别交集

# 新建日志收集器  设置日志收集器的级别：
# import logging
# my_logger=logging.getLogger('py15') # 新建名为py15的日志收集器
# my_logger.setLevel('INFO') # 设定收集的级别,这里的INFO可以小写info

# 指定格式：一般日志需要指定级别 时间 信息等日志信息，输出的时候设置格式
# fmt=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s') # 创建输出格式

# 新建输出渠道  设置输出渠道的级别：默认输出到console控制台，取的收集级别和输出级别交集
# ch=logging.StreamHandler() # 新建输出渠道
# ch.setLevel('ERROR') # 设定输出的级别,这里的DEBUG可以小写debug
# ch.setFormatter(fmt) # 把输出格式设置到输出渠道中来设置输出渠道的格式

# 指定输出文本渠道  输出的渠道级别：这里指定到文本中，运行后如果指定的文本不存在则会新建一个文本并输出到该文本中，
# 如果存在，则会输出到该文本中，每一次运行，日志都会往该文本中添加日志内容，不会清除掉之前的，
# 取的收集级别和指定输出文本级别交集，这里可以指定多个输出文本渠道，注意后面要建立日志收集器和指定输出文本渠道的配合关系
# file_handler=logging.FileHandler('py15.log',encoding='utf-8') # 指定输出文本渠道，传编码格式参数，
# 防止中文在py15.log中出现乱码
# file_handler.setLevel('DEBUG') # 设定指定输出文本渠道的级别,这里的ERROR可以小写error
# file_handler.setFormatter(fmt) # 把输出格式设置到设置指定输出文本渠道中来设置指定输出文本渠道的格式

# 日志收集器和输出渠道  日志收集器和指定输出文本渠道建立配合关系：
# my_logger.addHandler(ch)  # 建立日志输出到控制台，取的收集级别和输出级别交集
# my_logger.addHandler(file_handler)  # 建立日志输出到指定的文本中，取的收集级别和指定输出文本级别交集

# 输出日志：不加指定格式的输出为this is a error msg，
# 加上指定格式的输出为2019-05-25 16:50:30,165-ERROR-study_log.py-py15-日志信息:this is a error msg，
# 日志信息显示哪些内容，是根据前面创建的指定格式控制的
# my_logger.debug('this is a debug msg') # 取的收集级别和输出级别交集则不输出在concole，取得收集级别和指定文本级别的交集则不输出在指定文本中
# my_logger.info('this is a info msg') # 取的收集级别和输出级别交集则输出在concole，取得收集级别和指定文本级别的交集则不输出在指定文本中
# my_logger.warning('this is a warning msg') # 取的收集级别和输出级别交集则输出在concole，取得收集级别和指定文本级别的交集则不输出在指定文本中
# my_logger.error('this is a error msg') # 取的收集级别和输出级别交集则输出在concole，取得收集级别和指定文本级别的交集则输出在指定文本中
# my_logger.critical('this is a critical msg') # 取的收集级别和输出级别交集则输出在concole，取得收集级别和指定文本级别的交集则输出在指定文本中

# 指定格式的格式意思解析：
# %(relativeCreated)d:输出日志信息时的，自Logger创建以来的毫秒数
# %(asctime)s:字符串形式的当前时间，默认格式是:'2003-07-08 16:49:45,896'，逗号后面的是毫秒数
# %(levelname)s:文本形式的日志级别
# %(filename)s:调用日志输出函数的模块的文件名
# %(name)s:Logger的名字
# %(thread)d:线程ID，可能没有
# %(threadName)s:线程名，可能没有
# %(process)d:进程ID，可能没有
# %(message)s:用户输出的信息
# %(levelno)s:数字形式的日志级别
# %(pathname)s:调用日志输出函数的模块的完整路径名，可能没有
# %(module)s:调用日志输出函数的模块名
# %(funcName)s:调用日志输出函数的函数名
# %(lineno)d:调用日志输出函数的语句所在的代码行
# %(created)f:当前时间，用UNIX标准的表示时间的浮点数表示




































