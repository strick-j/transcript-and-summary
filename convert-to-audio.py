from moviepy.editor import *

filename = input("Enter the mp4 file you wish to convert to audio name: ")

video_path = f"{filename}.mp4"
audio_path = f"{filename}.mp3"

video = VideoFileClip(f"{video_path}")
video.audio.write_audiofile(f"{audio_path}")