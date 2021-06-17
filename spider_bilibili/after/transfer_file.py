import shutil
import os

shutil.move(r"D:\python\project\bilibili\bilibili_version\video\专业课加选修课2.docx", r"D:\video\bilibili\1.docx")
dir1 = r'D:\video\bilibili\1'
if os.path.exists(dir1) == 0:
    os.mkdir(dir1)
# print(i)
# print(os.path.exists(dir1))


