# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:07:29 2019

@author: Administrator
"""

import os
import re
import sys
import threading
from hashlib import md5
from urllib.parse import urlencode

import requests


def get_page(offset):
    headers = {
        'cookie': 'tt_webid=6732319867229423107; csrftoken=2b461cc760363fab27b9386dbf4e37ca; tt_webid=6732319867229423107; WEATHER_CITY=%E5%8C%97%E4%BA%AC; passport_auth_status=0f327ded3a6ae0f9af78c0c717154af0; sso_auth_status=085b78061c33b016a85dca13cc23b58d; login_flag=976bb02ceb707e7bd6fa34e2262a4e19; sessionid=a95378cda20a55671d13b6327fede803; sid_tt=a95378cda20a55671d13b6327fede803; ccid=34ced35c84a04d8541f1dbc6c5dd7687; uid_tt=6b32b6fe0e53b2ada6f3992c0fd26d2c34e2607618a66a24abeadb00f170296d; UM_distinctid=16d6269bbd26d6-079e82cbb8066b-5373e62-1fa400-16d6269bbd3765; _ga=GA1.2.402794203.1569314160; CNZZDATA1259612802=1360915038-1569309931-https%253A%252F%252Fwww.toutiao.com%252F%7C1569309931; sso_uid_tt=7e6b89be5a09acedeb12af8903e6310c; toutiao_sso_user=812de0274d63836577cf6e2ee7f7a69d; sid_guard="a95378cda20a55671d13b6327fede803|1569377214|15552000|Mon\054 23-Mar-2020 02:06:54 GMT"; s_v_web_id=e626d7a8beb79508c3f1e52cc11e01e8; __tasessionId=sjumb16271569740070248',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    base_url = 'https://www.toutiao.com/api/search/content/?'
    url = base_url + urlencode(params)
    try:
        r = requests.get(url, headers=headers)
        if 200 == r.status_code:
            return r.json()
    except:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('title') is None:
                continue
            title = re.sub('[\t\\\|]', '', item.get('title'))
            images = item.get('image_list')
            if images and title:
                for image in images:
                    origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                    yield {
                        'image': origin_image,
                        'title': title
                    }


def save_image(item):
    # img_path = 'img' + os.path.sep + item.get('title')
    img_path = 'img' + os.path.sep
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    r = requests.get(item.get('image'))
    file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
        file_name=md5(r.content).hexdigest(),
        file_suffix='jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(r.content)
        print("Downloaded image is {} path is {}".format(item.get('title'), file_path))
    else:
        print("Already Downloaded")


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        try:
            save_image(item)
        except:
            print("下载图片失败！")


if __name__ == '__main__':

    keyword = sys.argv[1]
    print(keyword)

    # pool = Pool()     # 进程池
    groups = ([x * 20 for x in range(10)])
    '''
    pool.map(main, groups)
    pool.close()
    pool.join()
    '''
    tasks = []  # 线程池

    for group in groups:
        task = threading.Thread(target=main, args=(group,))
        tasks.append(task)
        task.start()

    # 等待所有线程完成
    for _ in tasks:
        _.join()
    print("完成图片爬取并存储到本地！")
