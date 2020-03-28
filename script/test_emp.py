# 按照设计顺序编写员工模块的增删改查场景测试用例脚本


# 导包
import unittest
import logging
import requests
from api.login_api import loginApi
import app
from utils import assert_commit_utils
from api.emp import EmpApi


# 创建测试类
class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = loginApi()
        # 实例化empApi对象
        self.emp_api = EmpApi()
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
        pass

    def tearDown(self):
        pass

    # 编写测试用例: 员工的增删改查
    def test01_test_emp_operation(self):
        # 1.实现登录接口(操作员工的前提)
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # 获取登录接口返回json格式响应数据
        logging.info("响应数据:{}".format(response.json()))
        # 提取响应数据中的令牌,并保存到请求头
        token = response.json().get("data")
        logging.info("令牌是:{}".format(token))
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("请求头是:{}".format(headers))

        # 2.实现添加员工接口
        response = self.emp_api.add_emp("无敌的沙福林达人02","15899009981",headers)
        # 打印添加员工的URL
        logging.info("添加员工URL:{}".format(self.emp_api.emp_url))
        # 获取到的员工返回的json数据
        add_result = response.json()
        logging.info("查询添加的员工信息为:{}".format(add_result))
        # 把员工id提取出来,并保存到变量
        emp_id = add_result.get("data").get("id")
        logging.info("员工id为:{}".format(emp_id))
        self.assertIn("操作成功", add_result.get("message"))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self,response,200,True,10000,"操作成功")

        # 3.实现查询员工接口
        # 把员工ID拼接到URL中,组成查询员工所需要的url
        response = self.emp_api.query_emp(emp_id,headers)
        logging.info("查询员工信息:{}".format(response.json()))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self, response, 200, True, 10000, "操作成功")

        # 4 实现修改员工接口
        #   把员工id拼接到url中，组成修改员工所需要的URL
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(emp_id,"无敌的沙福da",headers)
        # 打印修改员工的结果
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self, response, 200, True, 10000, "操作成功")

        # 5 实现删除员工接口
        delete_emp_url = self.emp_url + "/" + emp_id
        # 打印删除员工的URL
        # logging.info("删除员工的URL为：{}".format())
        # 发送删除员工接口请求
        response = self.emp_api.delete_emp(emp_id,headers)
        # 打印删除员工的结果
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self, response, 200, True, 10000, "操作成功")