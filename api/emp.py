# 封装操作员工模块的接口请求

import requests

# 创建封装的测试类
class EmpApi:
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    # 封装添加员工接口
    def add_emp(self,username,mobile,headers):
        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2020-03-16",
                    "formOfEmployment": 2,
                    "departmentName": "snowsnow",
                    "departmentId": "1226092852421177344",
                    "correctionTime": "2020-03-15T16:00:00.000Z"
                    }

        return requests.post(url=self.emp_url,
                             json=jsonData,
                             headers=headers
                             )

    # 封装查询员工接口
    def query_emp(self,emp_id,headers):
        query_url = self.emp_url + "/" + emp_id
        return requests.get(url=query_url,headers=headers)

    # 封装修改员工接口
    def modify_emp(self,emp_id,username,headers):
        # 拼接修改员工的URL
        modify_url = self.emp_url +"/"+emp_id
        jsonData = {"username":username}
        return requests.put(url=modify_url,json=jsonData,headers=headers)

    # 封装删除员工接口
    def delete_emp(self,empid,headers):
        # 拼接删除员工的URL
        delete_url = self.emp_url +"/"+empid
        return requests.delete(url=delete_url,headers=headers)