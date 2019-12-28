#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 14:46
# @Author  : longHui.wu  
# @File    : maybe.py
import requests
from lxml import etree
import re
import base64
from fontTools.ttLib import TTFont

# url = "https://sz.58.com/searchjob/"
url = "https://sz.58.com/searchjob/pve_5569_1_pve_5568_1/"

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/73.0.3683.86 Safari/537.36",
}

response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
font_face = html.xpath('//head/style[1]/text()')[0].strip()
# 提前字体文件
base64_code = re.findall(r"base64,(.*?)\)", font_face)
if len(base64_code) != 0:
    base64_code = base64_code[0]
woff = base64.b64decode(base64_code)
# base64 写入字体文件58tc.woff中，一定要wb方式写入，每次运行代码会覆盖文件
with open("58tc.woff", "wb") as f:
    f.write(woff)

# 打开下载保存好的新字体文件58tc.woff
font = TTFont('58tc.woff')
# 打开本地保存的基本字体文件58.woff
base_font = TTFont("jianli.woff")

# getGlyphNames()[1:-1]和getGlyphOrder()[2:]结果是一样的
# uni_list = font.getGlyphNames()[1:-1]
uni_list = font.getGlyphOrder()[2:]

# 定义一个临时存储新字体文件映射关系的字典temp
temp = {}
# 把本地字体文件的映射关系用base_uni和base_value两个列表映射保存
base_uni = ['uniE16E', 'uniE1A8', 'uniE281', 'uniE2AE', 'uniE2BD', 'uniE2D6', 'uniE335', 'uniE393', 'uniE3B2',
            'uniE50A', 'uniE539', 'uniE57F', 'uniE5F3', 'uniE766', 'uniE82D', 'uniE884', 'uniE90A', 'uniEA33',
            'uniEAAF', 'uniEB01', 'uniEC12', 'uniEDC8', 'uniEDF5', 'uniEE81', 'uniEE83', 'uniEED5', 'uniEF5B',
            'uniF0D3', 'uniF1B7', 'uniF23A', 'uniF340', 'uniF3BE', 'uniF3F1', 'uniF426', 'uniF4D4', 'uniF500', 'uniF521'
    , 'uniF542', 'uniF571', 'uniF588', 'uniF66D', 'uniF680', 'uniF699', 'uniF6A3', 'uniF835']
base_value = ['陈', '杨', 'E', '4', '6', 'M', '高', '下', '2', '李', '生', '吴', '经', '王', '3', '博', '技', '本',
              '周', '刘', '无', '应', '中', '校', '以', '7', '9', '科', '1', '届', '硕', '士', '黄', '大', '张', '5', '0'
    , 'B', '赵', 'A', '男', '专', '女', '验', '8']

# base_uni = [
#     'uniE0AC', 'uniE0D6', 'uniE189', 'uniE19A', 'uniE1BC', 'uniE441', 'uniE47A', 'uniE4BE', 'uniE4F1',
#     'uniE587', 'uniE5B0', 'uniE5CE', 'uniE615', 'uniE632', 'uniE701', 'uniE87F', 'uniEAC1', 'uniEAF9',
#     'uniEB60', 'uniEB96', 'uniEBB0', 'uniEC03', 'uniEF5F', 'uniEF8B', 'uniF037', 'uniF076', 'uniF0A0',
#     'uniF13A', 'uniF14D', 'uniF1DB', 'uniF264', 'uniF2D1', 'uniF31A', 'uniF386', 'uniF406', 'uniF46B',
#     'uniF49A', 'uniF4DB', 'uniF5F0', 'uniF607', 'uniF62A', 'uniF6E6', 'uniF772', 'uniF787', 'uniF7B9'
# ]
# base_value = [
#     '7', '下', '王', '周', '专', '0', '女', '博', '杨', '李', '校', '技', '届', '8', '男', '科', '中',
#     '赵', '生', 'M', '9', '以', '经', '6', '陈', 'A', '验', '黄', 'B', '5', '士', '1', '张', '硕', '4',
#     '高', '无', '大', '吴', 'E', '应', '3', '2', '本', '刘'
# ]
# 循环对比
for i in range(len(base_uni)):
    # 编码字体坐标转化成了列表，列表里是一个个元组，元组里放的是(x,y)坐标
    new_glyph = list(font['glyf'][uni_list[i]].coordinates)
    # 用前两个坐标作为取差值
    new_glyph_difference = [abs(k[0] - k[1]) for k in new_glyph[:2]]
    for j in range(len(base_uni)):
        base_glyph = list(base_font['glyf'][base_uni[j]].coordinates)
        base_glyph_difference = [abs(n[0] - n[1]) for n in base_glyph[:2]]
        # 比较两个差值是否为0
        if int(abs(sum(new_glyph_difference) / len(new_glyph_difference) - sum(base_glyph_difference) / len(
                base_glyph_difference))) == 0:
            # 把编码去掉uni三个字符然后转换成全小写，再拼接成网页源代码一样的编码格式，最后把映射关系存储到temp字典中
            temp["&#x" + uni_list[i][3:].lower() + ';'] = base_value[j]

# 构造正则表达式用|匹配左右任意一个表达式，替换编码
re_rule = '(' + '|'.join(temp.keys()) + ')'
# 把所有的编码替换成文字
response_data = re.sub(re_rule, lambda x: temp[x.group()], response.text)
web = etree.HTML(response_data)

content = web.xpath('//*[@id="infolist"]/ul/li')
person = []
for el in content:
    name = el.xpath('./div[1]/dl/dd/div[1]/a/span/text()')
    sex = el.xpath('./div[1]/dl/dd/div[1]/a/div/div/em[1]/text()')
    age = el.xpath('./div[1]/dl/dd/div[1]/a/div/div/em[2]/text()')
    work_time = el.xpath('./div[1]/dl/dd/div[1]/a/div/div/em[3]/text()')
    school = el.xpath('./div[1]/dl/dd/div[1]/a/div/div/em[4]/text()')

    want_work = el.xpath('./div[1]/dl/dd/p[1]/span/text()')
    now = el.xpath('./div[1]/dl/dd/p[1]/em[2]/text()')
    want_local = el.xpath('./div[1]/dl/dd/p[2]/span/text()')
    print(name, sex, age, work_time, school, want_work, now, want_local)

# personal_information = data.xpath('//div[@id="infolist"]/ul/li//dl[@class="infocardMessage clearfix"]')
# for info in personal_information:
#     # 姓名
#     name = info.xpath('./dd//span[@class="infocardName fl stonefont resumeName"]/text()')[0]
#     # 性别
#     gender = info.xpath('./dd//div[@ class="infocardBasic fl"]/div/em[1]/text()')[0]
#     # 年龄
#     age = info.xpath('./dd//div[@ class="infocardBasic fl"]/div/em[2]/text()')[0]
#     school = info.xpath('./div[1]/dl/dd/div[1]/a/div/div/em[4]/text()')
#     # 工作经验
#     work_experiences = info.xpath('./dd//div[@ class="infocardBasic fl"]/div/em[3]/text()')
#     if work_experiences == []:
#         work_experience = ""
#     else:
#         work_experience = info.xpath('./dd//div[@ class="infocardBasic fl"]/div/em[3]/text()')[0]
#     # 学历
#     educations = info.xpath('./dd//div[@ class="infocardBasic fl"]/div/em[4]/text()')
#     if educations == []:
#         education = ""
#     else:
#         education = info.xpath('./dd//div[@ class="infocardBasic fl"]/div/em[4]/text()')[0]
#     print(name, gender, age, work_experience, education)
