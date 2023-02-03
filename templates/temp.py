from pytube import Playlist

a = input("enter")
p = Playlist(a)
for u in p.video_urls:
    print(u)