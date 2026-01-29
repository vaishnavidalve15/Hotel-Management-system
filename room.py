from tkinter import*
from PIL import Image, ImageTk   # pip install pillow
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #======================Variable======================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


         # ============== Title ==========================
        lbl_title = Label(
            self.root,
            text="ROOM BOOKING DETAILS",
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
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman", 12, "bold"),padx=2,)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

         # ======================= lables and entries =======================
        #cust_contact
        lbl_cust_contact=Label(LabelFrameleft,text="Customer Contact :",font=("time new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=20,font=("arial",13))
        entry_contact.grid(row=0,column=1,sticky=W)
        #fetch data button
        btnFetchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="white",width=8)
        btnFetchData.place(x=347,y=4)

    

         #check_in_date
        check_in_date=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check_in Date :",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,width=29,font=("arial",13))
        txtcheck_in_date.grid(row=1,column=1)

         #check_out_date
        lbl_check_out=Label(LabelFrameleft,font=("arial",12,"bold"),text="Check_out Date :",padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_check_out=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,width=29,font=("arial",13))
        txt_check_out.grid(row=2,column=1)

         # room type
        label_roomtype=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room Type :",padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",13),width=27,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.grid(row=3,column=1)

        # available room
        lblRoomAvailable=Label(LabelFrameleft,font=("arial",12,"bold"),text="Available Room :",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_roomNo=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailable,font=("arial",13),width=27,state="readonly")
        combo_roomNo["value"]=rows
        combo_roomNo.grid(row=4,column=1)


        # meal
        lblMeal=Label(LabelFrameleft,font=("arial",12,"bold"),text="Meal :",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,width=29,font=("arial",13))
        txtMeal.grid(row=5,column=1)

        #no of days
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="No Of Days :",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays,width=29,font=("arial",13))
        txtNoOfDays.grid(row=6,column=1)

        #Pais Tax
        lblNoOfDays=Label(LabelFrameleft,font=("arial",12,"bold"),text="Paid Tax :",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txttxtNoOfDays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,width=29,font=("arial",13))
        txttxtNoOfDays.grid(row=7,column=1)

         #sub total
        lbl_subtotal=Label(LabelFrameleft,font=("arial",12,"bold"),text="Sub Total :",padx=2,pady=6)
        lbl_subtotal.grid(row=8,column=0,sticky=W)
        txt_subtotal=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,width=29,font=("arial",13))
        txt_subtotal.grid(row=8,column=1)

         #Total Cost
        lblTotal_cost=Label(LabelFrameleft,font=("arial",12,"bold"),text="Total Cost :",padx=2,pady=6)
        lblTotal_cost.grid(row=9,column=0,sticky=W)
        txtTotal_cost=ttk.Entry(LabelFrameleft,textvariable=self.var_total,width=29,font=("arial",13))
        txtTotal_cost.grid(row=9,column=1)

        #=====================bill button===================
        btnBill=Button(LabelFrameleft,text="Bill",command=self.calculate_bill,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #==============buttons=====================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="white",fg="black",width=10)
        btnreset.grid(row=0,column=3,padx=1)

        #===================== rigth side image ======================
        img3 = Image.open(r"C:\Users\vaish\OneDrive\Documents\Hotel Management System\Images\bed.jpg")
        img3 = img3.resize((520, 260), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=260)

          #=================== Table frame search system ======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search system",font=("times new roman", 12, "bold"),padx=2,)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By :",bg="blue",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",13),width=24,state="readonly")
        combo_Search["value"]=("Contact","Roomavailable")
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13))
        txtSearch.grid(row=0,column=2,padx=2)

        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial", 11, "bold"),bg="black",fg="white",width=10)
        btnSearch.grid(row=0,column=3,pady=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial", 11, "bold"),bg="black",fg="white",width=10)
        btnShowAll.grid(row=0,column=4,pady=1)

         #================= show data table ======================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_Table=ttk.Treeview(details_table,columns=("Contact","Checkin Date","Checkout Date","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_Table.xview)
        Scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("Contact",text="Contact")
        self.room_Table.heading("Checkin Date",text="Check-in Date")
        self.room_Table.heading("Checkout Date",text="Check-out Date")
        self.room_Table.heading("roomtype",text="Room Type")
        self.room_Table.heading("roomavailable",text="Room No")
        self.room_Table.heading("meal",text="Meal")
        self.room_Table.heading("noOfdays",text="NoOfDays")


        self.room_Table["show"]="headings"

        self.room_Table.column("Contact",width=100)
        self.room_Table.column("Checkin Date",width=100)
        self.room_Table.column("Checkout Date",width=100)
        self.room_Table.column("roomtype",width=100)
        self.room_Table.column("roomavailable",width=100)
        self.room_Table.column("meal",width=100)
        self.room_Table.column("noOfdays",width=100)
       

        self.room_Table.pack(fill=BOTH,expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #===========add data=====================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All filds are requaried",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                              self.var_contact.get(),
                                                                              self.var_checkin.get(),
                                                                              self.var_checkout.get(),
                                                                              self.var_roomtype.get(),
                                                                              self.var_roomavailable.get(),
                                                                              self.var_meal.get(),
                                                                              self.var_noofdays.get()              
                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
  
    
    #=============== fetch data =====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

     #================= update data ======================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(                                                                                                                                                       
                                                                                                                                        self.var_checkin.get(),
                                                                                                                                        self.var_checkout.get(),
                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                        self.var_roomavailable.get(),
                                                                                                                                        self.var_meal.get(),
                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                        self.var_contact.get()                                                                                                                                                                      
                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been update successfully",parent=self.root)
  
      #======================= Delete data =================================
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this room ",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #==================== Reset data =========================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
         
    #==================All data fetch===================

    def Fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please enter contact number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        query=("select Name from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
        else:
         conn.commit()
         conn.close()

        #name
         showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
         showDataframe.place(x=450,y=55,width=300,height=180)

         lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
         lblName.place(x=0,y=0)

         lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
         lbl.place(x=90,y=0)

        #grnder
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        query=("select Gender from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
        lblGender.place(x=0,y=30)

        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
        lbl2.place(x=90,y=30)

        #email
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        query=("select Email from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
        lblemail.place(x=0,y=60)

        lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
        lbl3.place(x=90,y=60)

        #nationality
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        query=("select Nationality from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        lblnationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
        lblnationality.place(x=0,y=90)

        lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
        lbl3.place(x=90,y=90)

        #address
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()
        query=("select Address from customer where Mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
        lbladdress.place(x=0,y=120)

        lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
        lbl4.place(x=90,y=120)

    #============== search data ======================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vaish@2003",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================calculations=========================
    def total(self):
        inDate = self.var_checkin.get()    
        outDate = self.var_checkout.get()   

        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")

        total_days = abs((outDate - inDate).days)
        self.var_noofdays.set(total_days)

    def calculate_bill(self):
        days = float(self.var_noofdays.get())
        roomavailable = self.var_roomavailable.get()
        meal_type = self.var_meal.get()

        room_cost = 0
        meal_cost = 0

    # Room price
        if roomavailable == "Single":
            room_cost = 500
        elif roomavailable == "Double":
            room_cost = 700
        elif roomavailable == "Luxury":
            room_cost = 1200
        elif roomavailable == "Deluxe":
            room_cost = 1400

    # Meal price
        if meal_type == "No Meal":
            meal_cost = 0
        elif meal_type == "Breakfast":
            meal_cost = 300
        elif meal_type == "Lunch":
            meal_cost = 500
        elif meal_type == "Dinner":
            meal_cost = 700

        subtotal = (room_cost + meal_cost) * days
        tax = subtotal * 0.10
        total = subtotal + tax

        self.var_paidtax.set(f"Rs. {tax:.2f}")
        self.var_actualtotal.set(f"Rs. {subtotal:.2f}")
        self.var_total.set(f"Rs. {total:.2f}")
  



if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()