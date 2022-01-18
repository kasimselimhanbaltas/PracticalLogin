import webbrowser
import pyautogui as pa
import time
import os
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import Components
import User

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

comps = []
    
#Satir sayisini tespit etme
def satirsayisi():
    with open ("users.txt","r") as file:
        count = 0
        for line in file:
            count+=1
    return count
#Girilen hesap dosyada kayıtlı iise 1 değilse 0 döndürür
def HesapKontrol(accname):
    file = open("users.txt","r")
    r = file.readlines()
    for i in range(satirsayisi()):
        if r[i].strip()==accname:
            return 1
    else:
        return 0
#Hesap dosyada yoksa girilen parametreleri ekle
def writeAcc(acc,uname,pw):
    file =open ("users.txt","a")
    file.write(f"{acc}\n{uname}\n{pw}\n")
    file.close()

#Hesap mevcut ise username ve passwordu al
def GetAccData(acc):
    file =open ("users.txt","r")
    r = file.readlines()
    mevcut = 0
    for i in range(satirsayisi()):
        if acc==r[i].strip():
            uname1 = r[i+1].strip()
            pw1 = r[i+2].strip()
            mevcut+=1
            return str(uname1),str(pw1)
    if mevcut == 0:
        return 0,0
    file.close()
    

def AddAcc(acc):
    def Ok():
        def saveAcc():
            uname = e3.get()
            password = e4.get()
            writeAcc(acc,uname,password)
            messagebox.showinfo("Account","Account saved!")
            root4.destroy()
        root4=Tk()
        root4.title("Add Account")
        root4.geometry("400x250+800+85")
        root4.resizable(0, 0)
        global e3
        global e4
        global e5
        Label(root4, text="Username",padx=20,pady=10).grid(row=0,column=0,columnspan=2)
        Label(root4, text="Password",padx=20,pady=10).grid(row=1,column=0,columnspan=2)
        e3 = Entry(root4,borderwidth=5)
        e3.grid(row=0,column=4,columnspan=2,padx=20,pady=10)
        e4=Entry(root4,borderwidth=5)
        e4.grid(row=1,column=4,columnspan=2,padx=20,pady=10)
        e4.config(show="*")
        registerbutton = Button(root4, text="Save Account",padx=30,pady=20,command=saveAcc)
        registerbutton.grid(row=3,column=1,columnspan=4)
        root4.mainloop()
        
    if HesapKontrol(acc) != 1:#Saving accounts
        Ok()
    else:#Already registered
        messagebox.showinfo("Account","You already registered for this component.")
    
def AddAcc1():
    AddAcc("insta")
def AddAcc2():
    AddAcc("twtr")
def AddAcc3():
    AddAcc("yt")
def AddAcc4():
    AddAcc("gh")
def AddAcc5():
    AddAcc("stack")    
def AddAcc6():
    AddAcc("twtch")    
def AddAcc7():
    AddAcc("ues")    
def AddAcc8():
    AddAcc("bys") 
def AddAcc9():
    AddAcc("li")  
         
