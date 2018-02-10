#coding = utf-8
__author__ = 'Aimee'

from interface.public import Config
from interface.public import HttpService

#对请求方式参数化
def get_host(EndPoint):
    host = Config.url()
    endpoint = EndPoint
    url = ''.join([host,endpoint])
    return url

#再次封装类中的函数
def get_response(url,Method,**DataALL):
    if Method =='get':
        resp = HttpService.MyHTTP(url).get(url,**DataALL)
    elif Method =='post':
        resp = HttpService.MyHTTP(url).post(url,**DataALL)
    return resp
