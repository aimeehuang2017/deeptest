#coding:utf-8

__author__ = 'Aimee'

import unittest
import requests
import json

from interface.public import base
from interface.public import HttpService

class PostDateTest(unittest.TestCase):
    def setUp(self):
        #引用封装的函数
        endpoint = 'post'
        self.url = base.get_host(endpoint)

    def test_post_data_1(self):
        params = {'show_env': 1}
        data = {'aa': 'aimee', 'bv': '学测试'}
        #发送请求
        #引用封装的类
        DataALL = {'params': params, 'data': data}
        # resp = HttpService.MyHTTP(self.url).post(self.url, **DataALL)

        # 引用再次封装的函数
        Method = 'post'
        resp = base.get_response(self.url, Method, **DataALL)

        # r = requests.post(self.url,params=params,data=data)
        # resp = r.json()

        #断言
        form = resp['form']['aa']
        # self.assertEqual(forme,'aimee')
        self.assertIn('aimee',form)

    def tearDown(self):
        pass

if __name__ == "__main__":
        unittest.main()

