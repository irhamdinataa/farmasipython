from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Kelas (Class)
class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")


        self.conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
        self.my_cursor = self.conn.cursor()
        # ==================addMed variable=================
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()

        #==main variable===
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
               bg="white",fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        # Image
        img1 = Image.open("C:/Users/irham/OneDrive/Documents/Farmasi/Logo.png")
        img1 = img1.resize((80, 80), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, bg='white')
        b1.pack(side=LEFT, padx=10)
       
        # ==================DataFrame=================
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1360, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information",
                                   fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=1100, height=350)

    
        # ===================buttonsFrame====================

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=70)
        ButtonFrame.place(x=-70, y=520, width=3000, height=65)

        # ====================Main Button=====================

        btnAddData = Button(ButtonFrame, text="Medicine Add", font=("arial", 11, "bold"), bg="darkgreen", fg="white",command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnUpdateMed = Button(ButtonFrame, text="UPDATE", font=("arial", 11, "bold"), width=14, bg="darkgreen", fg="white",command=self.update_data)
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonFrame, text="DELETE", font=("arial", 11, "bold"), width=14, bg="red", fg="white",command=self.delete)
        btnDeleteMed.grid(row=0, column=2)

        btnRestMed = Button(ButtonFrame, text="RESET", font=("arial", 11, "bold"), width=14, bg="darkgreen", fg="white",command=self.reset)
        btnRestMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial", 11, "bold"), width=14, bg="darkgreen", fg="white",command=self.exit_app)
        btnExitMed.grid(row=0, column=4)

        # ========Search By========
        lblSearch = Label(ButtonFrame, font=("arial", 16, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        #variable
        self.search_var = StringVar()
        serch_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
        serch_combo["values"]=("refno","medname","lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)

        self.searchTxt_var = StringVar()

        txtSerch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSerch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,text="SEARCH",font=("arial",11,"bold"),width=11,bg="darkgreen",fg="white",command=self.search_data,)
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,text="SHOW ALL",font=("arial",11,"bold"),width=11,bg="darkgreen",fg="white",command=self.fetch_data)
        showAll.grid(row=0,column=9)

        # ====================label and entry====================
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)
        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",font=("arial",12,"bold"),width=27)

        comTypeofMedicine['value']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)

        # ==========AddMedicine==========
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly",font=("arial",12,"bold"),width=27)
        comMedicineName['value']=med
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses",padx=2,pady=4)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage",padx=15,pady=6)
        lblDosage.place(x=410,y=1)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.place(x=540,y=5)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price (Rp)",padx=15,pady=6)
        lblPrice.place(x=410,y=40)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.place(x=540,y=45)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QTS",padx=15,pady=6)
        lblProductQt.place(x=410,y=80)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.place(x=540,y=85)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning",padx=15,pady=6)
        lblPrecWarning.place(x=410,y=120)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrecWarning.place(x=540,y=125)

        # ================Image===================
        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text="Stay Home Stay Safe:",padx=15,pady=6,bg="white",fg="red",width=37)
        lblhome.place(x=410,y=180)

        img2=Image.open("C:/Users/irham/OneDrive/Documents/Farmasi/far.jpeg")
        img2=img2.resize((405,100), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=475,y=370)

        # ==================dataframeRight===================
        DataFramerRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                    fg="darkgreen",font=("arial",12,"bold"))
        DataFramerRight.place(x=910,y=5,width=400,height=350)

        img5=Image.open("C:/Users/irham/OneDrive/Documents/Farmasi/lab.jpeg")
        img5=img5.resize((370,75), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)


        lblrefno=Label(DataFramerRight,font=("arial",12,"bold"),text="Reference No:")
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFramerRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=80)

        lblmedName=Label(DataFramerRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFramerRight,textvariable=self.addmed_var,font=("arial",15,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=110)

        # ======================side frame=======================
        side_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)


        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)


        # =================Medicine Add Buttons=================
        down_frame=Frame(DataFramerRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=290,y=150,width=70,height=130)

        btnAddmed=Button(down_frame,text="ADD",font=("arial",9,"bold"),width=9,bg="lime",fg="white",pady=4, command=self.AddMed)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE",font=("arial",9,"bold"),width=9,bg="purple",fg="white",pady=4, command=self.UpdateMed)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="DELETE",font=("arial",9,"bold"),width=9,bg="red",fg="white",pady=4, command=self.DeleteMed)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,text="CLEAR",font=("arial",9,"bold"),width=9,bg="orange",fg="white",pady=4, command=self.ClearMed)
        btnClearmed.grid(row=3,column=0)


        # ===================Frame Details===================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)

        # ===================Main Table & scrollbar===================
        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=570,width=1360,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","medicinename","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("medicinename",text="Medicine Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price (Rp)")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("medicinename",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


#===add medicine functionality declaration===

    def AddMed(self):
        refMed = self.refMed_var.get()
        addmed = self.addmed_var.get()
        
        if refMed == '' or addmed == '':
            messagebox.showerror("Error", "Harus diisi semuanya")
            return
        
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO pharma(Ref, MedName) VALUES (%s, %s)", (refMed, addmed))  
            conn.commit()
            messagebox.showinfo("Success", "Medicine Added")
            self.fetch_dataMed()  # Assuming this function fetches updated data
            self.Medget_cursor()  # Assuming this function refreshes UI or cursor
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#===medgetcursor===

    def Medget_cursor(self,event=""):
        cursor_row = self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])

    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                self.addmed_var.get(),
                self.refMed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("success","data has been updated")

    def DeleteMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")

#====Main tabble =======
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get() == "":
            messagebox.showerror("error","all field are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharmacy values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.ref_var.get(),
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideEffect_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.product_var.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","data has ben inserted")


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,value=i)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideEffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.product_var.set(row[12])
        
    def update_data(self):
        if self.ref_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s,Type=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosge=%s,price=%s,product=%s where refno=%s ",(
                                                                                self.cmpName_var.get(),
                                                                                self.typeMed_var.get(),
                                                                                self.medName_var.get(),
                                                                                self.lot_var.get(),
                                                                                self.issuedate_var.get(),
                                                                                self.expdate_var.get(),
                                                                                self.uses_var.get(),
                                                                                self.sideEffect_var.get(),
                                                                                self.warning_var.get(),
                                                                                self.dosage_var.get(),
                                                                                self.price_var.get(),
                                                                                self.product_var.get(),
                                                                                self.ref_var.get(),
                
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","data has been updated")

    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        sql="delete from pharmacy where refno=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Delete","deleted successfully")

    def reset(self):
        #self.ref_var.set(""),
        self.cmpName_var.set(""),
        #self.typeMed_var.set(""),
        #self.medName_var.set,("")
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.product_var.set("")

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.searchTxt_var.get()) + "%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
