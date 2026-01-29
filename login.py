from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk   # pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from Hotel import HotelManagementSystem

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\vaish\OneDrive\Documents\Hotel Management System\Images\wp9764012.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img=Image.open(r"C:\Users\vaish\OneDrive\Documents\Hotel Management System\Images\logo1.webp")
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        lblimg=Label(image=self.photoimage,bg="black",borderwidth=0)
        lblimg.place(x=730,y=175,width=100,height=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=90)

        # lable
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=140)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=170,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=210)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=240,width=270)

        #============== icon image =============================
        img2=Image.open(r"C:\Users\vaish\OneDrive\Documents\Hotel Management System\Images\username1.jpg")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=310,width=25,height=25)

        img3=Image.open(r"C:\Users\vaish\OneDrive\Documents\Hotel Management System\Images\password.webp")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=380,width=25,height=25)

        # login btn
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="red",activeforeground="black",activebackground="red")
        loginbtn.place(x=110,y=290,width=120,height=35)
 

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All filds required")
        elif self.txtuser.get()=="vaishnavidalve15" and self.txtpass.get()=="Vaish@123":
            messagebox.showinfo("success","Welcome to Hotel Management System project")
            self.root.destroy()

            self.root = Tk()
            HotelManagementSystem(self.root)
            self.root.mainloop()
        else:
            messagebox.showerror("Invalid","Invalid username & password")
  



if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
        