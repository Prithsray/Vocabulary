import os
from tkinter import *
from tkinter import messagebox as mb
import datetime
import csv
import sounddevice as sd
import soundfile as sf
from tkinter import filedialog
import shutil, os

word1=input("Enter the word ")
#using this because unable to use name from e1 for audio file name 
root = Tk()
root.geometry('520x540')
root.title("Automation Application")
root.configure(background='pink')


# creating labels and entry widgets
# word, description, picture, sound recorder 

l1 = Label(root, text="Automation",width=25,font=("times",20,"bold"),bg='black',fg='white')
l1.place(x=70,y=50)

l2 = Label(root, text="Word",width=20,font=("times",12,"bold"),anchor="w",bg='pink')
l2.place(x=70,y=130)
e1 = Entry(root,width=20,bd=2)
e1.place(x=240,y=130)
word=e1.get()

l3 = Label(root, text="Description",width=20,font=("times",12,"bold"),anchor="w",bg='pink')
l3.place(x=70,y=180)
e2 = Entry(root,width=40,bd=2)
e2.place(x=240,y=180)

################# FOR PICTURE  ############

def Picture():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File", filetypes = (("Image Files","*.jpg*"),("all files","*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    # Change label contents
    
    files = [filename]
    for f in files:
        shutil.move(f, "D:\COLLEGEMATERIALS\Project SR Sir\Vocabulary App\TESTINGVOCAB\TESTINGVOCAB\Image")

l4 = Label(root, text="Picture",width=20,font=("times",12,"bold"),anchor="w",bg='pink')
l4.place(x=70,y=230)


bpic = Button(root,text = "Browse Files",command = Picture) 
label_file_explorer = Label(root,
                            text = "Insert your file here",
                            fg = "blue")
label_file_explorer.place(x=250,y=225) 
bpic.place(x=380,y=225)  

################# FOR SOUND  ############
          
def sound():
    
    fs = 48000
    # seconds
    duration = 5
    myrecording = sd.rec(int(duration * fs),samplerate=fs, channels=2)
    sd.wait()
    # Save as wav file at correct sampling rate
    sf.write("TESTINGVOCAB/Sound/%s.wav"%word1, myrecording, fs)

l4 = Label(root, text="Sound Recorder",width=20,font=("times",12,"bold"),anchor="w",bg='pink')
l4.place(x=70,y=280)

b = Button(text="Record",command=sound)
b.place(x=240, y=280)

################# FOR SAVE  ############

def save():
    word=e1.get()
    description=e2.get()
    data=[[word,description]]
    f=open('Regfile.csv', 'a+' , newline='')
    with f:
        write=csv.writer(f)
        write.writerows(data)
    f.close()
    mb.showinfo('Success', 'Details recorded successfully')
    
################# FOR NOT SAVE  ############

def notsave():
    os.remove("TESTINGVOCAB/Sound/%s.wav"%word1)
    #os.remove("image.png")
    root.destroy()

b1 = Button(root, text='Submit',command=save,width=15,bg='white',fg='green',font=("times",12,"bold"))
b1.place(x=90,y=440)
b2 =Button(root, text='Cancel',command=notsave,width=15,bg='white',fg='red',font=("times",12,"bold"))
b2.place(x=290,y=440)

root.mainloop()

