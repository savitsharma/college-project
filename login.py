from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

#pip install pillow

class Login_Window:
    def __init__(self,root): 
        self.root=root
        self.root.title("Login") 
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\logim) 
        1b1_bg=Label(self.root, image=self.bg) 
        1b1_bg.place(x=0, y=0, relwidth=1,relheight=1)

        frame=Frame(self.root, bg="black") 
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Admin\Desktop\login_form\images") 
        img1=img1.resize((100,100), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage (img1)
        lblimg1=Label(image=self.photoimage1,bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175,width=100,height=1000)
        
        get_str=Label(frame, text="Get Started", font-("times new roman", 20, "bold"),fg="white",bg="black") 
        get_str.place(x=95, y=100)

        # label

        username=1b1=Label(frame, text="Username", font=("times new roman",15, "bold"), fg="white",bg="black") 
        username.place(x=70, y=155)
        
        self.txtuser=ttk.Entry(frame, font-("times new roman",15, "bold")) 
        self.txtuser.place(x-40, y=180,width=270)

        password=1b1=Label (frame, text="Password", font=("times new roman",15, "bold"), fg="white",bg="black") 
        password.place(x=70, y=225)

        self.txtpass-ttk. Entry(frame, font-("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250,width=270)
  
        #=======icon image========
        img2=Image.open("C:\Users\Admin\Desktop\login_form\images\LoginIconAppl.png") 
        img2=img2.resize((25,25), Image.ANTIALIAS) 
        self.photoimage1=ImageTk.PhotoImage(img2)
        lblimgi=Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblings.place(x=650, y 323,width=25, height=25)

        img3-Image.open("C:\Users\Admin\Desktop\login_form\images\lock-512.png") 
        img3=img3.resize((25,25), Zmage.ANTIALIAS) 
        self.photoimage3=ImageTk.PhotoImage(img3) 
        lblimg1=Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=395,width=25,height=25)
        
        #login button 
        loginbtn=Button(frame,text="Login",font-("times new roman",15,"bold"), bd=3, relief-RIDGE, fg="white",bg="red", active foreground="white", activebackground="red")
        loginbtn.place(x=110,y=300,width=120, height=35)

        #register button 
        registerbtn=Button(frame,text="Login",font=("times new roman",15,"bold"), bd=3, relief-RIDGE, fg="white",bg="red", active foreground="white", activebackground="red")
        registerbtn.place(x=110,y=300,width=120, height=35)

        #forrget password 
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"), bd=3, relief-RIDGE, fg="white",bg="red", active foreground="white", activebackground="red")
        loginbtn.place(x=110,y=300,width=120, height=35)
       
       
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="": 
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success", "Welcome to codewithkiran channel plaze subscribe my channel")
            else:
                messagebox.showerror("Invalid", "Invalid username&password")