from urllib import request
from urllib import parse
import json
import time
import random
import hashlib

content=input('请输入要翻译的句子：')

if __name__=="__main__":
    #对应上图的Request URL
    Request_URL="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    Form_Data={}

    u='fanyideskweb'
    d=content
    f=str(int(time.time()*1000)+random.randint(1,10))
    c='rY0D^0\'nM0}g5Mm1z%1G4'

    sign=hashlib.md5((u+d+f+c).encode('utf-8')).hexdigest()


    Form_Data['taye']='AOTO'
    Form_Data['i']= content
    Form_Data['doctype']= 'json'
    Form_Data['Version']= '2.1'
    Form_Data['salt']=f
    Form_Data['sign']=sign
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['ue']='ue:UTF-8'
    Form_Data['action'] = 'FY_BY_REALTIME'
    #使用urlencode方法转换标准格式
    data=parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    request=request.urlopen(Request_URL,data)
    #读取信息并解码
    html=request.read().decode('utf-8')
    #使用json
    translate_results=json.loads(html)
    #打印翻译结果
    print('翻译结果是：%s'% translate_results)

