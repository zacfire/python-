# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
    #创建txt文件
    file = open('一念永恒.txt','w',encoding='utf-8')
    #一念永恒的目录地址
    target_url = 'http://www.biqukan.com/1_1094/'
    head = {}
    head[ 'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url=target_url,headers=head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建Beautifulsoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档数，找书div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果在创景一个beautifulsoup对象，对其进行解析
    down_soup = BeautifulSoup(str(chapters),'lxml')
    #计算章节数
    numbers = (len(down_soup.dl.contents)-1)/2 - 8
    index =1
    #开始记录内容标志位，只要正文卷下面的链接，最新章节列表链接剔除
    begin_flag = False
    #遍历所有dl标签下的子节点
    for child in down_soup.dl.children:
        #过滤回车
        if child != '\n':
            #找到正文卷，使用标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
            #爬取链接
            if begin_flag == True and child.a !=None:
                download_url = "http://www.biqukan.com"+child.a.get('href')
                download_req = request.Request(url=download_url,headers=head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')
                download_name = child.string
                soup_texts =BeautifulSoup(download_html,'lxml')
                texts = soup_texts.find_all(id = 'content',class_ = 'showtxt')
                soup_text= BeautifulSoup(str(texts),'lxml')
                write_flag = True
                file.write(download_name+'\n\n')
                #将爬取内容写入文件
                for each in soup_text.div.text.replace('\xa0',''):
                    if each=='h':
                        write_flag = False
                    if write_flag == True and each !='':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                file.write('\n\n')
                #打印抓取进度
                sys.stdout.write("已下载：%.3f%%"% float(index/numbers)+'\r')
                sys.stdout.flush()
                index += 1
    file.close()