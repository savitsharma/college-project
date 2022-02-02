from tkinter import *
from tkinter import ttk
from turtle import up, width
from PIL import ImageTk, Image
  
  
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np



class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        img_top=Image.open(r"images\download.jfif")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325) 

        #  train data button

        save_btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,width=20,font=("times new roman",30,"bold"),bg="red",fg="white")
        save_btn.place(x=0,y=380,width=1530,height=90)


        img_bottom=Image.open(r"images\download (1).jfif")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=360) 

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]   # list comprehensing

        faces=[] 
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')               # gray scale image  
            imageNP=np.array(img,'uint8')                    # data type
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        
        
        #========= train the classifier and save ====================


        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!!")




        


        


           
if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()                             