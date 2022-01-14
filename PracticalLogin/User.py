from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time



class Acces:
    def Login():
        def Ok():
            uname=e1.get()
            password = e2.get()
            file = open("users.txt","r")
            entryun = file.readlines()
            namevar = entryun[0]
            pwvar = entryun[1]
            file.close()
            if (uname == "" and password == ""):
                messagebox.showinfo("Login", "Blank not allowed.")
            elif (uname == namevar.strip() and password==pwvar.strip()):
                messagebox.showinfo("Login","Login Successful")
                time.sleep(2)
                root1.destroy()
            else:
                messagebox.showinfo("Login","Incorrect username or password.")

        root1= Tk()
        root1.title("Login")
        root1.geometry("330x200+800+100")
        global e1
        global e2
        Label(root1, text="Username",padx=20,pady=10).grid(row=0,column=0,columnspan=2)
        Label(root1, text="Password",padx=20,pady=10).grid(row=1,column=0,columnspan=2)

        e1 = Entry(root1,borderwidth=5)
        e1.grid(row=0,column=2,columnspan=2,padx=20,pady=10)

        e2=Entry(root1,borderwidth=5)
        e2.grid(row=1,column=2,columnspan=2,padx=20,pady=10)
        e2.config(show="*")


        Button(root1,text="Login",command=Ok,padx=50,pady=20).grid(row=2,column=1,columnspan=2)
        root1.mainloop()

    def Register():
        def Ok():
            uname = e3.get()
            password = e4.get()
            cpassword = e5.get()
            print(uname)
            print(password)
            print(cpassword)
            if (password == cpassword):
                messagebox.showinfo("Register", "Register Succesful!")
                with open("users.txt", "w") as output_file:
                    output_file.write(f"{uname}\n{password}\n")
                root3.destroy()
            else:
                messagebox.showinfo("Register","Passwords doesnt match!")
                Ok()
        root3=Tk()
        root3.title("Register")
        root3.geometry("400x270+800+100")
        root3.resizable(0, 0)
        global e3
        global e4
        global e5
        Label(root3, text="Username",padx=20,pady=10).grid(row=0,column=0,columnspan=2)
        Label(root3, text="Password",padx=20,pady=10).grid(row=1,column=0,columnspan=2)
        Label(root3, text="Confirm Password",padx=20,pady=10).grid(row=2,column=0,columnspan=2)
        e3 = Entry(root3,borderwidth=5)
        e3.grid(row=0,column=4,columnspan=2,padx=20,pady=10)
        e4=Entry(root3,borderwidth=5)
        e4.grid(row=1,column=4,columnspan=2,padx=20,pady=10)
        e4.config(show="*")
        e5=Entry(root3,borderwidth=5)
        e5.grid(row=2,column=4,columnspan=2,padx=20,pady=10)
        e5.config(show="*")
        registerbutton = Button(root3, text="Register",padx=30,pady=20,command=Ok)
        registerbutton.grid(row=3,column=1,columnspan=4)
        root3.mainloop()


#Acces.Register()