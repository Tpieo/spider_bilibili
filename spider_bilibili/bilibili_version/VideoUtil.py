from bilibili_version import RequestUtil
from bilibili_version import FileUtil


def download_video_single(referer_url, video_url, audio_url, video_name):
    video_name = '1'
    print("视频正在下载")
    video_content = RequestUtil.getVideRequest(referer_url, video_url)
    print('视频下载完成，大小：', round(int(video_content.headers.get('content-length', 0)) / 1024 / 1024, 2), 'MB')
    FileUtil.out_received_video(video_content, video_name, "bilibili_version/video_final/")
    print("音频正在下载")
    audio_content = RequestUtil.getVideRequest(referer_url, audio_url)
    print('音频下载完成，大小：', round(int(audio_content.headers.get('content-length', 0)) / 1024 / 1024, 2), 'MB')
    FileUtil.out_received_audio(audio_content, video_name, "bilibili_version/video_final/")
    FileUtil.video_audio_merge_single(video_name, "bilibili_version/video_final/")


