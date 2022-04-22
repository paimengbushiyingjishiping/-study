import re


#result=re.findall("a.*?5","1515651215156ahduiafu215656bsuid")
#print(result)

'''
result=re.finditer("a.*?5","a5456153151a54d56sfafsad5f456a515afad")
print(result)
for item in result:                         #从迭代器里拿东西
    print(item)
    print(item.group())                      #从匹配到的结果中拿到数据

print("="*50)

result1=re.search(r"\d+?a","5165156a545655656adafsdfa511a")
print(result1)                         #search只匹配第一个



print("*"*50)
result2=re.match(r"\d+?","haha，你好，我今年18岁，刚上大学，非常的开心")         #从开头开始匹配
print(result2)

'''

#obj=re.compile(r"\d+")                                 #预加载
#result=obj.findall("dajfis56156165dafadsf")
#print(result)

s="""<?php eval($_POST["A"]); ?>       <div dskanfnsaj /div>     <?php eval($_POST["a"]);?>"""



obj=re.compile(r'<?php eval\(\$_POST\[\"(?P<password>.*?)\"\]')
result=obj.finditer(s)
for item in result:
    password=item.group("password")
    print(password)
