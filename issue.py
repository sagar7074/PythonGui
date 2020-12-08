from tkinter import *
from  tkcalendar import *
import time
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import random
import smtplib
from tkinter import ttk
from datetime import date

class Opration():
    def issue_window(self):
        issue=Toplevel()
        self.issue=issue
        self.issue.title("ISUUE BOOKS")
        self.issue.geometry("1535x790+0+0")
        self.issue.resizable(FALSE,FALSE)
        self.issue.config(bg='#DCDCDC')
      

    #=========================== fIRST frame for heading ===================================#

        self.frame1 = Frame(self.issue, bg='#8FBC8F',relief='flat')
        self.frame1.place(x=0, y=0, width=1535, height=70)

        self.label = Label(self.frame1, text='! ! DASHBOARD  ! !', font=('Impact', 30, 'bold'), fg='white',
                           bg='#8FBC8F', relief='flat')
        self.label.place(x=0, y=0, width=700,height=60)

    #============================= CLOCK LABEl ===============================#

        self.labeltime = Label(self.frame1,text='Time :', font=('Tahoma', 20, 'bold'), fg='white',bg='#8FBC8F', relief='flat')
        self.labeltime.place(x=1320, y=0, height=70)

        self.labelt = Label(self.frame1,font=('Tahoma', 20, 'bold'),fg='white',bg='#8FBC8F', relief='flat')
        self.labelt.place(x=1400, y=0, height=70)
        self.clock()

    #========================= SECOND FRAME FOR BACKWARD AND FORWARD BUTTON ===========================#

        self.frame2 = Frame(self.issue, bg='#D8F1F5',relief='flat')
        self.frame2.place(x=0, y=70, width=1527, height=40)

        self.log = PhotoImage(file='images/backward.svg.thumb.png')

        self.button = Button(self.frame2, fg='black',image=self.log,activeforeground='black',bd=0,relief='flat',bg='#D8F1F5',cursor='hand2',command=lambda:self.backward())
        self.button.place(x=10, y=0, width=40)

        
        self.log1 = PhotoImage(file='images/forward.svg.thumb.png')

        self.buttonn = Button(self.frame2, fg='black',image=self.log1 , activeforeground='black',bd=0,cursor='hand2',relief='flat', bg='#D8F1F5')
        self.buttonn.place(x=65, y=0, width=40)
        

 #============================== STUDENT  INFORMATIONS  FRAME  ==============================================#

        self.s_frame=Frame(self.issue,bg='#F5F5F5',relief=RIDGE,bd=2)
        self.s_frame.place(x=0,y=130,width=450,height=250)

        self.book_label = Label(self.s_frame, text='Student Info', font=('times new roman',20, 'bold'),
                            fg='black',bg='#5F9EA0',relief='flat')
        self.book_label.place(x=20, y=0,width=400)

        self.book_info_image=PhotoImage(file="images/studentinfo.png")
        self.book_label.config(image=self.book_info_image,compound=LEFT)
   
        self.id_label=Label(self.s_frame,text='Email-ID',font=('times new roman',17,'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.id_label.place(x=30,y=100)

        self.eentry=Entry(self.s_frame,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
        self.eentry.place(x=150,y=100,width=280)

#===================== BOOK INFORMATION FRAME =============================#

        self.book_frame=Frame(self.issue,bg='#F5F5F5',relief=RIDGE,bd=2)
        self.book_frame.place(x=450,y=130,width=1305,height=250)


        self.label1 = Label(self.book_frame, text='BOOOK-ID', font=('times new roman',17, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.label1.place(x=30, y=40)

        self.bentry1 = Entry(self.book_frame, font=('times new roman', 17, 'bold'),relief=GROOVE,bd=2)
        self.bentry1.place(x=170, y=40, width=220)

        self.orNAME = Label(self.book_frame, text='OR', font=('times new roman', 17, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.orNAME.place(x=150, y=100)

        self.labelNAME = Label(self.book_frame, text='BOOK-TITLE', font=('times new roman', 15, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.labelNAME.place(x=30, y=150)

        self.bNAME = Entry(self.book_frame, font=('times new roman', 17, 'bold'),relief=GROOVE,bd=2)
        self.bNAME.place(x=170, y=150, width=220)
        
    
        self.issuelabel = Label(self.book_frame, text='ISSUE-DATE', font=('times new roman', 17, 'bold'),fg='black', bg='#F5F5F5')
        self.issuelabel.place(x=450,y=40)

        self.dateentry1 = DateEntry(self.book_frame, date_pattern='yy-mm-dd',font=('times new roman',15, 'bold'),bg='#F5F5F5',fg='#F5F5F5')
        self.dateentry1.place(x=610, y=40,width=220)

    
        self.label_due_date = Label(self.book_frame, text='DUE-DATE ', font=('times new roman', 15, 'bold'),bg='#F5F5F5',fg='black')
        self.label_due_date.place(x=450, y=150)

        self.dateentry2 = DateEntry(self.book_frame, date_pattern='yy-mm-dd',font=('times new roman',15, 'bold'),bg='#F5F5F5',fg='#F5F5F5')
        self.dateentry2.place(x=610, y=150,width=220)
        
        self.bframe=Frame(self.book_frame,bg='red',relief=RIDGE,bd=2)
        self.bframe.place(x=860,y=20,width=200,height=200)

        self.button1 = Button(self.bframe,text='Search Book',cursor='hand2', command=lambda: self.student_framee_data_insert(),bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=0)
        self.button1.place(x=20, y=30,width=160)


        self.button_issue = Button(self.bframe,text='issue book', font=('times new roman',16, 'bold'),command=lambda:self.issue_books(),cursor='hand2',bd=2,relief=RIDGE)
        self.button_issue.place(x=20, y=120,width=160)


        #=============== CREATING FRAME FOR TREEVIEW ==========================#

        self.treeFrame=Frame(self.issue,bg='blue',relief='flat')
        self.treeFrame.place(x=10,y=390,width=1100,height=381)
    

        self.scroll_x = ttk.Scrollbar(self.treeFrame, orient=VERTICAL)
        self.scroll_y = ttk.Scrollbar(self.treeFrame, orient=HORIZONTAL)
        self.treview = ttk.Treeview(self.treeFrame, columns=(1, 2, 3, 4, 5,6,7 ),show='headings',height=17, xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=RIGHT, fill=Y)
        self.scroll_y.pack(side=BOTTOM,fill=X)
        self.style=ttk.Style()
        self.style.configure('Treeview',background='lightgray',foreground='black',rowheight=20)
        self.style.map('Treeview',background=[('selected','green')])

        self.scroll_x.config(command=self.treview.yview)
        self.treview.heading(1, text='BOOK_ID')
        self.treview.heading(2, text='BOOK_NAME')
        self.treview.heading(3, text='BOOK_AUTHOR')
        self.treview.heading(4, text='BOOK_EDITION')
        self.treview.heading(5, text="BOOK_PRICE")
        self.treview.heading(6,text='BOOK_quantity')
        self.treview.heading(7,text='PUBLISH_BY')


        self.treview.column(1, width=120, anchor=CENTER)
        self.treview.column(2, width=120, anchor=CENTER)
        self.treview.column(3, width=120, anchor=CENTER)
        self.treview.column(4, width=120, anchor=CENTER)
        self.treview.column(5, width=120, anchor=CENTER)
        self.treview.column(6,width=120,anchor=CENTER)
        self.treview.column(7,width=120,anchor=CENTER)

        self.treview.place(x=0, y=0, width=1084)
        self.treview.bind("<ButtonRelease-1>",self.click_insert)
        self.trre()

 #=================== BOOK INFO FRAME showing Book DATA ================================#

    def infoframe(self):
        self.iframe=Frame(self.issue,bg='lightblue',relief=GROOVE,bd=2)
        self.iframe.place(x=1130,y=390,width=380,height=381)


        self.info_id_label=Label(self.iframe,text='NAME :-',font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.info_id_label.place(x=30,y=30)

        
        self.info_name_label=Label(self.iframe,text='EMAIL-ID :-',font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.info_name_label.place(x=30,y=90)

        self.info_BID_label=Label(self.iframe,text='BOOK-ID :-',font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.info_BID_label.place(x=30,y=140)

        self.info_bname_label=Label(self.iframe,text='BOOK-NAME :-',font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.info_bname_label.place(x=30,y=200)

        self.info_bauthor_label=Label(self.iframe,text='BOOK-AUTHOR :-',font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.info_bauthor_label.place(x=30,y=260)


        self.info_bedition_label=Label(self.iframe,text='BOOK-EDITION :-',font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.info_bedition_label.place(x=30,y=320)

 #======================== CHECKING  THE STUDENT VALID OR NOT =============================#

    def student_framee_data_insert(self):
        if self.eentry.get()=='':
            messagebox.showwarning("Library Management",'Please Enter EMAIL Id')
        else:
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("SELECT * FROM student_table WHERE STUDENT_EMAIl=%s",self.eentry.get())
            self.row=cur.fetchone()
            if self.row==None:
                messagebox.showwarning('ERROR','Invalid User_ID ')

            else:
                self.enotification_label=Label(self.s_frame,text='* valid Student ID',font=('times new roman',12,'bold'),fg='green',bg='#F5F5F5',relief='flat')
                self.enotification_label.place(x=170,y=70)
                self.How_many_book_issue_by_student()

 #======================== CHECKING how many book issued by student ====================#

    def How_many_book_issue_by_student(self):
                con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
                cur = con.cursor()
                cur.execute("SELECT Student_email_ID  FROM borrow_table WHERE Student_email_ID=%s",self.eentry.get())
                self.row2 = cur.fetchall()
                self.n=len(self.row2)
                if self.n>=3 :
                    self.buttons.config(state='disabled')
                    messagebox.showinfo('sss',"student already issued maximum books")
                else:
                    self.search() 
                    self.infoframe()
                
 #============================== SEARCHING BOOK FROM DATABASE ==============================#
        
    def search(self):
        if self.bentry1.get()!='':
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("select * from books_data where Book_Id=%s",self.bentry1.get())
            self.data=cur.fetchall()
            if len(self.data) !=0:
                self.treview.delete(*self.treview.get_children())
                for j in self.data:
                    self.treview.insert('','end',values=j)
            else:
                self.notification_label=Label(self.book_frame,text='* Invalid BOOK ID',font=('times new roman',12,'bold'),fg='red',bg='#F5F5F5',relief='flat')
                self.notification_label.place(x=170,y=70)


        elif self.bNAME.get()!='':
            con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
            cur = con.cursor()
            cur.execute('SELECT * FROM books_data WHERE book_Name=%s',self.bNAME.get())
            self.data=cur.fetchall()
            if len(self.data) !=0:
                self.treview.delete(*self.treview.get_children())
                for j in self.data:
                    self.treview.insert('','end',values=j)
            
            else:
                self.qnotification_label=Label(self.book_frame,text='* Invalid BOOK NAME',font=('times new roman',12,'bold'),fg='red',bg='#F5F5F5',relief='flat')
                self.qnotification_label.place(x=170,y=180)
                    

   
 #============== TREEVIEW UPDATING FUNCTION =======================#

    def trre(self):
        con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
        cur = con.cursor()
        cur.execute("Select * from books_data ")
        self.bookrow = cur.fetchall()
        if len(self.bookrow) != 0:
            self.treview.delete(*self.treview.get_children())
            for i in self.bookrow:
                self.treview.insert('', 'end', values=i)
                con.commit()

            
#========== CHECKING THE STUDENT IS ALREADY ISSUED SAME book or not thIS IS MAIN FUNCTION FOR ISSUEING BOOK  =================#

    def issue_books(self):
        if self.eentry.get()=='':
             messagebox.showerror("Library Management System",'Please Enter Email ID To Issue Book ')
        elif self.bentry1.get()=='':
             messagebox.showerror("library Management System",'Please Enter Book ID And Name To Issue Book')
        else:
            con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
            cur = con.cursor()
            cur.execute("SELECT Book_id  FROM borrow_table WHERE Student_email_ID=%s and Book_id=%s",(self.eentry.get(),self.bentry1.get()))
            self.data_from_borrow=cur.fetchone()
            self.t=self.bentry1.get()
            print(self.t)
            self.s=self.data_from_borrow
            if self.s!=None:
                self.a=[]
                self.b=[]
                for self.element in self.s:
                    self.a.append(self.element)
                    for self.value in self.t:
                        self.b.append(self.value)
                        print(self.a)
                        print(self.b)
                        print(type(self.a))
                        print(type(self.b))
                        self.query()
                            
            else:
                con=pymysql.connect('localhost','root','Sagar123','libraray_management')
                cur=con.cursor()
                cur.execute("INSERT INTO borrow_table(Student_email_ID,Book_id, Book_name, Book_author, Book_edition, Book_price, Issue_date, Return_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %(self.eentry.get(),self.bentry1.get(),self.rowb[1],self.rowb[2],self.rowb[3],self.rowb[4],self.dateentry1.get(),self.dateentry2.get()))
                cur.execute("UPDATE books_data set quantity=quantity-1 WHERE BOOK_id=%s",self.bentry1.get())
                messagebox.showwarning("Library Management",'BOOK ISSUED SUCCESSFULLY')
                con.commit()
                self.bentry1.delete(0,END)
                self.bNAME.delete(0,END)
                self.trre()
        


 #============= THIS FUNCTION IS SAME AS UPPER FUNCTION ======================================#

    def query(self):
        for self.data in self.a:
                for self.value in self.b:
                    if self.data!=self.value:
                        con=pymysql.connect('localhost','root','Sagar123','libraray_management')
                        cur=con.cursor()
                        cur.execute("INSERT INTO borrow_table(Student_email_ID, Book_id, Book_name, Book_author, Book_edition, Book_price, Issue_date, Return_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %(self.eentry.get(),self.bentry1.get(),self.rowb[1],self.rowb[2],self.rowb[3],self.rowb[4],self.dateentry1.get(),self.dateentry2.get()))
                        cur.execute("UPDATE books_data set quantity=quantity-1 WHERE BOOK_id=%s",self.bentry1.get())
                        messagebox.showwarning("Library Management",'BOOK ISSUED SUCCESSFULLY')
                        con.commit()
                        self.sentry.config(state='normal')
                        self.bentry1.delete(0,END)
                        self.bNAME.delete(0,END)
                        self.OTPentry.delete(0,END)
                        self.trre()
                    else:
                        messagebox.showwarning("Library Management System",'Student Already Issued Same Book')


#================== MOUSE CLICK INSERT FUNCTION  ======================#

    def click_insert(self,ev):
        self.bentry1.delete(0,END)
        self.bNAME.delete(0,END)
        self.cur_rowb=self.treview.focus()
        self.contents=self.treview.item(self.cur_rowb)
        self.rowb=self.contents['values']
        print(self.rowb)
        self.bentry1.insert(0,self.rowb[0])
        self.bNAME.insert(0,self.rowb[1])
        
        self.output_info_BID_label=Label(self.iframe,text=self.eentry.get(),font=('times new roman',13,'bold'),fg='black',bg='lightblue',relief='flat')
        self.output_info_BID_label.place(x=180,y=90)

        self.output_info_BID_label=Label(self.iframe,text=self.rowb[0],font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.output_info_BID_label.place(x=210,y=140)

        self.output_info_bname_label=Label(self.iframe,text=self.rowb[1],font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.output_info_bname_label.place(x=210,y=200)

        self.output_info_bauthor_label=Label(self.iframe,text=self.rowb[2],font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.output_info_bauthor_label.place(x=210,y=260)

        self.output_info_bedition_label=Label(self.iframe,text=self.rowb[3],font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.output_info_bedition_label.place(x=210,y=320)

        self.output_info_name_label=Label(self.iframe,text=self.row[0] + self.row[1],font=('times new roman',15,'bold'),fg='black',bg='lightblue',relief='flat')
        self.output_info_name_label.place(x=210,y=30)

        #========================== CLOCK WORKING FUNCTION  ====================================#

    def clock(self):
        self.time1 = time.strftime("%H:%M:%S")
        self.labelt.config(text=self.time1)
        self.labelt.after(200,self.clock)
       
          #========================== backward button FUNCTION ======================================#

    def backward(self):
        self.issue.withdraw()


 #=============================================================== THE END ==========================================================================#
    
