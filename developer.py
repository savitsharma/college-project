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


class developer():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        img_top=Image.open(r"images\developer_1.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720) 



        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)


        img_top1=Image.open(r"images\developer_2 (2).jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=345,y=15,width=150,height=200) 


        # img_top2=Image.open(r"images\developer_2.jpg")
        # img_top2=img_top2.resize((1530,720),Image.ANTIALIAS)
        # self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        # f_lbl2=Label(main_frame,image=self.photoimg_top2)
        # f_lbl2.place(x=1000,y=0,width=500,height=600)



    # ======== DEVELOPER INFO ===================== 
        student_name_label=Label(main_frame,text="Hello, my name is, Pranjal ",font=("times new roman",20,"bold"),bg="white",fg="green")
        student_name_label.place(x=0,y=5)  

        student_name_label=Label(main_frame,text="I am the developer of this  ",font=("times new roman",20,"bold"),bg="white",fg="green")
        student_name_label.place(x=0,y=40)   

        student_name_label=Label(main_frame,text="project ",font=("times new roman",20,"bold"),bg="white",fg="green")
        student_name_label.place(x=0,y=75)   


        
        img_top2=Image.open(r"images\developer_2.jpg")
        img_top2=img_top2.resize((500,390),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl2=Label(main_frame,image=self.photoimg_top2)
        f_lbl2.place(x=0,y=210,width=500,height=390)







if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()                             