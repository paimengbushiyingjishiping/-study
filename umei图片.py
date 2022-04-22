import requests
import re
domain="https://umei.net"                                      #图片所在的主网站
f=open("tupain.html",mode="w",encoding="utf-8")
url="https://umei.net/faxingtupian/nvshengfaxing/"

resp=requests.get(url)
resp.encoding="utf-8"
resp_text=resp.text

obj=re.compile(r'<ul class="pic-list after">(?P<FW>.*?)</ul>',re.S)            #抓取图片所在的html
book=obj.finditer(resp_text)
for item in book:
   FW=item.group("FW")
   print(FW)

n=1
obj1=re.compile(r'a href="(?P<href>.*?)".*?',re.S)               #抓取图片的地址（jpg，png）
href1=obj1.finditer(FW)
for item in href1:
      href=item.group("href")
      realhref=domain+href
      print(realhref)
      resp_finall=requests.get(realhref)
      resp_finall.encoding="utf-8"
      resp_finall_text=resp_finall.text
      obj2=re.compile(r'<a href=".*?">.*?<img src="(?P<tupian>.*?)" /></a>',re.S)
      book2=obj2.finditer(resp_finall_text)

      for item in book2:                                      #下载图片
        tupian=item.group("tupian")
        print(tupian)
        img_resp=requests.get(tupian)
        with open(f"{n}.png",mode="wb")as f:
          f.write(img_resp.content)
        print(f"{n}.png下载完成")
        n=n+1


resp.close()
resp_finall.close()
img_resp.close()
