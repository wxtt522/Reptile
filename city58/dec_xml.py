# 解析xml文件
from xml.etree import ElementTree as ET

tree = ET.parse('jianli.xml')
root = tree.getroot()   # 一个Element对象
childs = root.getchildren()

for c in childs:
    for cc in c.getchildren():
        datas = {}
        datas[cc.tag] = cc.attrib
        print(datas)
