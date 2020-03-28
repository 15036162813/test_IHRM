# 登录接口测试执行脚本

# 导包
import requests
import unittest
import logging
from api.login_api import loginApi
import app
from utils import assert_commit_utils, read_login_data
from parameterized import parameterized


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

    # 定义要加载的登录数据
    filename = app.BASE_PATH + "/data/login.json"

    # 编写测试函数
    # 登陆成功
    @parameterized.expand(read_login_data(filename))
    def test_login(self, case_name, jsonData, http_code, success, code, message):
        jsonData = jsonData
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录结果(首先要导入日志模块)
        logging.info("登陆的结果为:{}".format(response.json()))

        #  向assert_commit_utils()函数中传递数据
        assert_commit_utils(self, response, http_code, success, code, message)
