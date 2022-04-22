import requests
import re

url="https://dy2018.com/"
head={
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}
resp=requests.get(url,headers=head)
resp.encoding="gbk"
pagesource=resp.text


obj=re.compile(r"2022必看热片.*?<ul>(?P<all>.*?)</ul>",re.S)


hahaha=obj.finditer(pagesource)

for item in hahaha:
    all=item.group("all")

    print(all)


obj2=re.compile(r'<li><a href=\'(?P<html>.*?)\' title=(?P<name>.*?)>.*?',re.S)
haha2=obj2.finditer(all)
for item in haha2:
    html=item.group("html")
    name=item.group("name")
    print(name)
    child_url=url.strip("/")+html
    print(child_url)
    child_resp=requests.get(child_url)
    child_resp.encoding = 'gbk'

    obg3=re.compile(r"【下载地址】本站专属下载器：点击下方链接.*?bgcolor=\"\#fdfddf\"><a href=\"(?P<xiazai>.*?)\"",re.S)
    diahao=obg3.finditer(child_resp.text)
    for item in diahao:
        xiazai=item.group("xiazai")
        print(xiazai)

