from tkinter import*
from PIL import Image, ImageTk   # pip install pillow
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        
         # ============== Title ==========================
        lbl_title = Label(
            self.root,
            text="Room Adding Department",
            font=("times new roman", 18, "bold"),
            bg="black",
            fg="white",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

         # ================ Logo =======================
        img2 = Image.open(r"C:\Users\vaish\OneDrive\Documents\Hotel Management System\Images\hotel logo.jpg")
        img2 = img2.resize((100, 45), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

         # ================ label frame ==================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Rooms Add",font=("times new roman", 12, "bold"),padx=2,)
        LabelFrameleft.place(x=5,y=50,width=540,height=350)

         # ======================= lables and entries =======================
        #Floor
        lbl_floor=Label(LabelFrameleft,text="Floor :",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(LabelFrameleft,textvariable=self.var_floor,width=20,font=("arial",13))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #Room no
        lbl_RoomNo=Label(LabelFrameleft,text="Room No :",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)
        
        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(LabelFrameleft,textvariable=self.var_roomNo,width=20,font=("arial",13))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room type
        lbl_RoomType=Label(LabelFrameleft,text="Room Type :",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)
        
        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomType,width=20,font=("arial",13))
        entry_RoomType.grid(row=2,column=1,sticky=W)

           #==============buttons=====================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnreset.grid(row=0,column=3,padx=1)

             #=================== Table frame search system ======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman", 12, "bold"),padx=2,)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_Table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomtype"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_Table.xview)
        Scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("floor",text="Floor")
        self.room_Table.heading("roomno",text="Room No")
        self.room_Table.heading("roomtype",text="Room Type")

        self.room_Table["show"]="headings"

        self.room_Table.column("floor",width=100)
        self.room_Table.column("roomno",width=100)
        self.room_Table.column("roomtype",width=100)
       

        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

     #===========add data=====================
    def add_data(self):
            if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                messagebox.showerror("Error","All filds are requaried",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_roomNo.get(),
                                                                                self.var_RoomType.get()                      
                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("success","New room added successfully ",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
    
    #=============== fetch data =====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.room_Table.focus()
        content=self.room_Table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])

     #================= update data ======================
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomNo=%s,RoomType=%s",(                                                                                                                                                       
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomNo.get(),
                                                                                    self.var_RoomType.get(),
                                                                                                                                                                                                                                                         
                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been update successfully",parent=self.root)

    #======================= Delete data =================================
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this room ",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #==================== Reset data =========================
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")

    
      
  
       

if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()