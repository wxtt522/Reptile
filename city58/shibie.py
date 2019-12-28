from fontTools.ttLib import TTFont

font = TTFont('testotf1.woff')  # 读取woff文件
# font.saveXML('./m.xml')#转成xml
num = [6, 2, 9, 0, 1, 8, 4, 3, 7, 5]
list = font.getGlyphOrder()[2:]
print(list)
for i, p in zip(list, num):
    dict[p] = i
print(dict)
nian = ''

# font1 = TTFont('testotf1.woff')  # 读取新的woff文件
# # font1.saveXML('./m999.xml')  # 转成xml
# ff_list = font1.getGlyphNames()  # 返回一个对象
# ff_news = font1.getGlyphOrder()
# for fo in ff_news:
#     fo2 = font1['glyf'][fo]
#     for fff1 in list:
#         fo3 = font['glyf'][fff1]
#         if fo2 == fo3:
#             print(fo, dict[fff1])
