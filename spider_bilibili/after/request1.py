import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV1M54y1d7UB?t=8&p=62'
}
url = 'https://www.bilibili.com/video/BV1M54y1d7UB?t=8&p=62'
res = requests.get(url=url, headers=headers)
res = res.text
result = re.findall('"part": "(.*?)", "duration"', res)
sum = 0
for name1 in result:
    sum += 1
    print(name1)
print(sum)