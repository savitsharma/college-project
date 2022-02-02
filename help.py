from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from turtle import up
from PIL import ImageTk, Image
  
  
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]


class help():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        img_top=Image.open(r"images\help.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720) 

        title_lbl=Label(f_lbl,text="Email: pranjaldude2000@gmail.com",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=500,y=300)




if __name__=="__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()                                     