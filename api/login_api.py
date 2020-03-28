# 定义封装的登录API

import requests


class loginApi:

    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self, jsonData, headers):
        response = requests.post(url=self.login_url, json=jsonData, headers=headers)
        return response


# main 方法   防止导入模块时执行写在类外面的代码  调试用
if __name__ == '__main__':
    login_api = loginApi()
    jsonData = {"mobile": "13800000002", "password": "123456"}
    headers = {"Content-Type": "application/json"}
    response = login_api.login(jsonData, headers)
    print("登录结果为:", response.json())
