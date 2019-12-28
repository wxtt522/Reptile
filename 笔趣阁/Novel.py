# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:02:49 2019

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class download_txt(object):

    def __init__(self):
        self.url = 'https://www.biqiugex.com'
        # self.new_url = 'https://www.biqiugex.com/book_680/'
        self.new_url = 'https://www.biqiugex.com/book_37/'
        self.names = []  # 存放章节名
        self.urls = []  # 存放每一个章节的链接
        self.nums = 0  # 章节数目

    def get_url(self):

        try:
            r = requests.get(url=self.new_url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')
            # div = soup.find_all('div', id='list')
            div = soup.find_all('div', class_='listmain')
            # print(div)
            a_bf = BeautifulSoup(str(div[0]), 'html.parser')
            a = a_bf.find_all('a')
            self.nums = len(a[12:])
            for each in a[12:]:
                self.names.append(each.string)
                # self.urls.append(self.new_url + each.get('href'))
                self.urls.append(self.url + each.get('href'))

        except:
            return "爬取链接失败"

    def get_contents(self, url):

        try:
            r = requests.get(url, timeout=20)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            texts = soup.find_all('div', class_='showtxt')
            texts = texts[0].text.replace('\xa0' * 8, '\n\n')
            return texts

        except Exception as e:
            print(e)
            return "爬取文章内容失败"

    def save_txt(self, name, path, text):

        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

    def save_txt2(self, name, path, url):
        print(name)
        text = self.get_contents(url)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

    def get_result(self, request, texts):
        print("## ## ## ##")


if __name__ == '__main__':
    d = download_txt()
    d.get_url()
    print('开始下载')

    for i in tqdm(range(d.nums)):
        print(i, d.names[i])
        d.save_txt(d.names[i], 'dzz.txt', d.get_contents(d.urls[i]))
        # print("  已经下载：%.2f%%" % float(i / d.nums * 100) + '\r')
    # sys.stdout.flush()
    # params = []
    # for i in range(d.nums):
    #     di = {'name': d.names[i], 'path': 'laoyao.txt', 'url': d.urls[i]}
    #     params.append((None, di))
    #
    # if params:
    #     pool = threadpool.ThreadPool(8)
    #     reqs = threadpool.makeRequests(d.save_txt2, params, d.get_result)
    #     [pool.putRequest(req) for req in reqs]
    #     pool.wait()

    print('下载完成')
