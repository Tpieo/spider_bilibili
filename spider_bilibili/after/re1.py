import re
import os
f = open(r'D:\python\project\bilibili\2.txt', encoding='utf-8')
# str = "a1234ba2345ba4567bcdef"
str = f.read()
result = re.findall('"part": "(.*?)", "duration"', str)
sum = 0
for name1 in result:
    sum += 1
    print(name1)
print(sum)

# "part": "1.1 面向对象编程模式2", "duration": 186, "vid": "", "weblink": "", "dimension": { "width": 960, "height": 540, "rotate": 0 } }, { "cid": 172932822, "page": 5, "from": "vupload", "part": "1.1 面向对象编程模式3", "duration"
