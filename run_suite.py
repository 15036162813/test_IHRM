# 管理测试用例

# 导包
import time
import unittest





# 创建测试套件
from HTMLTestRunner_PY3 import HTMLTestRunner

import app
from script.test_emp2 import TestEmp
from script.test_login_params import TestLogin

suite = unittest.TestSuite()
# 在测试套件中添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))
# 定义测试报告名称
# ihrm_report_path = app.BASE_PATH + "/report/ihrm{}.html".format(time.strftime("%Y%m%d %H%M%S"))
ihrm_report_path = app.BASE_PATH + "/report/ihrm.html"
with open(ihrm_report_path,"wb") as f:
    # 实例化 HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=2, title="IHRM人力资源管理系统", description="这是使用HTMLTestRunner_PY3生成的报告")
    # 使用实例化的HTMLTestRunner运行测试套件
    runner.run(suite)