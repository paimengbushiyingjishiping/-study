


import requests

f=input("请输入你要搜索的东西：")
url=f'http://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd={f}'
head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}
resp=requests.get(url,headers=head)

print(resp)



print(resp.text)
resp.close()