# pip install pytube
import os
from pytube import YouTube
link = input("Linki Giriniz : ")
directory = input("Yol : ")
yt = YouTube(link)

mp3 = yt.streams.filter(only_audio=True).first()
print("Veri aliniyor..")
sonuc = mp3.download(directory)
print("Veri alindi!")
print("İndirilme basladi..")
base , ext = os.path.splitext(sonuc)
to_mp3 = base + ".mp3"
os.rename(sonuc,to_mp3)
print("İndirilme tamamlandi!")

