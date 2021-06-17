import subprocess
subprocess.Popen('ffmpeg -i C:\\Users\\1\\Desktop\\1_video.mp4 -i C:\\Users\\1\\Desktop\\1_audio.mp4 -c copy 1.mp4 -y -loglevel quiet', shell=True)
# os.sys('ffmpeg -i C:\\Users\\1\\Desktop\\1_video.mp4 -i C:\\Users\\1\\Desktop\\1_audio.mp4 -c copy C:\\Users\\1\\Desktop\\1.mp4 -y -loglevel quiet')