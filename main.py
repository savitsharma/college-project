from cgitb import text
import string
from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image
import tkinter  
from time import strftime  
from datetime import datetime    
from tkinter import filedialog

from student import student
import os
from train import train
from face_recoginzation import Face_recogination
from attendence import attendence
from developer import developer
from help import help



class Face_Recogination_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")

       
      


        # first image 


        img1=Image.open(r"C:\Users\HP\Desktop\final year project\images\a.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130) 

        
        
        
        
        
        # second image
        
        img2=Image.open(r"C:\Users\HP\Desktop\final year project\images\b.jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130) 

        
        
        
        
        
        # third image
        
        img3=Image.open(r"C:\Users\HP\Desktop\final year project\images\c.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130) 
  
        

        #  bg image


        img4=Image.open(r"C:\Users\HP\Desktop\final year project\images\bg image.jfif")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710) 


        # title

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        
        # time

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"italic"),bg="white",fg="green")    
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        # student button


        img5=Image.open(r"C:\Users\HP\Desktop\final year project\images\students.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220) 

        b1_1=Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40) 


        # detect face button


        img6=Image.open(r"C:\Users\HP\Desktop\final year project\images\face detection.jfif")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220) 

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40) 


        
        
        # attendence button


    


        img7=Image.open(r"C:\Users\HP\Desktop\final year project\images\attendence.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=100,width=220,height=220) 

        b1_1=Button(bg_img,text="Attendence",command=self.attendence_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40) 


        # helpdesk button

        img8=Image.open(r"C:\Users\HP\Desktop\final year project\images\help desk.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220) 

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40) 



        # training button

        img9=Image.open(r"C:\Users\HP\Desktop\final year project\images\training.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220) 

        b1_1=Button(bg_img,text="Training",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40) 

 
        
        # photos face button

        
        img10=Image.open(r"C:\Users\HP\Desktop\final year project\images\photos.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220) 

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img ,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40) 


        # developer face button

        
        img11=Image.open(r"C:\Users\HP\Desktop\final year project\images\developer.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220) 

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40) 


        # exit button

        
        img12=Image.open(r"C:\Users\HP\Desktop\final year project\images\exit.png")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.exit_data)
        b1.place(x=1100,y=380,width=220,height=220) 

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.exit_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40) 

    
    def open_img(self):
        os.startfile("data")




    # ============== functions buttons================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recogination(self.new_window)


    def attendence_data(self):    
        self.new_window=Toplevel(self.root)
        self.app=attendence(self.new_window)

    def developer_data(self):    
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)  


    def help_data(self):    
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)        

    
    def exit_data(self):
        self.exit=tkinter.messagebox.askyesno("face recogination","Are you sure you want to exit this project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return    






if __name__=="__main__":
    root=Tk()
    obj=Face_Recogination_system(root)
    root.mainloop()             