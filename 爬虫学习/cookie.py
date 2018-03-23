# -*- coding: UTF-8 -*-

from urllib import request
from http import cookiejar

if __name__ == "__main__":

    #设置保存cookie的文件，同级目录下的cookie.txt
    filename='cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie,写入文档
    cookie = cookiejar.MozillaCookieJar(filename)
    cookie.save(ignore_discard=True, ignore_expires=True)
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器
    handler=request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    #此处的open方法打开网页
    response = opener.open('https://wx.zsxq.com/dweb/#')
    #打印cookie信息
    print(response.read().decode('utf-8'))

