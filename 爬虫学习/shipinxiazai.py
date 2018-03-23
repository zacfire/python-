import re
import json
from bs4 import BeautifulSoup
from urllib import request, parse

if __name__ == '__main__':
    ip='http://www.iqiyi.com/v_19rr8cybts.html'
    get_url = 'https://www.55523355.com/index.php?url=%s' %ip

    get_movie_url= 'https://www.55523355.com/index.php'

    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
        'Referer':'https://www.55523355.com/index.php?url=%s' %ip
    }

    get_url_req = request.Request(url = get_url,headers= head)
    get_url_response = request.urlopen(get_url_req)
    get_url_html = get_url_response.read().decode('utf-8')
    bf = BeautifulSoup(get_url_html , 'lxml')

    a=str(bf.find_all('script'))

    pattern = re.compile("url:'(.+)',",re.IGNORECASE)
    url = pattern.findall(a)[0]

    get_movie_data = {
        'refres': '1',
        'url':'%s' % url
    }
    get_movie_req = request.Request(url= get_movie_url,headers= head)
    get_movie_data=parse.urlencode(get_movie_data).encode('utf-8')
    get_moive_response = request.urlopen(get_movie_url,get_movie_data)
    get_moive_html = get_url_response.read().decode('utf-8')
    print(get_movie_data['url'])