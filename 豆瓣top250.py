    import requests
    import re


    for i in range(1,11):

         head={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}


         resp=requests.get(f"https://movie.douban.com/top250?start={i}&filter=",headers=head)
         pagesource=resp.text
         print(resp.text)
         obj=re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?导演: (?P<director>.*?)&nbsp;&nbsp;&nbsp;'
                   r'主演: (?P<actor>.*?)<br>(?P<age>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;(?P<genres>.*?)</p>.*?<span>(?P<num>.*?)人评价</span>',re.S)            #re.S可以让正则表达式匹配换行符

         hah=obj.finditer(pagesource)
         for item in hah:
           name=item.group("name")
           director=item.group("director")
           actor=item.group("actor")
           age=item.group("age").strip()      #去掉字符串两边的空白
           country=item.group("country")
           genres=item.group("genres").strip()
           num=item.group("num").strip()


           print(name,director,actor,age,country,genres,num)

