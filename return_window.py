from tkinter import *
from tkinter import messagebox
import  pymysql
from PIL import ImageTk
from tkcalendar import *
from datetime import date


class Return():
    def first(self):
        return_window=Toplevel()
        self.return_window=return_window
        self.return_window.title("RETURN_WINDOW")
        self.return_window.geometry("1527x790+0+0")
        self.return_window.resizable(FALSE,FALSE)
        self.frame1 = Frame(self.return_window, bg='#8FBC8F', relief='flat')
        self.frame1.place(x=0, y=0, width=1527, height=80)

        self.label = Label(self.frame1, text='! ! DASHBOARD ! !', font=('Impact',30, 'bold'),
                           fg='white',
                           bg='#8FBC8F', relief='flat')
        self.label.place(x=0, y=0, width=800, height=70)
         #========================= SECOND FRAME BACKWARD AND FORWARD BUTTON ===========================#

        self.frame2 = Frame(self.return_window, bg='#D8F1F5',relief='flat')
        self.frame2.place(x=0, y=80, width=1527, height=199)

        self.log = PhotoImage(file='images/backward.svg.thumb.png')

        self.button = Button(self.frame2, fg='black',image=self.log,activeforeground='black',bd=0,relief='flat',bg='#D8F1F5',cursor='hand2',command=lambda:self.backward())
        self.button.place(x=10, y=0, width=40)

        
        self.log1 = PhotoImage(file='images/forward.svg.thumb.png')

        self.buttonn = Button(self.frame2, fg='black',image=self.log1 , activeforeground='black',bd=0, relief='flat', bg='#D8F1F5',cursor='hand2')
        self.buttonn.place(x=65, y=0, width=40)

    #=================== CREATING SEARCH STUDENT INFO ============================#
        
        self.search_lbel=Label(self.frame2,text='ENTER Email :',font=('times new roman', 17, 'bold'),fg='black', bg='#D8F1F5',relief='flat')
        self.search_lbel.place(x=400,y=30)

        self.student_info_entry = Entry(self.frame2, font=('times new roman', 17, 'bold'),relief=RAISED,bd=3)
        self.student_info_entry.place(x=680, y=30, width=250)
        self.Seach_student_image=PhotoImage(file='images/SEARCH STUDENT.png')
        self.searchs_button=Button(self.frame2,image=self.Seach_student_image,font=('times new roman',17,'bold'),command=lambda:self.search(),cursor='hand2',bd=0,bg='#D8F1F5')
        self.searchs_button.place(x=950,y=20)

        self.label1 = Label(self.frame2, text='BOOOK-ID       :', font=('times new roman',15, 'bold'),
                            fg='black',bg='#D8F1F5',relief=FLAT)
        self.label1.place(x=400, y=80)

        self.bentry1 = Entry(self.frame2, font=('times new roman', 15, 'bold'),relief=RAISED,bd=3)
        self.bentry1.place(x=680, y=80, width=250)

          
        self.return_date = Label(self.frame2, text='Return-Date', font=('times new roman', 15, 'bold'),fg='black',bg='#D8F1F5',relief='flat')
        self.return_date.place(x=400, y=130)

        self.dateentry2 = DateEntry(self.frame2, date_pattern='yy-mm-dd',font=('times new roman',15, 'bold'),bg='#D8F1F5',fg='#F5F5F5')
        self.dateentry2.place(x=680, y=130)

        self.return_book_image=PhotoImage(file='images/Return.png')
        self.return_button=Button(self.frame2,image=self.return_book_image,bd=0,bg='#D8F1F5',command=lambda:self.return_book(),cursor='hand2')
        self.return_button.place(x=950,y=100)
        
        self.extend_date_iamge=PhotoImage(file='images/extend.png')
        self.extend_button=Button(self.frame2,image=self.extend_date_iamge,font=('times new roman',17,'bold'),bd=0,bg='#D8F1F5',command=lambda:self.extend_date(),cursor='hand2')
        self.extend_button.place(x=1150,y=100)


    #====================== CREATING TREEVIEW ==================================#
        self.frame3 = Frame(self.return_window, relief='flat',bg='red')
        self.frame3.place(x=0, y=280, width=1527, height=620)

        self.scroll_x = ttk.Scrollbar(self.frame3, orient=VERTICAL)
        self.treview = ttk.Treeview(self.frame3, columns=(1, 2, 3, 4, 5,6,7,8 ),show='headings',height=30, yscrollcommand=self.scroll_x.set)
        self.scroll_x.pack(side=RIGHT, fill=Y)
        self.style=ttk.Style()
        self.style.configure('Treeview',background='lightgray',foreground='black',rowheight=20)
        self.style.map('Treeview',background=[('selected','green')])

        self.scroll_x.config(command=self.treview.yview)
        self.treview.heading(1, text='Student_EMAIL')
        self.treview.heading(2, text='BOOK_ID')
        self.treview.heading(3, text='BOOK_NAME')
        self.treview.heading(4, text="Book_AUTHOR")
        self.treview.heading(5,text='Book_edition')
        self.treview.heading(6,text='BOOK_price')
        self.treview.heading(7,text='ISsue_DATE')
        self.treview.heading(8,text='Return_Date')

        self.treview.column(1, width=100, anchor=CENTER)
        self.treview.column(2, width=100, anchor=CENTER)
        self.treview.column(3, width=100, anchor=CENTER)
        self.treview.column(4, width=100, anchor=CENTER)
        self.treview.column(5, width=100, anchor=CENTER)
        self.treview.column(6,width=100,anchor=CENTER)
        self.treview.column(7,width=100,anchor=CENTER)
        self.treview.column(8,width=100,anchor=CENTER)
        self.treview.place(x=0, y=0, width=1520)
        self.treview.bind("<ButtonRelease-1>",self.insertint_textbox)
        self.tree_update()
      
        
       

 #============== INSERTING VALUE IN TREEVIEW =========================#
 
    def tree_update(self):
        con=pymysql.connect('localhost','root','Sagar123','libraray_management')
        cur=con.cursor()
        cur.execute("SELECT Student_email_ID, Book_id, Book_name, Book_author, Book_edition, Book_price, Issue_date, Return_date FROM borrow_table")
        self.info = cur.fetchall()
        if len(self.info) != 0:
            self.treview.delete(*self.treview.get_children())
            for i in self.info:
                self.treview.insert('', 'end', values=i)
                con.commit()
            
  #===================== INSERTING INTO ENTRY FIELDS=========================#  
    def insertint_textbox(self,ev):
        self.student_info_entry.delete(0,END)
        self.bentry1.delete(0,END)
       
        self.cur_row=self.treview.focus()
        self.contents=self.treview.item(self.cur_row)
        self.info=self.contents['values']
        print(self.info)
      
        self.student_info_entry.insert(0,self.info[0])
        self.bentry1.insert(0,self.info[1])
        self.dateentry2.delete(0,END)
        self.dateentry2.insert(0,self.info[7])
        
        
    #========================== CREATING SERACH DATA FOR STUDENT INFO --CALLING AT FRAME_2 ==========================#

    def search(self):
        if self.student_info_entry.get()=='':
            messagebox.showwarning("Library Management System",'Please Enter Student Id To Search records')
        else:
            print(self.student_info_entry.get())
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("select * from borrow_table where Student_email_ID=%s",self.student_info_entry.get())
            self.data=cur.fetchall()
            if len(self.data) !=0:
                self.treview.delete(*self.treview.get_children())
                for j in self.data:
                    self.treview.insert('','end',values=j)

    #============================== CREATING RETURN BOOK FUNCTION =======================#


    def return_book(self):
        if self.bentry1.get()=='':
             messagebox.showwarning("Library Management System",'Please Select The Record Or Enter Book-ID To Return Book ')
        else:
            self.calculating_fine()
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("Delete  from borrow_table where Student_email_Id=%s and Book_id=%s",(self.student_info_entry.get(),self.bentry1.get()))
            
            cur.execute("UPDATE books_data set quantity=quantity+1 where Book_id=%s",self.bentry1.get())
            con.commit()
            con.close()
            messagebox.showinfo("Library Management System",'Book Return Successfully')
            self.tree_update()
            
    #========================= EXTEND DATE FUNCTION =========================#

    def extend_date(self):
        con=pymysql.connect('localhost','root','Sagar123','libraray_management')
        cur=con.cursor()
        cur.execute("select Student_email_ID from borrow_table Where Student_email_id=%s and Book_Id=%s",(self.student_info_entry.get(),self.bentry1.get()))
        id=cur.fetchone()
        print(id)
        cur.execute("Update borrow_table set Return_date=%s Where Student_email_ID=%s",(self.dateentry2.get(),id))
        con.commit()
        con.close()
        self.tree_update()
        messagebox.showinfo("Library Management System",'Date Extend Successfully')
        
    #================ BACKWARD FUNCTION ================================#    

    def backward(self):
        self.return_window.destroy()
    
    #======================== CALCULATING FINE =========================================#
    def calculating_fine(self):
        self.s=date.today()
        print(self.s)
        n=self.student_info_entry.get()
        con=pymysql.connect('localhost','root','Sagar123','libraray_management')
        cur=con.cursor()
        cur.execute("SELECT Issue_date,Return_date FROM borrow_table Where Student_email_ID='"+n+"'")
        t=cur.fetchone()
        if t!=None:
            print(t)
            print(t[1])
            self.b=t[1]
            delta1=self.s
            delta2=self.b
            delta=delta1-delta2
            chm=delta.days
            print(chm)

            if chm<=0:
                messagebox.showinfo("Library Management System",'No fine Is genreted')

            elif chm>0:
                self.charge=5*chm
                print(self.charge)
                messagebox.showinfo("Library Management System",'Your Fine Is  '+ str(self.charge)+"  Ruppes")
        
        else:
            messagebox.showinfo("Library Management system",'Please select The Record To Proceed ')
 
 #================================================================ THE END ===========================================================#

            
        