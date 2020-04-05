from pytube import YouTube
import subprocess
import os

# you should make directory 'youtube'
# you should put ffmpeg file into 'youtube' directory

download_path = './youtube'
high_resolution_video_index = 0

input_url = input('What is your youtube url? ')

# YouTube(url).streams.get_highest_resolution().donwload(download_path)

videos = YouTube(input_url).streams

# videos = YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
# for i in range(len(videos)):
#     print(i, ' : ', videos[i])

videos[high_resolution_video_index].download(download_path)

input_want_mp3 = input('Do you want to make mp3 file (y/n)? ')

if input_want_mp3 == 'y':
    original_filename = videos[high_resolution_video_index].default_filename
    video_filename = os.path.join(download_path, original_filename)
    mp3_filename = video_filename + '.mp3'

    subprocess.call([
        download_path + '/ffmpeg',
        '-i',
        video_filename,
        mp3_filename
    ])

print('completed!')
