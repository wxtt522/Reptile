import requests
from lxml import etree

from study.city58.jianli import change_font

url = 'https://sz.58.com/searchjob/pve_5569_1_pve_5568_1/?key=%E7%BE%8E%E5%AE%B9&cmcskey=%E7%BE%8E%E5%AE%B9&final=1&jump=2&specialtype=gls&jlabtest=&-3=J&param8616=0&param8516=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
html = requests.get(url, headers=headers)
page = html.content.decode(html.encoding)
web = etree.HTML(page)
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
    person.append({'姓名': change_font(''.join(name)), '性别': change_font(''.join(sex)), '年龄': change_font(''.join(age))
                   , '工龄': change_font(''.join(work_time)), '学历': change_font(''.join(school)), '期望职位': ''.join(want_work)
                   , '现职位': ''.join(now), '期望工作地': ''.join(want_local)})
print(person)