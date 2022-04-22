import requests

url="https://space.bilibili.com/628288620?spm_id_from=333.337.0.0"
head={
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}
resp=requests.get(url,headers=head)
print(resp.text)
resp.close()