s = '?《Python应用基础》微专业体验课——Python 面向对象语法精讲_audio.mp4'
print(s)
def replace_char(s1):
    char = ['?', '*' ,':' ,'"','<', '>' ,'\\' ,'/' ,'|']
    for i in s1:
        if i in char:
            s1 = s1.replace(i, '')
    return s1
s = replace_char(s)
print(s)
