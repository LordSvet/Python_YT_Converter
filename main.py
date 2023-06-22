import customtkinter as ctinker
import tkinter
from tkinter import ttk
from threading import Thread
from ConvertMP3 import ConvertMP3
from ConvertMP4 import ConvertMP4



#Some global variables
links = []
pathSelected = None
converterObject = None
unsuccessfulLinks = []

def openCompleteWindow():
    window = ctinker.CTkToplevel()
    window.geometry("300x200")
    windowLabel = ctinker.CTkLabel(window,text="Download Complete!")
    windowLabel.pack()
    if len(converterObject.unsuccessfulLinks)>0:
        unsuccessfulLinksLabel = ctinker.CTkLabel(window,text="Some of these links returned an error. Please try again :(")
        unsuccessfulLinksLabel.pack()
    window.transient(master=root)
    
    
def wrongLink():
    window = ctinker.CTkToplevel()
    window.geometry("300x200")
    windowLabel = ctinker.CTkLabel(window,text="Please insert a valid link!")
    windowLabel.pack()
    window.transient(master=root)


#Method that checks if a path has been selected, converting mdoe has been selected and at least one link is existing in the list so that the convert button can be enabled
def prerequisitesMet():
    return pathSelected != None and convertOption.get() != "Select Conversion Type" and linksListBox.size()>0

#Method gets called when user has inserted something in the entry and clicked Enter
#The inserted link is added to the links list and to the ListBox for links
def enterWasPressed(link):
    link = textEntry.get()
    if not ConvertMP3.isLinkValid(link):
        textEntry.delete(0,'end')
        wrongLink()
        return
    links.append(link)
    textEntry.delete(0,'end')
    linksListBox.insert(tkinter.END,link)
    if prerequisitesMet():
        convertButton.configure(state="normal")
    
    
#Method gets called when user has deleted one or more items in the ListBox
#Removes the entry from the ListBox and also from the links List
def linkWasDeleted(selectedLinks):
    selectedLinks = linksListBox.curselection()
    for link in reversed(selectedLinks):
        links.remove(linksListBox.get(link))
        linksListBox.delete(link)

#I know it looks like this method is copy pasted from the last one but buttonClick command doesn't require arguments while the key bind does
def deleteButtonOnclick():
    selectedLinks = linksListBox.curselection()
    for link in reversed(selectedLinks):
        links.remove(linksListBox.get(link))
        linksListBox.delete(link)
         

def getDownloadDir():   #User selects path for download and it is saved in var pathSelected
    global pathSelected
    pathSelected = ctinker.filedialog.askdirectory()
    if prerequisitesMet():
        convertButton.configure(state="normal")
    
    
def conversionOptionSelected(value):
    if prerequisitesMet():
        convertButton.configure(state="normal")
        
    
def conversion(): 
    global converterObject
    if convertOption.get()=='MP3':
        converterObject = ConvertMP3(links,pathSelected,unsuccessfulLinks)
    elif convertOption.get()=='MP4':
        converterObject = ConvertMP4(links,pathSelected,unsuccessfulLinks)
    converterObject.doConversion()
    
    for link in links:
        links.remove(link)
    linksListBox.delete(0,ctinker.END)
    progressBar.stop()
    progressBar.set(0)
    openCompleteWindow()
    
        

def timeToConvertBitches():
    progressBar.start()
    thread = Thread(target=conversion)    #Runs the target command on a different thread so that the GUI doesn't freeze while downloading
    thread.start()
    




#First defining system settings
ctinker.set_appearance_mode("dark")
ctinker.set_default_color_theme("dark-blue")

root = ctinker.CTk()
root.title("YouTube Downloader")

#Defining ListBox which is inside root
linksListBox = tkinter.Listbox(master=root, selectmode=tkinter.EXTENDED)
linksListBox.grid(row=0,column=0,padx=20,pady=10,sticky="NSEW")

#Defining the frame that will hold the buttons and comboBox
frame = ctinker.CTkFrame(master=root)
frame.grid(row=1,column=0,sticky="NSEW")


#Making buttons which will be included in frame

#Defining the button that removes selected entries from the list
removeButton = ctinker.CTkButton(master=frame, text="Delete Selected Items",command=deleteButtonOnclick)
removeButton.grid(row=0,column=0,padx=20,pady=10)

#Defining the button that starts the conversion process
convertButton = ctinker.CTkButton(master=frame, text="Convert & Download",command=timeToConvertBitches,state='disabled')
convertButton.grid(row=0,column=1,padx=20,pady=10)

#Defining the ComboBox which will have two options: Convert to MP3 or to MP4
convertOption = ttk.Combobox(master=frame, values=["MP3","MP4"],state='readonly')
convertOption.bind('<<ComboboxSelected>>', conversionOptionSelected)
convertOption.set("Select Conversion Type")
convertOption.grid(row=0,column=2,padx=20,pady=10)

#Defining the button that selects the path where the vids will be downloaded
selectPath = ctinker.CTkButton(master=frame,text="Choose Download Location",command=getDownloadDir)
selectPath.grid(row=0,column=3,padx=20,pady=10)

#Defining the text entry which is where the user will input the new links to youtube vids
textEntry = ctinker.CTkEntry(master=root,width=600,height=50)
textEntry.grid(row=2,column=0,pady=20,padx=15,sticky="NSEW")

#Defining a progress bar for whilst downloading
progressBar = ctinker.CTkProgressBar(root,orientation="horizontal",mode="indeterminate",width=500,height=20)
progressBar.grid(row=3,column=0,pady=20,padx=15)
progressBar.set(0)


#Grid Configurations
root.rowconfigure(0,weight=3);
root.columnconfigure(0,weight=3);

frame.rowconfigure(0,weight = 1)
frame.columnconfigure(0,weight=1);
frame.columnconfigure(1,weight=1);
frame.columnconfigure(2,weight=1);
frame.columnconfigure(3,weight=1);



#Setting style setting for the ListBox and binding the Delete and Backspace keys so it deletes entries
linksListBox.configure(background="darkgrey",font=('Comic Sans MS',15))
linksListBox.bind('<Delete>', linkWasDeleted)
linksListBox.bind('<BackSpace>', linkWasDeleted)


#Binding the Enter key so it adds a link to the ListBox on clicking enter
textEntry.bind('<Return>',enterWasPressed)

#mainloop makes the GUI run
root.mainloop()