def Main():
    def EditList():
        def GetValues():
            if i.get():
                comps.append('insta')
            if i2.get()==1:
                comps.append('yt')
            if i3.get()==1:
                comps.append('twtr')
            if i4.get()==1:
                comps.append('gh')
            if i5.get()==1:
                comps.append('stack')
            if i6.get()==1:
                comps.append('twtch')
            if i7.get()==1:
                comps.append('ues')
            if i8.get()==1:
                comps.append('bys')
            if i9.get()==1:
                comps.append('li')
            if i10.get()==1:
                comps.append('wp')
            if i11.get()==1:
                comps.append('ggl')
            if i12.get()==1:
                comps.append('wik')
        def comOk():
            GetValues()
            root.destroy()
            placement()

        #root2.withdraw()
        root = Toplevel(root2)
        root.title('Edit The List')
        root.geometry('300x800+800+85')

        myFont = font.Font(size=15)
        i=IntVar()
        c = Checkbutton(root, padx=10, text="Instagram", variable=i)
        i2=IntVar()
        c2 = Checkbutton(root, padx=10, text="Youtube", variable=i2)
        i3=IntVar()
        c3 = Checkbutton(root, padx=10, text="Twitter", variable=i3)
        i4=IntVar()
        c4 = Checkbutton(root, padx=10, text="Github", variable=i4)
        i5=IntVar()
        c5 = Checkbutton(root, padx=10, text="StackOverflow", variable=i5)
        i6=IntVar()
        c6 = Checkbutton(root, padx=10, text="Twitch", variable=i6)
        i7=IntVar()
        c7 = Checkbutton(root, padx=10, text="Ues", variable=i7)
        i8=IntVar()
        c8 = Checkbutton(root, padx=10, text="Bys", variable=i8)
        i9=IntVar()
        c9 = Checkbutton(root, padx=10, text="LinkedIn", variable=i9)
        i10=IntVar()
        c10 = Checkbutton(root, padx=10, text="WhatsApp", variable=i10)
        i11=IntVar()
        c11 = Checkbutton(root, padx=10, text="Google", variable=i11)
        i12=IntVar()
        c12 = Checkbutton(root, padx=10, text="Wikipedia", variable=i12)

        accInsta = Button(root, text= "Account", padx=30,pady=4,command=AddAcc1)
        accTwitter = Button(root, text= "Account", padx=30,pady=4,command=AddAcc2)
        accYoutube = Button(root, text= "Account", padx=30,pady=4,command=AddAcc3)
        accGithub = Button(root, text= "Account", padx=30,pady=4,command=AddAcc4)
        accStack = Button(root, text= "Account", padx=30,pady=4,command=AddAcc5)
        accTwitch = Button(root, text= "Account", padx=30,pady=4,command=AddAcc6)
        accUes = Button(root, text= "Account", padx=30,pady=4,command=AddAcc7)
        accBys = Button(root, text= "Account", padx=30,pady=4,command=AddAcc8)
        accLinkedIn = Button(root, text= "Account", padx=30,pady=4,command=AddAcc9)

        butOK = Button(root, text='Tamam', padx=5, pady=10, command=comOk)

        accInsta['font'] = myFont
        accTwitter['font'] = myFont
        accYoutube['font'] = myFont
        accGithub['font'] = myFont
        accStack['font'] = myFont
        accTwitch['font'] = myFont
        accUes['font'] = myFont
        accBys['font'] = myFont
        accLinkedIn['font'] = myFont
        butOK['font'] = myFont

        #Grid placement

        c.grid(row=1,column=0)
        c2.grid(row=2,column=0) 
        c3.grid(row=3,column=0)
        c4.grid(row=4,column=0)
        c5.grid(row=5,column=0)
        c6.grid(row=6,column=0)
        c7.grid(row=7,column=0)
        c8.grid(row=8,column=0)
        c9.grid(row=9,column=0)
        c10.grid(row=10,column=0,columnspan=2)
        c11.grid(row=11,column=0,columnspan=2)
        c12.grid(row=12,column=0,columnspan=2)


        accInsta.grid(row=1,column=1)
        accYoutube.grid(row=2,column=1)
        accTwitter.grid(row=3,column=1)
        accGithub.grid(row=4,column=1)
        accStack.grid(row=5,column=1)
        accTwitch.grid(row=6,column=1)
        accUes.grid(row=7,column=1)
        accBys.grid(row=8,column=1)
        accLinkedIn.grid(row=9,column=1)

        butOK.grid(row=13,column=0,columnspan=2)

        root.mainloop()
    
    root2=Tk()
    root2.title("PracticalLogin")
    root2.geometry("450x800+800+85")
    root2.resizable(0, 0)

    # configure the grid
    root2.columnconfigure(0, weight=1)
    #root2.columnconfigure(1, weight=1)

    def Execute():
        if j1.get()==1:
            Components.Instagram()
        if j2.get()==1:
            Components.Youtube()
        if j3.get()==1:
            Components.Twitter()
        if j4.get()==1:
            Components.Github()
        if j5.get()==1:
            Components.Stack()
        if j6.get()==1:
            Components.Twitch()
        if j7.get()==1:
            Components.Ues()
        if j8.get()==1:
            Components.Bys()
        if j9.get()==1:
            Components.LinkedIn()
        if j10.get()==1:
            Components.WhatsApp()
        if j11.get()==1:
            Components.Google()
        if j12.get()==1:
            Components.Wikipedia()

    #button creation
    myFont = font.Font(size=15)
    j1=IntVar()
    c = Checkbutton(root2, text="Instagram", variable=j1)
    j2=IntVar()
    c2 = Checkbutton(root2, text="Youtube", variable=j2)
    j3=IntVar()
    c3 = Checkbutton(root2, text="Twitter", variable=j3)
    j4=IntVar()
    c4 = Checkbutton(root2, text="Github", variable=j4)
    j5=IntVar()
    c5 = Checkbutton(root2, text="StackOverflow", variable=j5)
    j6=IntVar()
    c6 = Checkbutton(root2, text="Twitch", variable=j6)
    j7=IntVar()
    c7 = Checkbutton(root2, text="UES", variable=j7)
    j8=IntVar()
    c8 = Checkbutton(root2, text="BYS", variable=j8)
    j9=IntVar()
    c9 = Checkbutton(root2, text="LinkedIn", variable=j9)
    j10=IntVar()
    c10 = Checkbutton(root2, text="WhatsApp", variable=j10)
    j11=IntVar()
    c11 = Checkbutton(root2, text="Google", variable=j11)
    j12=IntVar()
    c12 = Checkbutton(root2, text="Wikipedia", variable=j12)


    editButton = Button(root2,text='Edit Components',width=10,padx=40,pady=20,command=EditList)
    but= Button(root2, text= "Execute",width=10, padx=40,pady=20,command=Execute)
    exitButton = Button(root2, text='Exit',width=10,padx = 40,pady=20,command=root2.destroy)

    c['font'] = myFont
    c2['font'] = myFont
    c3['font'] = myFont
    c4['font'] = myFont
    c5['font'] = myFont
    c6['font'] = myFont
    c7['font'] = myFont
    c8['font'] = myFont
    c9['font'] = myFont
    c10['font'] = myFont
    c11['font'] = myFont
    c12['font'] = myFont

    but['font'] = myFont
    editButton['font'] = myFont
    exitButton['font'] = myFont


    #button placement
    editButton.grid(row=0,column=0,columnspan=2)
    def placement():
        i = 1
        if "insta" in comps:
            c.grid(row=i,column=0);i+=1
        if "yt" in comps:
            c2.grid(row=i,column=0);i+=1
        if "twtr" in comps:
            c3.grid(row=i,column=0);i+=1
        if "gh" in comps:
            c4.grid(row=i,column=0);i+=1
        if "stack" in comps:
            c5.grid(row=i,column=0);i+=1
        if "twtch" in comps:
            c6.grid(row=i,column=0);i+=1
        if "ues" in comps:
            c7.grid(row=i,column=0);i+=1
        if "bys" in comps:
            c8.grid(row=i,column=0);i+=1
        if "li" in comps:
            c9.grid(row=i,column=0);i+=1
        if "wp" in comps:
            c10.grid(row=i,column=0);i+=1
        if "ggl" in comps:
            c11.grid(row=i,column=0);i+=1
        if "wik" in comps:
            c12.grid(row=i,column=0);i+=1
        but.grid(row=14,column=0,columnspan=2);i+=1
        exitButton.grid(row=15,column=0,columnspan=2);i+=1
    placement()
    root2.mainloop()



