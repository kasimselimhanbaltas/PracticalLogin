import pyautogui as pa
from tkinter import ttk
import webbrowser
import pyautogui as pa
import time
import os
from tkinter import *
import User
from tkinter import messagebox



chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
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
def FindandClick(imgname):
    pa.click(pa.locateCenterOnScreen(imgname,confidence=0.9))
def FindandMove(imgname):
    pa.moveTo(pa.locateCenterOnScreen(imgname,confidence=0.9))
def isOnScreen(imgname,tries):
    errorcount = 0
    while True:
        if pa.locateCenterOnScreen(imgname,confidence=0.8):
            return 1
        else: 
            time.sleep(0.5)
            if errorcount==tries:
                return 0
            errorcount += 1

def Instagram():
    url="www.instagram.com"
    webbrowser.get(chrome_path).open(url);time.sleep(2)
    if HesapKontrol("insta"):
        if isOnScreen('imgdata/instalgcheck.png',5):
            print("Instagram opened, you already logged in.")
        else:
            username,password = GetAccData("insta") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/instath.png',3):
                FindandClick('imgdata/instath.png')
                pa.write(username)
                pa.press('tab')
                pa.write(password)
                pa.press('enter')
                print("Instagram opened and logged in.")
            else:
                print('Instagram opened.')
    else:
        print('Instagram opened.')
def Youtube():
    url="www.youtube.com"
    webbrowser.get(chrome_path).open(url);time.sleep(2)
    if HesapKontrol("yt"):
        if isOnScreen('imgdata/ytali.png',3):
            print("YouTube opened, you already logged in.")
        else:
            username,password = GetAccData("yt") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/ytlogin.png',5):
                FindandClick('imgdata/ytlogin.png')
                if isOnScreen('imgdata/ytlgcheck.png',3):
                    pa.write(username)
                    pa.hotkey('altright','q')
                    pa.write('hotmail.com')
                    pa.press('enter')
                    time.sleep(1)
                    pa.write(password)
                    pa.press('enter')
            if isOnScreen('imgdata/ytverification.png',2):
                print('Youtube opened.')
                print('Logging in to Youtube requires verification. You must continue the progress from here.')
            else:
                print('Youtube opened and logged in.')
    else:
        print('Youtube opened.')
def Twitter():
    url="https://twitter.com/login?lang=tr"
    webbrowser.get(chrome_path).open(url);time.sleep(2)
    if HesapKontrol("twtr"):
        if isOnScreen('imgdata/twlgchceck.png',3):
            print('Twitter opened, you already logged in.')
        else:
            username,password = GetAccData("tw") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/twlogin.png',5):
                FindandClick('imgdata/twlogin.png')
                pa.write(username)
                pa.press('enter')
                time.sleep(2)
                pa.write(password)
                pa.press('enter')
                time.sleep(2)
                print('Twitter opened and logged in.')
            else:
                print('Twitter opened.')
    else:
        print('Twitter opened.')
def Github():
    url = "https://github.com/login"
    webbrowser.get(chrome_path).open(url)
    if HesapKontrol("gh"):
        if isOnScreen('imgdata/gitcheck.png',3):
            print('Twitter opened, you already logged in.')
        else:
            username,password = GetAccData("gh") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/gitlgcheck.png',5):
                pa.write(username)
                pa.press('tab')
                pa.write(password)
                pa.press('enter')
                print('GitHub opened and logged in.')
            else:
                print('GitHub opened.')
    else:
        print('Github opened.')
def Stack():
    url = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"
    webbrowser.get(chrome_path).open(url)
    if HesapKontrol("stack"):
        if isOnScreen('imgdata/stackcheck.png',3):
            print('Twitter opened, you already logged in.')
        else:
            username,password = GetAccData("stack") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/soflg.png',5):
                FindandClick('imgdata/soflg.png')
                pa.write(username)
                pa.hotkey('altright','q')
                pa.write('gmail.com')
                pa.press('tab')
                pa.write(password)
                pa.press('enter')
                print('Stackoverflow opened and logged in.')
            else:
                print('Stackoverflow opened.')
    else:
        print('StackOverflow opened.')
