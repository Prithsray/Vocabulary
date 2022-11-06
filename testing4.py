import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#importing tkinter after pil gives error
from PIL import Image
from playsound import playsound

vocabfile = open("data1.csv","r")
vocabdata= vocabfile.readlines()
random.shuffle(vocabdata)

def check(new_word,pic):
    if new_word==pic:
        messagebox.showinfo("result", "Correct!")
        gui.destroy()
        
    else:
        messagebox.showinfo("result", "Incorrect!" )
        gui.destroy()
        print("Correct meaning of the word should be: "+description)
        print("The correct picture and pronunciation is given- ")  
        myImage = Image.open("H:/Programming/TESTINGVOCAB/Image/"+new_word+".png"); 
        myImage.show();
        myImage.close();
            
        playsound("Sound/"+new_word+".wav")


#first part
for i in range(3):
        x = vocabdata[i].strip()
        data = x.split(",\"")     
        new_word = data[0]
        description = data[1]  
        #add others, antonyms, rhyming words, similar words etc in database        
        #question=input() #questions appear from database or others
        #print(new_word) 

        pic=[]
        j=0
        while j in range(4):
            xj = vocabdata[j].strip()
            dataj = xj.split(",\"")     
            option = dataj[0]
            #print(option)
            pic.append(dataj[0])
            j+=1
        pic.append(new_word)
        random.shuffle(pic)
        picnew=set(pic) #to remove duplicates
        pic=list(picnew)

        gui = Tk(className='Questions') #the window
        gui.geometry("1000x500")
        gui.configure(bg='#333738')
        l=Label(gui,text="Choose the correct picture. Which is the "+new_word+"?" ).pack() #label widget
        pic0=pic[0]
        pic1=pic[1]
        pic2=pic[2]
        pic3=pic[3]
        photo=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic0+".png")
        Button(gui, image = photo, command=lambda:check(new_word,pic0)).place(x=0, y=250) #picture on the button
        photo1=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic1+".png")
        Button(gui, image = photo1, command=lambda:check(new_word,pic1)).place(x=0, y=25)     
        photo2=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic2+".png")
        Button(gui, image = photo2, command=lambda:check(new_word,pic2)).place(x=250, y= 25) 
        photo3=PhotoImage(file=r"H:/Programming/TESTINGVOCAB/Image/"+pic3+".png")
        Button(gui, image = photo3, command=lambda:check(new_word,pic3)).place(x=250, y=250) 

        gui.mainloop()   

