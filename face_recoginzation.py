from tkinter import *
from tkinter import ttk
from turtle import up, width
from PIL import ImageTk, Image
from time import strftime  
from datetime import datetime  
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np



class Face_recogination:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530, height=45)
        

        # first image

        img_top=Image.open(r"C:\Users\HP\Desktop\final year project\images\face2.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        

        # second image

        img_bottom=Image.open(r"images\face.png")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb2=Label(self.root,image=self.photoimg_bottom)
        f_lb2.place(x=650,y=55,width=950,height=700)

        # button

        save_btn=Button(self.root,text="TRAIN DATA",command=self.face_recog,width=30,font=("times new roman",19,"bold"),bg="darkgreen",fg="white")
        save_btn.place(x=0,y=600,width=1530,height=50)
    
    
    #=========== attendence =========================================

    def mark_attendance(self,i,r,n,d):
        with open("excel.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and    (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")   # year
                dtString=now.strftime("%H:%M:%S")  # time
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")


             







    # ============== face recogination ================================


    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))          # formula



                conn=mysql.connector.connect(host="localhost",user="root",password="Pranjal@123", database="face_recognization",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from students where student_id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)

                my_cursor.execute("select  Roll_no from students where student_id="+str(id))
                r=my_cursor.fetchone()
                r=str(r)


                
                my_cursor.execute("select  department from students where student_id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)


                my_cursor.execute("select student_id from students where student_id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)

                

                if confidence>77:   # for known face

                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)


                else:              # for unknown face
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unkown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord=[x,y,w,h]     ##################################

            return coord    

        def recognize(img,clf,facecascade):
            coord=draw_boundray(img,facecascade,1.1,10,(255,25,255),"Face",clf)
            return img


        facecascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow("Welcome to face recognization",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()    



           
if __name__=="__main__":
    root=Tk()
    obj=Face_recogination(root)
    root.mainloop()                             