from pytube import *
from pytube.exceptions import PytubeError
from pytube.helpers import safe_filename
import os
from ConvertClass import ConvertClass

class ConvertMP4(ConvertClass):
    def __init__(self, links, path,unsuccessfulLinks):
        super().__init__(links,path,unsuccessfulLinks)
    
    def doConversion(self):
        try:
            for link in self.links:
                ytLink = YouTube(link)
                try:
                    videoTitle = (safe_filename(ytLink.title))
                except PytubeError as pe:
                    print(str(pe))
                    videoTitle = link #This is just in case something goes wrong when taking in the title
                if not ConvertClass.checkIfVidExists(path=self.path,title=videoTitle):
                    ytLink.streams.first().download(self.path,filename=videoTitle+'.mp4')
                    print(videoTitle + " downloaded!")
                else:
                    print("Video already exists!")
                    continue
        except Exception as e:
            print(str(e))
            self.unsuccessfulLinks.append(link)
