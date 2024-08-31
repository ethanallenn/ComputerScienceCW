import tkinter
from tkinter import messagebox
from tkinter import *

def makeWindow():
    global titleVar, genreVar, directorVar, leadactorVar, durationVar, releasedateVar, certificateVar, is3dVar
    
    win = Tk()
    
    frame1 = Frame(win)
    frame1.grid(row=1, column=0, padx=5, pady=5)
    
    Label(frame1, text="Title goes here.", font=("Helvetica 12 bold"))
    Label.grid(row=0, column=0)
    
    Label(frame1, text="Title")