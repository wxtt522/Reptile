# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:33:55 2019

@author: Administrator
"""

import requests
import re
import time
import random
from redis import Redis


class Zhihu(object):

    def __init__(self):

        self.url = 'https://www.zhihu.com/api/v4/questions/310564833/answers'
        self.headers = {
            'cookie': '_zap=a8c0b7cf-055d-4b71-9091-5e7a4af583ba; d_c0="AAAhuR7sxQ-PTrRceFpYnLjumnpob8O8M9k=|1563760381"; tshl=; __utmv=51854390.100-1|2=registration_date=20151219=1^3=entry_date=20151219=1; _ga=GA1.2.1633948531.1563949119; _xsrf=DAtL1q7WYloJc9SXF6fVuCJpG0CsB2ap; tst=h; capsion_ticket="2|1:0|10:1571035459|14:capsion_ticket|44:MTMxZjVkM2I4NDRkNGVlNWJkNGMyOTE5MzM5ZDdlYTc=|096989e8b5c94d7cf8b536e571c1bb4d4b654686eb99f26fc26a68d1c61d75d7"; z_c0="2|1:0|10:1571035465|4:z_c0|92:Mi4xZXZCa0FnQUFBQUFBQUNHNUh1ekZEeVlBQUFCZ0FsVk5TV2VSWGdCNU5ZcTQ3dXJnTVEycWNTZTdUcVFmd1Zia05n|19ce79dea94789ff6156c192a9a95c88f574ef9c17e823d4339633bfc2ca09aa"; __utma=51854390.1633948531.1563949119.1567160205.1571035659.3; __utmz=51854390.1571035659.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wen-xin-tian-tang/activities; q_c1=a7aa7feda1dd4dc986301b7725101a68|1572398527000|1563760487000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1571565113,1571724394,1572398417,1572483503; tgw_l7_route=fd63c3ae6724333eae94c71ab6d69628; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1572502831',
            'referer': 'https://www.zhihu.com/question/310564833',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        self.r = Redis.from_url("redis://127.0.0.1:6379", decode_responses=True)

    def get_urls(self, offset, urls):

        params = {
            'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
            'limit': 5,
            'offset': offset,
            'platform': 'desktop',
            'sort_by': 'default'
        }
        r = requests.get(self.url, headers=self.headers, params=params)
        data = r.json()['data']
        for i in data:
            content = i['content']
            pic_urls = re.findall(r'data-actualsrc="(.*?.(gif|jpg|png))', content)
            for j in range(len(pic_urls)):
                self.r.sadd("urls", pic_urls[j][0])

    def get_total(self):

        params = {
            'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
            'limit': 5,
            'offset': 0,
            'platform': 'desktop',
            'sort_by': 'default'
        }
        r = requests.get(self.url, headers=self.headers, params=params)
        totals = r.json()['paging']['totals']
        return totals


if __name__ == '__main__':

    crawl = Zhihu()
    total = crawl.get_total()
    page = int(total / 5) + 1
    urls = []
    for i in range(page):
        crawl.get_urls(offset=i * 5, urls=urls)
        print("已抓取第{}页回答的全部表情包链接！".format(i + 1))
        time.sleep(random.random())
