# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error

if __name__=="__main__":
    #一个不存在的链接
    url = "http://www.ikkkkkk.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read()
    except error.HTTPError as e:
        print(e.code)