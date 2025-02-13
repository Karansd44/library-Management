from tkinter import *
from tkinter import ttk 

class librarymanagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("library management system")
        self.root.geometry("1550x800+0+0")
        
        
        
        
        
        #====================================Variable =================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()
        
        lbltitle=Label(self.root, text ="LIBRARY MANAGEMENT SYSTEM",bg = "powder blue",fg="green",bd=20,relief = RIDGE,font = ("time new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        
        
        frame = Frame(self.root ,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        
       # ====================================DataFrameLeft================================
        
        DataFrameLeft=LabelFrame(frame, text ="Libarary Membership imformation",bg="powder blue",fg="black",bd=20,relief = RIDGE,font = ("time new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width = 860,height=360)
        
        lblMemebr =Label(DataFrameLeft,bg = "powder blue",textvariable=self.member_var, text="Member Type" ,font=("arial",12,"bold"),padx=2,pady=6)
        lblMemebr.grid(row=0,column=0,sticky=W)
        
        
        comMemeber =ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=27,state="readyonly")
        comMemeber['value'] =("Admin staff","lecturer","Student")
        comMemeber.current(0)
        comMemeber.grid(row=0,column=1)
        
        
        lblPRN_NO =Label(DataFrameLeft,bg = "powder blue", text="PRN NO" ,font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle =Label(DataFrameLeft,bg = "powder blue", text="ID No" ,font=("arial",12,"bold"),padx=2 ,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg = "powder blue", text="FirstName" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg = "powder blue", text="LastName" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg = "powder blue", text="Address1" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,bg = "powder blue", text="Address2" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,bg = "powder blue", text="Post Code" ,font=("arial",12,"bold"),padx=2 ,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,bg = "powder blue", text="Mobile" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,bg = "powder blue", text="Book ID" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtBookID.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,bg = "powder blue", text="Book Title" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,bg = "powder blue", text="Author" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg = "powder blue", text="Date Borrowed" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)
        
        lblDateDue=Label(DataFrameLeft,bg = "powder blue", text="Date Due" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)
        
        lblDaysOnBook=Label(DataFrameLeft,bg = "powder blue", text="Days On Book" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,bg = "powder blue", text="Late Return Fine" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDateOverDue=Label(DataFrameLeft,bg = "powder blue", text="Date Over Due" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateOverDue.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg = "powder blue", text="Actual Price" ,font=("arial",12,"bold"),padx=2 ,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)
        
        #================================================DataFrameRight================================================
        
        DataFrameRight=LabelFrame(frame, text ="Book Details",bg = "powder blue",fg="black",bd=20,relief = RIDGE,font = ("arial",12,"bold"))
        DataFrameRight.place(x=870,y=5,width = 590  ,height=360)
        
        self.txtBox=Text(DataFrameRight,font = ("arial",12,"bold"),width=39,height =16,padx=2,pady=6)
        self.txtBox.grid(row =0,column=2)
        
    
        
        listBooks=["Crash Course Python", "Head First Programming", "Eloquent JavaScript", "The Pragmatic Programmer", "The Lord of Rings",  "The Guide to Galaxy", "Dune", "Frankenstein",
                   "A Brief History of Time", "The Martian", "The Handmaid's Tale", "Algorithms to Live By", "Artificial Intelligence", "Computer Networking", "Operating Systems", "Deep Learning"]
        
        listBox=Listbox(DataFrameRight,font = ("arial",12,"bold"),width=20,height =16)
        listBox.grid(row=0,column=0,padx=4)
    
        
        
        for item in listBooks:
            listBox.insert(END,item)
        
        #===========================================Button frame================================
        
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData=Button(Framebutton, text="Add Data", font=("arial",12, "bold"), width=23,bg="#3F00FF" , fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton, text="Show Data",font=("arial",12,"bold"),width=23,bg="#3F00FF",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="#3F00FF",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="#3F00FF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="#3F00FF",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="#3F00FF",fg="white")
        btnAddData.grid(row=0,column=5)
        
         #===========================================Information frame================================
        
        FrameDetails = Frame(self.root ,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)
        
        
        Table_frame=Frame(FrameDetails,bd=6, relief=RIDGE ,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1485,height=190)
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,columns=("Member Type","prnno","title", "firstname", "lastname", "address1","address2","postid", "mobile", 
                                                             "bookid","booktitle","auther", "dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.configure(command=self.library_table.xview)
        yscroll.configure(command=self.library_table.yview)
        
        
        self.library_table.heading("Member Type",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)
        
        self.library_table.column("Member Type",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table. column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)



if __name__ == "__main__":
    root = Tk()
    obj= librarymanagementSystem(root)
    root.mainloop()