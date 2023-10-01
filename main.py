#importing the required libraries

from pytube import YouTube

link = input("Enter the link of the YouTube video to be downloaded: ")

yt = YouTube(link)

print("Title: ", yt.title, "\nViews: ", yt.views, "\nRating: ", yt.rating)


yd = yt.streams.get_highest_resolution();
#can even just extract the audio
# ya = yt.streams.get_audio_only();

yd.download('C:/Users/Sidhant Mishra/Downloads')
# ya.download('C:/Users/Sidhant Mishra/Downloads')


