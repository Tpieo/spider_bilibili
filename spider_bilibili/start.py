# 1.请把要下载的视频网页源代码放到html.txt文件里
# 2.在下面的 start_page 后面输入起始页，end_page 后面输入结束页（只有1页，都输入为1）
# 3.在 save_path 里输入保存路径，按照 python 反斜杠转义

start_page = 16
end_page = 114
save_path = 'D:\\video\\bilibili'

# 替换不可命名的字符
def replace_char(s):
    char = ['?', '*' ,':' ,'"','<', '>' ,'\\' ,'/' ,'|']
    for i in s:
        if i in char:
            s = s.replace(i, '')
    return s

import re # (.*?)
import shutil
import os

# video_info
f = open('html.txt', encoding='utf-8')
s = f.read()
f.close()
episode_names_list = re.findall('"part":"(.*?)","duration"', s)
video_title = re.findall('<h1 title="(.*?)" class="video-title">', s)[0]
video_BV_index = re.findall('"videoData":{"bvid":"(.*?)","aid"', s)[0]
video_url = re.findall('itemprop="url" content="(.*?)"><meta data-vue-meta=', s)[0]
up = re.findall('itemprop="author" name="author" content="(.*?)">', s)[0]
# save_info
dir1 = f'{save_path}\\{video_title[0:20]}'
if os.path.exists(dir1) == 0:
    os.mkdir(dir1)
f2 = open(f'{save_path}\\{video_title[0:20]}\\info.txt', 'w')
f2.write(f'url:{video_url}\nup:{up}')
f2.close()

# transfer_file
# from: bilibili_version/video/1.mp4 to: D:\video\bilibili
start_page = start_page
end_page = end_page
print(f'您当前正在下载：{video_title[0:20]}')
for i in range(start_page-1, end_page):
    print(f'您当前正在下载：P{str(i+1)}_{episode_names_list[i]}')
    video_BV_index_evrey_episode = f'{video_BV_index}?p={str(i+1)}'
    __import__('bilibili_version').BLBL.main("单个", video_BV_index_evrey_episode, 0)  ###
    video_from = 'bilibili_version\\video\\1.mp4'
    video_to_dir = f'{save_path}\\{video_title[0:20]}'
    video_name = replace_char(episode_names_list[i])
    video_to = f'{video_to_dir}\\P{str(i+1)}_{video_name}.mp4'
    shutil.move(video_from, video_to)
    print(f'P{str(i+1)}_{episode_names_list[i]} 已转移到目标路径！')
    print()

print(f'{video_title[0:20]} 从 P{str(start_page)} 到 P{str(end_page)} 下载完成！')
print()
