#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 10:39
# @Author  : longHui.wu  
# @File    : matlib_graph.py
import os
import re
import time
import urllib.request

import pytesseract
from PIL import Image
from fontTools.ttLib import TTFont
import requests
from lxml import etree
from matplotlib import pyplot as plt
import numpy as np


def deal_font(font):
    font_name = font.getGlyphOrder()[2:]
    zb = [font['glyf'][i].coordinates for i in font_name]
    fig, ax = plt.subplots()
    for index, one in enumerate(zb):
        x, y = [i[0] for i in one], [i[1] for i in one]
        plt.plot(x, y)
        x_n = [i + np.max(x) + 100 for i in x]
        plt.plot(x_n, y)
        plt.fill(x, y, 'black')
        plt.fill(x_n, y, 'black')
        # 去边框
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        # 去刻度
        plt.axis('off')
        plt.fill(x, y, 'black')
        plt.savefig('images/%s.jpg' % index)
        plt.close()
    path = 'images/'
    num = []
    # 灰度、二值化
    for one in os.listdir(path):
        img = Image.open(path + one)
        imgry = img.convert("L")
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        out.save(path + one)
        # text = pytesseract.image_to_string(out, lang="num")
        text = pytesseract.image_to_string(out)
        num.append(text[0])
    # 字名与数字
    name_num = {font_name[i]: num[i] for i in range(len(font_name))}
    print(name_num)
    return name_num


font = TTFont(r'jianli2.woff')
deal_font(font)
