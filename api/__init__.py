# 初始化日志配置的代码放在api模块下的__init__.py
# 为什么要把初始化日志配置的代码放在这里?
# 因为: 后续我们是通过script脚本进行测试,而scrip脚本在执行是会调用api中的接口,由于在导入api模块时,会优先运行__init__.py中的代码
# 所以: 只要我们导入了api中的接口,那么就会运行__init__.py中的代码,从而自动地完成日至配置信息的初始化操作

# 把整个项目的日志模块都进行一次初始化,后续所有的代码都可以使用logging.info来打印日志

# 导入模块和相应的包
import app,logging
# 初始化日志
app.init__Logging()
# 打印初始化的结果
logging.debug("DEBUG TEST_______")
logging.info("INFO TEST==========")