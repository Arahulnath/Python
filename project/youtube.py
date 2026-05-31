from pytube import YouTube

url = "https://www.youtube.com/watch?v=Pf-HIHDSJ4w"

yt = YouTube(url)

print("Title:", yt.title)

video = yt.streams.get_highest_resolution()

video.download("E:/python/PythonProject1/project")

print("Download completed")