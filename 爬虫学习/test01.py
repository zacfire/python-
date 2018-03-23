from urllib import request

if __name__ =="__main__":
    req=request.Request("https://www.bilibili.com/")
    request=request.urlopen(req)
    print("geturl打印信息：%s"%(request.geturl()))
    print('*******************************************')
    print("info打印信息：%s"%(request.info()))
    print('*****************************************')
    print("getcode打印信息：%s"%(request.getcode()))