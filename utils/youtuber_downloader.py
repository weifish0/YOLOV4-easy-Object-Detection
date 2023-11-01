import pytube
import time
import os

download_path = os.path.abspath(__file__)
print(download_path)

# 輸入網址
url = "https://www.youtube.com/watch?v=mPmG1IuHuBQ"

print("開始下載")
a = time.time()
my_video = pytube.YouTube(url)

# my_video = my_video.streams.get_audio_only()
my_video = my_video.streams.get_highest_resolution()

print(my_video.download(""))
b = time.time()

if b-a < 60: print(f'耗時{round(b-a)}秒')
else: print(f'耗時{int((b-a)//60)}分 {round((b-a)%60)}秒')