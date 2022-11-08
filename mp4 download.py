# pip install pytube
import os
from pytube import YouTube

link = input("Lütfen linki giriniz : ")
directory = input("Olusturulacak klaksorun adı nedir : ")
try : 
        yt = YouTube(link)
except :
        print("Hatali link!")
        exit()

print("Veri aliniyor..")
print("Veri alindi!")
print("Yukleme baslatiliyor..")
print("Yükleme hala devam ediyor, lütfen pencereyi kapatmatyınız!")
mp4 = yt.streams.get_highest_resolution().download(directory)
print("Yukleme tamamlandi!")
