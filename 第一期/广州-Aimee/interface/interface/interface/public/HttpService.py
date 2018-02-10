#coding = utf-8
__author__ = 'Aimee'

import requests
import json
#类的封装
class MyHTTP():
    def __init__(self,url):
        self.url = url
    #写死了参数个数
    # def get(self,url,params,headers):
    #     resp = requests.get(url,params=params,headers=headers)
    #     text = resp.json()
    #     return text

    #   参数参数化 get 、post其他delete 和put等一样写
    def get(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        try:
            resp = requests.get(url,params=params,headers=headers)
            text = resp.json()
            return text
        except Exception as e:
            print('get错误：s%' %e)

    def post(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        data = DataALL.get('data')
        json = DataALL.get('json')
        files = DataALL.get('files')
        try:
            resp = requests.post(url,params=params,headers=headers,data=data,json=json)
            text = resp.json()
            return text
        except Exception as e:
            print('post错误：s%' %e)






