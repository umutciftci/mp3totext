import split_file
import mp3towav
from split_file import *
import speech_recognition as sr
import os


for x in range(1,counter):
    AUDIO_FILE = ("/full/path/filename/chunk%d.wav" % (x,)) 
    
    # use the audio file as the audio source 
    
    r = sr.Recognizer() 
    
    with sr.AudioFile(AUDIO_FILE) as source: 
        #reads the audio file. Here we use record instead of 
        #listen 
        audio = r.record(source)   
    result = r.recognize_google(audio)
    try:
        with open("outputs.txt","a") as f:
            f.write(result+ '\n') 
        print("%d. audio file is done." % (x,)) 
    
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
    
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 


for i in range(1,counter):
    if os.path.exists("/full/path/chunk%d.wav" % (i,)):
        os.remove("/full/path/chunk%d.wav" % (i,))
    else:
        print("The file does not exist")
print("Files are deleted.")
print("Process completed.")