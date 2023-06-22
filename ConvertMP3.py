from pytube import *
from pytube.helpers import safe_filename
from pytube.exceptions import PytubeError
import os
from moviepy.editor import *
from ConvertClass import ConvertClass

class ConvertMP3(ConvertClass):
    def __init__(self, links, path,unsuccessfulLinks):
        super().__init__(links, path,unsuccessfulLinks)
        
    
    def convertToMP3(self, originalVid, convertedVid):
        file = AudioFileClip(self.path + '\\' + originalVid)
        file.write_audiofile(self.path + '\\' + convertedVid)
        os.remove(self.path + '\\' + originalVid)
        file.close()
        
    def doConversion(self):
        for link in self.links:
            try:
                ytLink = YouTube(link)
                try:
                    videoTitle = (safe_filename(ytLink.title))
                except PytubeError as pe:
                    print(str(pe))
                if not ConvertClass.checkIfVidExists(path=self.path,title=videoTitle):
                    ytLink.streams.get_audio_only().download(self.path,filename=videoTitle)
                    
                    print(videoTitle + " downloaded!")
                    self.convertToMP3(videoTitle, videoTitle + ".mp3")
                else: 
                    print("Song already exists!")
                    continue    #If vid already exists it just goes to next loop
            except Exception as e:
                print(str(e))
                self.unsuccessfulLinks.append(link)
            
