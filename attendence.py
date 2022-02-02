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


class attendence():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")


    # ============= variables ===================

        self.var_atten_id=StringVar()   
        self.var_atten_roll=StringVar()  
        self.var_atten_name=StringVar()  
        self.var_atten_dep=StringVar()  
        self.var_atten_time=StringVar()  
        self.var_atten_date=StringVar()  
        self.var_atten_attendance=StringVar()   



     # first image 


      


        img1=Image.open(r"C:\Users\HP\Desktop\final year project\images\students_1.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200) 

        
        
        
        
        
        # second image
        
        img2=Image.open(r"C:\Users\HP\Desktop\final year project\images\students_3.jpeg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200 )  


        #  bg image


        img4=Image.open(r"C:\Users\HP\Desktop\final year project\images\attendence.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530,height=710) 


        # title

        title_lbl=Label(bg_img,text="ATTENDENCE MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=45)


        # main frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

         # left label

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENTS ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        # image

        img_left=Image.open(r"C:\Users\HP\Desktop\final year project\images\student information.png")
        img_left=img_left.resize((755,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=755,height=130) 

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=745,height=400)

        # ======== labeled entry ==========================

        # attendence ID

        attendence_id_label=Label(left_inside_frame,text="Attendence ID:",font=("times new roman",12,"bold"),bg="white")
        attendence_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendence_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendence_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        # name
        name_id_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_id_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        name_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_id_entry.grid(row=0,column=3,padx=8,sticky=W)

    # roll_no
        roll_id_label=Label(left_inside_frame,text="Roll_No:",font=("times new roman",12,"bold"),bg="white")
        roll_id_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_id_entry.grid(row=1,column=1,padx=10,sticky=W)


        # department
        department_id_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_id_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        attendence_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        attendence_id_entry.grid(row=1,column=3,padx=10,sticky=W)

        
        # time
        time_id_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_id_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        attendence_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        attendence_id_entry.grid(row=2,column=1,padx=10,sticky=W)

         # date
        date_id_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_id_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_id_entry.grid(row=2,column=3,padx=10,sticky=W)



        # attendence
        attendence_label=Label(left_inside_frame,text="Attendence status",font=("times new roman",12,"bold"),bg="white")
        attendence_label.grid(row=3,column=0,padx=10,sticky=W)

        semester_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),textvariable=self.var_atten_attendance,width=20,state="read only")
        semester_combo["values"]=("Status","Present","Absent")
        semester_combo.current(0)
        semester_combo.grid(row=3,column=1,padx=8,pady=10,sticky=W)


        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=745,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv, width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv, width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update" ,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=20,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





         # right label

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=700,height=580)


        right_inside_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        right_inside_frame.place(x=5,y=5,width=690,height=460)

        #===================== Scroll bar ===============

        scroll_x=ttk.Scrollbar(right_inside_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_inside_frame,orient=VERTICAL)

        self.attendence_report=ttk.Treeview(right_inside_frame,column=("ID","roll_no","Name","Department","Time","Date","Attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendence_report.xview)
        scroll_y.config(command=self.attendence_report.yview)

        self.attendence_report.heading("ID",text="ATTENDENCE_ID")
        self.attendence_report.heading("roll_no",text="ROLL_NO")
        self.attendence_report.heading("Name",text="Name")
        self.attendence_report.heading("Department",text="Department")
        self.attendence_report.heading("Time",text="Time")
        self.attendence_report.heading("Date",text="Date")
        self.attendence_report.heading("Attendence",text="ATTENDENCE STATUS")
        # self.attendence_report.heading("",text="ATTENDENCE_ID")

        self.attendence_report["show"]="headings"

        self.attendence_report.column("ID",width=100)
        self.attendence_report.column("roll_no",width=100)
        self.attendence_report.column("Name",width=100)
        self.attendence_report.column("Department",width=100)
        self.attendence_report.column("Time",width=100)
        self.attendence_report.column("Date",width=100)
        self.attendence_report.column("Attendence",width=130)
        self.attendence_report.pack(fill=BOTH,expand=1 )

        self.attendence_report.bind("<ButtonRelease>",self.get_cursor)




    # =============== fetch data ==============================


    def fetchdata(self,rows):
        self.attendence_report.delete(* self.attendence_report.get_children())
        for i in rows:
            self.attendence_report.insert("",END,values=i)

    # =========== import csv ==================

    def importcsv(self):
        global mydata  
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="open csv" ,filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root) 
        
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")

            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)  

    # export csv

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO DATA","NO DATA FOUND TO EPORT",parent=self.root)
                return False        

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="open csv" ,filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root) 

            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)

                messagebox.showinfo(" Data Export"," Your data exported to "+os.path.basename(fln)+"successfully")    


        except Exception as es:
            messagebox.showerror("ERROR",f"due to:{str(es)}",parent=self.root)



    # ========= GET CURSOR ==============================

    def get_cursor(self,event=""):
        Cursor_row=self.attendence_report.focus()
        content=self.attendence_report.item(Cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])       


    # ================= RESET ==============================

    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("")                   
        self.var_atten_name.set("")                   
        self.var_atten_dep.set("")
        self.var_atten_time.set("")                   
        self.var_atten_date.set("")                   
        self.var_atten_attendance.set("Status")                   
        




if __name__=="__main__":
    root=Tk()
    obj=attendence(root)
    root.mainloop()                     