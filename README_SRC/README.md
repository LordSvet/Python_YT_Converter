 # Youtube MP3/MP4 Converter made in Python
I decided to make a YouTube video converter mainly to help me setup custom song radio's in games. It is free to use just download the repository by clicking <b>Code -> Download ZIP</b> 

 # Libraries used:
    - PyTube for downloading and converting the youtube video
    - moviepy for converting the MP4 file to MP3 on the disk
    - validators to validate if a URL is legit or not
    - os for removing, renaming files/directories
    - tkinter and customtkinter for the GUI

# Instructions:
1. Run the main.exe file and screen should look like this:
![StartImage](./images/1.FirstScreen.PNG)
2. In the text box on the bottom you can insert any YouTube video link and click the 'Enter' button on your keyboard to insert it in the list and then it will appear on the top. Looks like this:
![SecondExampleImage](./images/2.LinksInsertedExample.PNG)
3. In this list you can select one or more links and remove them from the list by either clicking the "Delete Selected Items" button in the window or the Delete or Backspace button on your keyboard.
Afterwards you have to choose the conversion type to either MP3 or MP4 from the dropdown menu saying "Select Conversion Type" and also the download location where the files will be stored by clicking "Choose Download Location".
4. After those two are selected the "Convert & Download" button should enable itself and once you click it the program will start working on the videos you've added. If the "Convert & Download" button is still disabled/greyed out then make sure you have fulfilled these requirements:
    - You have inserted at least one link and it is visible in the list
    - You have selected the conversion type to either MP3 or MP4
    - You have chose a download location
 
 5. Once the download is complete it should show a pop-up window like this:
 ![DownloadComplete](./images/5.Success.PNG)

 If There is an issue with one or more of the links you will see this screen:
 ![DownloadError](./images/4.Error.PNG)