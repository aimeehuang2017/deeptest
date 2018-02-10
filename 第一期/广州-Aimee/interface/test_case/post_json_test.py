#coding:utf-8
__author__ = 'Aimee'

import unittest
import requests
import json
from public import base
from public import read_excel
from public import HttpService

class PostJsonTest(unittest.TestCase):
    def setUp(self):
        # 引用封装的函数
        endpoint = 'post'
        self.url = base.get_host(endpoint)

    def test_post_json(self):
        data = {
            "employees": [
                {"firstName": "Bill", "lastName": "Gates"},
                {"firstName": "George", "lastName": "Bush"},
                {"firstName": "Thomas", "lastName": "Carter"}
            ]
        }
        #发送请求
        # r = requests.post(self.url,json=data)
        # resp = json.loads(r.text)
        #引用封装的类
        DataALL = { 'json': data}
        # resp = HttpService.MyHTTP(self.url).post(self.url, **DataALL)

        # 引用再次封装的函数
        Method = 'post'
        resp = base.get_response(self.url, Method, **DataALL)

        #断言
        employees = resp.get('data')
        self.assertIsInstance(employees,str)

    def tearDown(self):
        pass

    if __name__ =="__main__":
        unittest.main()


