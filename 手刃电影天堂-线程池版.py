import requests
import re
from concurrent.futures import ThreadPoolExecutor

def dongmanwang(url):

        domain="https://www.dy2018.com"

        head={
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"#user-agent使用机器
        }
        resp=requests.get(url,headers=head)
        resp.encoding="gbk"
        pagesource=resp.text


        obj=re.compile(r'height="26">.*?<a href="(?P<href>.*?)".*?title=(?P<title>.*?)>.*?',re.S)
        dongman=obj.finditer(pagesource)
        for index in dongman:
            href=index.group("href")
            title=index.group("title")
            child_url=domain+href
            print(child_url)
            print(title)

if __name__ == '__main__':

    with ThreadPoolExecutor(50)as t:
        for i in range(2,200):       #第二页到第二百页
            t.submit(dongmanwang,url=f"https://www.dy2018.com/html/dongman/index_{i}.html")#当i=1时是/dongman/index.html，没有下滑线，所以没有写在一起



