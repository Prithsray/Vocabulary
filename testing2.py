#currently working
#same pic appears sometimes > solved
import random

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

#importing tkinter after pil gives error
from PIL import Image

from playsound import playsound

def check(question,pic):
        if pic==question:
            messagebox.showinfo("result", "Correct!")
        else:
            #answer='N'
            messagebox.showinfo("result", "Incorrect!")


def gui(question):
    vocabfile = open("data1.csv","r")
    vocabdata= vocabfile.readlines()
    random.shuffle(vocabdata)
    pic=[]
    j=0
    while j in range(4):
        xj = vocabdata[j].strip()
        dataj = xj.split(",,")     
        option = dataj[0]
        #print(option)
        pic.append(dataj[0])
        j+=1
    pic.append(question)
    random.shuffle(pic)

    picnew=set(pic) #to remove duplicates
    pic=list(picnew)

    gui = Tk(className='Questions') #the window
    gui.geometry("1000x500")
    gui.configure(bg='#333738')

    l=Label(gui,text="Choose the correct picture" ).pack() #label widget
    pic0=pic[0]
    pic1=pic[1]
    pic2=pic[2]
    pic3=pic[3]
    photo=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic0+".png")
    Button(gui, image = photo, command=lambda:check(question,pic0)).place(x=0, y=250) #picture on the button

    photo1=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic1+".png")
    Button(gui, image = photo1, command=lambda:check(question,pic1)).place(x=0, y=25) #picture on the button
    
    photo2=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic2+".png")
    Button(gui, image = photo2, command=lambda:check(question,pic2)).place(x=250, y= 25) #picture on the button
    
    photo3=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic3+".png")
    Button(gui, image = photo3, command=lambda:check(question,pic3)).place(x=250, y=250) #picture on the button

    gui.mainloop()     
#gui()

def vocab():

    vocabfile = open("data1.csv","r")

    vocabdata= vocabfile.readlines()

    random.shuffle(vocabdata)
    for i in range(3):

        x = vocabdata[i].strip()
        data = x.split(",,")     

        question = data[0]

        CorrectAnswer = data[1]  

        print(question)

        answer = input("Do you know the word? Y/N ")

        if answer == "Y":
            print("OK!")
            #pic.append(question) 
            
            gui(question)

        elif answer == "N":
            print("Incorrect.")
            print("Correct answer should be: "+CorrectAnswer)  
            myImage = Image.open("H:/Programming/TESTINGVOCAB/Image/"+question+".png"); 
            myImage.show();
            myImage.close();
            
            playsound("Sound/"+question+".wav")
            
        print()
          

vocab()
