#importing the required libraries

from pytube import YouTube

link = input("Enter the link of the YouTube video to be downloaded: ")

yt = YouTube(link)

print("Title: ", yt.title, "\nViews: ", yt.views, "\nRating: ", yt.rating)


yd = yt.streams.get_highest_resolution();
#can even just extract the audio
# ya = yt.streams.get_audio_only();

if yd:
    yd.download('Enter the path where you want to download the video')
else:
    print("Couldn't find a stream of the highest resolution.")
# ya.download('Enter the path where you want to download the audio')


