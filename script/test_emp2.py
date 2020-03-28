# 按照设计顺序编写员工模块的增删改查场景测试用例脚本


# 导包
import unittest
import logging
import requests
from parameterized import parameterized

from api.login_api import loginApi
import app
from utils import assert_commit_utils
from api.emp import EmpApi
from utils import read_emp_data


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
    def test01_login(self):
        # 1.实现登录接口(操作员工的前提)
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, headers=app.HEADERS)
        # 获取登录接口返回json格式响应数据
        logging.info("响应数据:{}".format(response.json()))
        # 提取响应数据中的令牌,并保存到请求头
        token = response.json().get("data")
        logging.info("令牌是:{}".format(token))
        app.HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("请求头是:{}".format(app.HEADERS))

    # 定义员工数据文件的路径
    filename = app.BASE_PATH + "/data/emp.json"





    @parameterized.expand(read_emp_data(filename,"add_emp"))
    def test02_add_emp(self,username, mobile, http_code, success, code, message):
        # 2.实现添加员工接口
        response = self.emp_api.add_emp("无敌的沙福林达人03","15899009982",app.HEADERS)
        # 打印添加员工的URL
        logging.info("添加员工URL:{}".format(self.emp_api.emp_url))
        # 获取到的员工返回的json数据
        add_result = response.json()
        logging.info("查询添加的员工信息为:{}".format(add_result))
        # 把员工id提取出来,并保存到变量
        app.EMP_ID = add_result.get("data").get("id")
        logging.info("员工id为:{}".format(app.EMP_ID))
        self.assertIn("操作成功", add_result.get("message"))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self,response,http_code,success,code,message)







    @parameterized.expand(read_emp_data(filename,"query_emp"))
    def test03_query_emp(self,http_code,success,code,message):
        # 3.实现查询员工接口
        # 把员工ID拼接到URL中,组成查询员工所需要的url
        response = self.emp_api.query_emp(app.EMP_ID,app.HEADERS)
        logging.info("查询员工信息:{}".format(response.json()))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self, response, http_code, success, code, message)




    @parameterized.expand(read_emp_data(filename,"modify_emp"))
    def test04_modify_emp(self,username,http_coed,success,code,message):
        # 4 实现修改员工接口
        #   把员工id拼接到url中，组成修改员工所需要的URL
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(app.EMP_ID,"无敌的沙福da",app.HEADERS)
        # 打印修改员工的结果
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 现在由于修改员工返回的响应数据当中，没有修改的username
        # 所有我们并不知道修改的username有没有成功
        # 那么怎么办？
        # 我们需要连接到ihrm数据库中，然后按照添加员工返回的员工id查询这个员工id对应的
        # username的值，如果数据库的username与修改的username一致，那么就证明修改成功了
        # 实际数据：数据库查询出来的数据；预期：修改的数据
        # 我们执行的SQL语句，在navicat中是查不到任何数据的，原因是因为执行完毕之后，员工被删除了
        # 如果添加员工失败，那么员工ID提取失败，也会导致查询失败

        # 导包
        import pymysql
        # 建立连接
        conn = pymysql.connect(host="182.92.81.159",user="readuser",password="iHRM_user_2019",database='ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select username from bs_user where id={}".format(app.EMP_ID)
        cursor.execute(sql)
        # 输出sql语句
        logging.info("打印SQL语句:{}".format(sql))
        # 调试执行的SQL结果
        result = cursor.fetchone()
        logging.info("执行SQL语句查询的结果为:{}".format(result))
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        # 断言数据库查询的结果
        self.assertEqual("无敌的沙福da",result[0])

        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self, response, http_coed, success, code, message)






    @parameterized.expand(read_emp_data(filename,"delete_emp"))
    def test05_delete_emp(self,http_code,success,code,message):
        # 5 实现删除员工接口
        # 发送删除员工接口请求
        response = self.emp_api.delete_emp(app.EMP_ID,app.HEADERS)
        # 打印删除员工的结果
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 调用封装的断言模块进行断言,将要进行断言的数据,按照要求传递
        assert_commit_utils(self, response, http_code, success, code, message)