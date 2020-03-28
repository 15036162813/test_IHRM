# 登录接口测试执行脚本

# 导包
import requests
import unittest
import logging
from api.login_api import loginApi
import app
from utils import assert_commit_utils

# 创建一个配置类
class loginConfig:
    HEADERS = {"Content-Type": "application/json"}


# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        # 实例化loginApi
        self.login_api = loginApi()

    def tearDown(self):
        pass

    # 编写测试函数
    # 登陆成功
    def test01_login_success(self):
        jsonData = {"mobile":"13800000002","password":"123456"}
        # HEADERS = {"Content-Type":"application/json"}
        # logging.info("app中HEADERS是什么:{}".format(app.HEADERS))
        response = self.login_api.login(jsonData,app.HEADERS)
        # 利用日志模块打印登录结果(首先要导入日志模块)
        logging.info("登陆的结果为:{}".format(response.json()))
        # 断言登录的响应状态码,success,code,message
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True,response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功",response.json().get("message"))

        #  向assert_commit_utils()函数中传递数据
        assert_commit_utils(self,response,200,True,10000,"操作成功")
    # 密码错误
    def test02_password_is_error(self):
        jsanData = {"mobile":"13800000002","password":"1234567"}
        # 利用封装的登录接口,发送登录请求,注意: 需要传递的参数
        response = self.login_api.login(jsanData,app.HEADERS)
        # 利用日志模块打印响应数据(前提是导入日志模块)
        # 注意要将数据初始化  .format()
        logging.info("相应数据为:{}".format(response.json()))
        # 断言数据: 状态响应码,success,code,message

        # 向assert_commit_utils()函数中传递数据
        assert_commit_utils(self,response,200,False,20001,"用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exist(self):
        jsonData = {"mobile":"1380000000212","password":"123456"}
        # 利用封装的登录请求接口,发送登录请求,注意:传递的参数
        response = self.login_api.login(jsonData,app.HEADERS)
        # 利用日志模块打印响应数据
        logging.info("相应数据为:{}".format(response.json()))
        # 断言数据: 状态响应码,success,code,message

        # 向app中的assert_commit_utils()函数传递数据
        assert_commit_utils(self,response,200,False,20001,"用户名或密码错误")
        pass
    # 输入的手机号码有英文字符
    def test04_mobile_has_eng(self):
        jsonData = {"mobile":"13a800000002","password":"123456"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData,app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self,response,200,False,20001,"用户名或密码错误")
        pass
    # 手机号码有特殊字符
    def test05_mobile_has_special(self):
        jsonData = {"mobile": "13@#$2800000002", "password": "123456"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 20001, "用户名或密码错误")
        pass
    # 手机号码为空
    def test06_mobile_is_empty(self):
        jsonData = {"mobile": "", "password": "123456"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 20001, "用户名或密码错误")
        pass
    # 密码为空
    def test07_password_is_empty(self):
        jsonData = {"mobile": "13800000002", "password": ""}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 20001, "用户名或密码错误")
        pass
    # 多参-多出1个参数
    def test08_more_params(self):
        jsonData = {"mobile": "13800000002", "password": "123456","sign":"123123"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, True, 10000, "操作成功")
        pass
    # 少参-缺少mobile
    def test09_less_mobile(self):
        jsonData = { "password": "123456"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 20001, "用户名或密码错误")
        pass
    # 少参-缺少password
    def test10_less_password(self):
        jsonData = {"mobile": "13800000002"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 20001, "用户名或密码错误")
        pass
    # 无参
    def test11_none_params(self):
        jsonData = None
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")
        pass
    # 错误参数--输入错误的参数
    def test12_params_is_error(self):
        jsonData = {"mobiile": "13800000002","password":"123456"}
        # 利用封装好的登录接口,发送登录请求,注意: 传递的参数
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印响应体数据(先导入日志模块)
        logging.info("响应体数据:{}".format(response.json()))
        # 断言数据: 响应状态码,success,code,message
        # 向封装的 assert_commit_utils()函数传递数据进行断言
        assert_commit_utils(self, response, 200, False, 20001, "用户名或密码错误")
        pass