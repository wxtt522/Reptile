import base64
import re

import requests
from fontTools.ttLib import TTFont, BytesIO
#没有user-agent会找不到
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}
response=requests.get('https://zz.58.com/pinpaigongyu/?utm_source=link&spm=u-Lj4SZGxa1luDubj.psy_jiugongge&PGTID=0d100000-0015-696d-466f-b8e0970a2a06&ClickID=1',headers=headers)
# print(response.text)
#匹配出页面字体，正则抓取
text=response.text
font_str=re.findall(r"base64,(.*?)'\)",text)[0]

def make_font_bin(font_string):
    font_bin=base64.decodebytes(font_string.encode())
    #存储成文件用fontcreator打开作为基础字体仅此一次然后注释
    # with open('house.bin','wb') as f:
    #     f.write(font_bin)
    return font_bin
#打印出基础字体
base_str='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'
#fontcreator中找出的基础字形
base_num=['0','1','2','3','4','5','6','7','8','9']
#基础字形对应的编码信息
base_code=['uni9FA4','uni993C','uni9476','uni9EA3','uni9A4B'
           ,'uni9F64','uni9E3A','uni9F92','uni958F','uni9FA5']
# print(font_str)
#创建TTfont对象
base_font=TTFont(BytesIO(make_font_bin(base_str)))#解析xml页面
base_list=base_font.getGlyphOrder()
# print(base_font.getGlyphOrder())#得到所有编码信息
# print(base_font.getBestCmap())#得到编码所对应的的

#创建当前字体的ttfont
match_font = TTFont(BytesIO(make_font_bin(font_str)))
# print(match_font.getGlyphOrder())#得到所有编码信息
# print(match_font.getBestCmap())#得到编码所对应的的

#匹配俩种字体字形
def match_font_base(font_string):
    match_font = TTFont(BytesIO(make_font_bin(font_str)))
    num_dic = {}
    uni_list = match_font.getGlyphOrder()

    for i in range(11):
        # 找出相应字形对应绘制图元的对象
        matchGlyph = match_font['glyf'][uni_list[i]]
        for j in range(10):
            baseGlyph = base_font['glyf'][base_list[j]]
            # 如果相应绘制图元相等，认为两个字形相等
            if matchGlyph == baseGlyph:
                # 从已知对应关系列表中查出对应文字
                num_dic[uni_list[i]] = base_num[j]
                break
    return num_dic
print(match_font_base(font_str))
import lxml.html
d_map=match_font_base(font_str)
print(d_map)

#解析html找到相应信息
parse_result=lxml.html.fromstring(response.text)
house_elements=parse_result.cssselect('ul.list li')
for house_element in house_elements:
    '''房租信息'''
    moneys=house_element.cssselect('div.money span.strongbox b')[0].text
    money_bin=''.join(moneys.split(' '))
    # a=decode_text(money,d_map)
    money_hex_list=money_bin.encode('unicode-escape').decode()[4:].split('\\u')
    # print(money_hex_list)
    s=[]
    for money_hex in money_hex_list:
        if money_hex:
            if not money_hex.endswith(r'\n'):
                money_int=int(money_hex,16)
            else:
                money_int=int(money_hex[:4],16)
            # print(money_int)
            qian_moeny=match_font.getBestCmap()[money_int][:-2]
            hou_money='0'+str(int(match_font.getBestCmap()[money_int][-2:])-1)
            money=qian_moeny+hou_money
            s.append(d_map[money])
    if len(s) > 4:
        s.insert(4,'-')
    money_final=''.join(s)
    print('房租为%s元/月'%money_final)