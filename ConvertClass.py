import os
import validators

class ConvertClass:
    def __init__(self, links, path,unsuccessfulLinks):
        self.links = links  #links is a list that holds all youtube links
        self.path = path    #path is the output path where the vids will be downloaded
        self.unsuccessfulLinks = unsuccessfulLinks  #Here links of vids that were unsuccesfull will be stored
        
    def checkIfVidExists(path, title):  #If vid with title exists in folder it skips 
        return os.path.exists(path + "\\" + title) or os.path.exists(path + "\\" + title + ".mp3")\
               or os.path.exists(path + "\\" + title + ".mp4")                                   #^ Backslash indicates that code continues on next line
        
    def doConversion(self):
        raise NotImplementedError("Well this isn't supposed to happen is it")

    def setPath(self,newPath):
        self.path = newPath
        
    def __str__(self):  #For testing
        return "Links are: " + '||'.join(self.links) + ". And path selected is: " + self.path
    
    def unsuccessfulLinksToString(self):
        return "Links are: \n" + self.unsuccessfulLinks
    
    def isLinkValid(link):
        valid = validators.url(link)
        return valid