def Twitch():
    url = "https://www.twitch.tv/login"
    webbrowser.get(chrome_path).open(url)
    if HesapKontrol("twtch"):
        if isOnScreen('imgdata/twali.png',3):
            print('Twitch opened, you already logged in.')
        else:
            username,password = GetAccData("twtch") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/twitchlgcheck.png',3):
                #FindandClick('imgdata/twitchlgcheck.png')
                pa.write(username)
                pa.press('tab')
                pa.write(password)
                pa.press('enter');time.sleep(1)
            #if isOnScreen('imgdata/stackcheck.png',5):
            if isOnScreen('imgdata/twitchconfirmation.png',2):
                print('Twitch opened.')
                print('Logging in to Twitch requires verification. You must continue the progress from here.')
            else:
                print('Twitch opened and logged in.')
    else:
        print('Twitch opened.')
def Ues():
    url = "https://ues.marmara.edu.tr/Account/LoginBefore"
    webbrowser.get(chrome_path).open(url)
    if HesapKontrol("ues"):
        if isOnScreen('imgdata/uesali.png',3):
            print("Ues opened, you already logged in.")
        else:  
            username,password = GetAccData("ues") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/ueslgcheck2.png',3):
                pa.write(password)
                pa.press('enter')
                print('Ues opened and logged in.')
            if isOnScreen('imgdata/ueslgcheck.png',3):
                FindandClick('imgdata/ueslgcheck.png')
                pa.write(username)
                pa.press('enter')
                if isOnScreen('imgdata/ueslgcheck2.png',3):
                    pa.write(password)
                    pa.press('enter')
                    print('Ues opened and logged in.')
                else:
                    print('Ues opened')
            else:
                print('Ues opened.')
    else:
        print('Ues opened.')
def Bys():
    url = "https://bys.marmara.edu.tr/v2/Account/Login?ReturnUrl=%2Fv2%2F"
    webbrowser.get(chrome_path).open(url)
    if HesapKontrol("bys"):
        if isOnScreen('imgdata/bysali.png',3):
            print('Ues opened, you already logged in.')
        else:
            if isOnScreen('imgdata/byslgcheck.png',5):
                username,password = GetAccData("bys") 
                username=str(username)
                password=str(password)
                pa.write(username)
                pa.press('tab')
                pa.write(password)
                pa.press('enter')
                print('Bys opened and logged in.')
            else:
                print('Bys opened.')
    else:
        print('Bys opened.')
def LinkedIn():
    url = "https://www.linkedin.com/login/tr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    webbrowser.get(chrome_path).open(url)
    if HesapKontrol("li"):
        if isOnScreen('imgdata/liali.png',3):
            print('LinkedIn opened, you already logged in.')
        else:
            username,password = GetAccData("li") 
            username=str(username)
            password=str(password)
            if isOnScreen('imgdata/linkedinlgcheck.png',3):
                pa.moveTo(pa.locateCenterOnScreen('imgdata/lilger.png',confidence=0.8))
                pa.click(pa.moveRel(0,30))
                pa.hotkey('ctrl','a')
                pa.write(username)
                pa.hotkey('altright','q')
                pa.write('gmail.com')
                pa.press('tab')
                pa.write(password)
                pa.press('enter')
                print('LinkedIn opened and logged in.')
            else:
                print('LinkedIn opened.')
    else:
        print('LinkedIn opened.')
    



def Wikipedia():
    url="https://tr.wikipedia.org/wiki/Anasayfa"
    webbrowser.get(chrome_path).open(url)
def Google():
    url="https://www.google.com.tr/"
    webbrowser.get(chrome_path).open(url)
def WhatsApp():
    url="https://web.whatsapp.com/"
    webbrowser.get(chrome_path).open(url)

