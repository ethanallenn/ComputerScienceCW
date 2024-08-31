import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def initscreen(self):

    self.MainScreen.title("Admin Panel")
    self.MainScreen.configure(background = "#ffff00")
    self.pack(fill=BOTH, expand=1)

    RegisterButton = Button(self, text="Register", bg = "blue", fg = "White",command=self.User_Register)
    RegisterButton.place(x=200, y=100)

    LoginButton = Button(self, text="Login", bg = "blue", fg = "white",command=self.User_Login)
    LoginButton.place(x=270, y=100)

def User_Register(self):
    Firstname = Label(application, text="First name: ", bg = "blue", fg = "white")
    Firstname.grid(row=30, column=7)

    Surname = Label(application, text="Surname: ", bg = "blue", fg = "white")
    Surname.grid(row=30, column=10)

    Emailtag=Label(application,text="Email address: ", bg= "yellow", fg= "red")
    Emailtag.grid(row=15, column=7)

    Password = Label(application, text="Password: ", bg = "blue" fg = "white")
    Password.grid(row=35, column=7)

    SubmitButton=Button(self,text="Submit",bg="red",fg="yellow",command=self.File_Manipulation)
    SubmitButton.place(x=140, y=100)

    EntryBox1 = Entry(application)
    EntryBox1.grid(row=30, column=12)

    EntryBox2 = Entry(application)
    EntryBox2.grid(row=30, column=8)

    EntryBox3 = Entry(application)
    EntryBox3.grid(row=15, column=8)

    EntryBox4 = Entry(application)
    EntryBox4.grid(row=35, column=8)

    global EntryBox1
    global EntryBox2
    global EntryBox3
    global EntryBox4

def File_Manipulation(self):
    with open("ClientData.txt", "w+")as Client_File:
        EB=EntryBox1.get()
        EB2=EntryBox2.get()
        EB3=EntryBox3.get()
        EB4=EntryBox4.get()
        infocombo=EB 