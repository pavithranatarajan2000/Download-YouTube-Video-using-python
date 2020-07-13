#first install pip 
#from pip install pytube

from __future__ import unicode_literals  
import youtube_dl
import urllib
import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=bKxL536zqro'])  
    
  #In last line you can change the link to download video which you want
