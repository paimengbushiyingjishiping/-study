import requests



url="	https://fanyi.baidu.com/sug"

f=input("请输入你要翻译的词：")
dat={
    "kw":f
}
resp=requests.post(url,data=dat)

print(resp)
print(resp.json())