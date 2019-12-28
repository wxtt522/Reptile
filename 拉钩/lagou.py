# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 08:49:38 2019

@author: Administrator
"""
import requests
import random
from pymongo import MongoClient
import time
import numpy as np
from bs4 import BeautifulSoup

# Mongo配置
conn = MongoClient('127.0.0.1', 27017)
db = conn.lagou  # 连接lagou数据库，没有则自动创建
mongo_lagou = db.job  # 使用job集合，没有则自动创建

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

headers = {'User-Agent': random.choice(user_agent),  # 随机选取头部代理
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Referer': 'https://www.lagou.com/jobs/list_python?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=&labelWords=hot'
           }

# 请求r1，获取随机代理IP
r1 = requests.get('http://47.100.21.174:8899/api/v1/proxies?limit=60').json()
# 拉勾主页
url1 = 'https://www.lagou.com/jobs/list_{}?city=%E6%9D%AD%E5%B7%9E'
# 拉勾所有职位信息
url2 = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
# 拉勾具体职位信息
url3 = 'https://www.lagou.com/jobs/{}.html'


def getInfo(url):
    headers = {'User-Agent': random.choice(user_agent),
               'Referer': 'https://www.lagou.com/jobs/list_python?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=&labelWords=hot',
               'Accept-Language': 'zh-CN,zh;q=0.9'
               }
    proxy = random.choice(r1['proxies'])
    resp = requests.get(url, headers=headers, proxies={'http': 'http://{}:{}'.format(proxy['ip'], proxy['port'])})
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    text = []
    try:
        t = soup.find('div', attrs={'class': 'job-detail'})
        for i in t.findAll('p'):
            text.append(i.text)
        return "\n".join(text)
    except:
        return "Error"


for page in range(1, 31):
    print('正在爬取第{}页'.format(page))
    s = requests.session()
    s.get(url1, headers=headers, timeout=2)  # 请求首页获取cookies
    cookies = s.cookies  # 为此次获取的cookies
    proxy = random.choice(r1['proxies'])
    data = {
        'first': 'true',
        'kd': 'python',
        'pn': page
    }
    # 提交表单数据，做post申请
    r = requests.post(url2, headers=headers, cookies=cookies,
                      proxies={'http': 'http://{}:{}'.format(proxy['ip'], proxy['port'])}, data=data)
    r.encoding = 'utf-8'
    # 获取json数据
    result = r.json()
    positions = result['content']['positionResult']['result']
    for position in positions:
        positionId = position['positionId']
        companyFullName = position['companyFullName']
        district = position['district']
        education = position['education']
        financeStage = position['financeStage']
        firstType = position['firstType']
        secondType = position['secondType']
        thirdType = position['thirdType']
        createTime = position['createTime']
        jobNature = position['jobNature']
        positionAdvantage = position['positionAdvantage']
        positionName = position['positionName']
        salary = position['salary']
        workYear = position['workYear']
        skillLables = position['skillLables']
        detail = getInfo(url3.format(positionId))
        # 数据入库
        mongo_lagou.insert_one({
            'companyFullName': companyFullName,
            'district': district,
            'education': education,
            'financeStage': financeStage,
            'firstType': firstType,
            'secondType': secondType,
            'thirdType': thirdType,
            'createTime': createTime,
            'jobNature': jobNature,
            'positionAdvantage': positionAdvantage,
            'positionName': positionName,
            'salary': salary,
            'workYear': workYear,
            'skillLables': skillLables,
            'detail': detail
        })
        time.sleep(3)
        # 加上随机的时间延迟
    rdtime = 20 * np.random.rand()
    time.sleep(rdtime)
print("爬取完成！")
