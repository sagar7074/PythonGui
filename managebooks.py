from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql




class Manage:
    def M_window(self):
        manage=Toplevel()
        self.manage=manage
        self.manage.title("Manage Books")
        self.manage.geometry("1535x790+0+0")
        self.manage.resizable(FALSE,FALSE)
    
  #========= CREATING FRAME FOR HEADING ========================#

        self.frame1 = Frame(self.manage, bg='#8FBC8F',relief='flat')
        self.frame1.place(x=0, y=0, width=1535, height=70)

        self.label = Label(self.frame1, text='! ! MANAGE BOOKS  ! !', font=('Impact', 30, 'bold'), fg='white',
             bg='#8FBC8F', relief='flat')
        self.label.place(x=0, y=0, width=700,height=60)

  #============== CREATING FRMAE FOR BACKWARD AND FORWARD BUTTON ==================#
        self.frame2= Frame(self.manage, bg='#D8F1F5',relief='flat')
        self.frame2.place(x=0, y=70, width=1527, height=40)

        self.log = PhotoImage(file='images/backward.svg.thumb.png')

        self.button = Button(self.frame2, fg='black',image=self.log,activeforeground='black',bd=0,relief='flat',bg='#D8F1F5',cursor='hand2',command=lambda:self.backward())
        self.button.place(x=10, y=0, width=40)

        
        self.log1 = PhotoImage(file='images/forward.svg.thumb.png')

        self.buttonn = Button(self.frame2, fg='black',image=self.log1 , activeforeground='black',bd=0,cursor='hand2',relief='flat', bg='#D8F1F5')
        self.buttonn.place(x=65, y=0, width=40)

    #=================== CREATING FRAME  FOR LABELS AND BUTTONS ============================#
        self.frame3= Frame(self.manage, bg='#F5F5F5',relief=RIDGE,bd=2)
        self.frame3.place(x=10, y=120,width=1505, height=260)


        self.book_id = Label(self.frame3, text="BOOK-ID", font=('times new roman', 17, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.book_id.place(x=10,y=40)

        self.book_id_entry = Entry(self.frame3, font=('times new roman', 15, 'bold'),relief=GROOVE ,bd=2)
        self.book_id_entry.place(x=150,y=40,width=220)

        self.book_name = Label(self.frame3, text="BOOK-Title", font=('times new roman', 15, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.book_name.place(x=410,y=40)

        self.book_name_entry = Entry(self.frame3, font=('times new roman', 15, 'bold'),relief=GROOVE ,bd=2)
        self.book_name_entry.place(x=530,y=40,width=220)

        self.book_author = Label(self.frame3, text="BOOK-Author", font=('times new roman', 15, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.book_author.place(x=780,y=40)

        self.book_author_entry = Entry(self.frame3, font=('times new roman', 15, 'bold'),relief=GROOVE ,bd=2)
        self.book_author_entry.place(x=980,y=40,width=220)

        self.book_edition = Label(self.frame3, text="BOOK-Edition", font=('times new roman', 13, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.book_edition.place(x=10,y=100)

        self.book_edition_entry = Entry(self.frame3, font=('times new roman', 15, 'bold'),relief=GROOVE ,bd=2)
        self.book_edition_entry.place(x=150,y=100,width=220)

        self.book_quantity = Label(self.frame3, text="BOOK-Quantity", font=('times new roman', 13, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.book_quantity.place(x=410, y=100)

        self.book_quantity_entry = Entry(self.frame3, font=('times new roman', 15, 'bold'),relief=GROOVE ,bd=2)
        self.book_quantity_entry.place(x=540, y=100, width=220)


        self.publish_by = Label(self.frame3, text="PUBLISH_BY", font=('times new roman', 17, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.publish_by.place(x=780, y=100)

        self.publish_by_entry = Entry(self.frame3, font=('times new roman', 15, 'bold'),relief=GROOVE ,bd=2)
        self.publish_by_entry.place(x=980, y=100 , width=220)

        self.book_price = Label(self.frame3, text="BOOK-PRICE", font=('times new roman', 15, 'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.book_price.place(x=10, y=160)

        self.book_price_entry = Entry(self.frame3, font=('times new roman', 17, 'bold'),relief=GROOVE ,bd=2)
        self.book_price_entry.place(x=150, y=160, width=220)


        self.addbook_image = PhotoImage(file='images/ADDBOOKBUTTON.png')
        self.Addbookbutton =Button(self.frame3,image=self.addbook_image,bg='#F5F5F5',bd=0, command=lambda: self.add_book(),cursor='hand2')
        self.Addbookbutton.place(x=1250, y=20)

        self.updatebook_image=PhotoImage(file='images/update_book.png')
        self.update_bookbutton =Button(self.frame3,image=self.updatebook_image,bg='#F5F5F5',bd=0, command=lambda: self.update(),cursor='hand2')
        self.update_bookbutton.place(x=1250, y=80)


        self.search_book_image=PhotoImage(file='images/search.png')
        self.search_bookbutton =Button(self.frame3,image=self.search_book_image,bg='#F5F5F5',bd=0, command=lambda: self.search(),cursor='hand2')
        self.search_bookbutton.place(x=1250, y=140)

        self.delete_book_image=PhotoImage(file='images/deletebook.png')
        self.delete_bookbutton =Button(self.frame3,image=self.delete_book_image,bg='#F5F5F5',bd=0, command=lambda: self.delete(),cursor='hand2')
        self.delete_bookbutton.place(x=1250, y=200)

 #============== CREATING FRAME FOR TREEVIEW =================================#
        self.frame4 = Frame(self.manage, relief='flat',bg='red')
        self.frame4.place(x=10, y=380, width=1510, height=400)

        self.scroll_x = ttk.Scrollbar(self.frame4, orient=VERTICAL)
        self.scroll_y=ttk.Scrollbar(self.frame4,orient=HORIZONTAL)
        self.treview = ttk.Treeview(self.frame4, columns=(1, 2, 3, 4, 5,6,7 ),show='headings',height=18, xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=RIGHT, fill=Y)
        self.scroll_y.pack(side=BOTTOM, fill=X)
        self.style=ttk.Style()
        self.style.configure('Treeview',background='lightgray',foreground='black',rowheight=20)
        self.style.map('Treeview',background=[('selected','green')])

        self.scroll_x.config(command=self.treview.yview)
        
        self.treview.heading(1, text='BOOK ID')
        self.treview.heading(2, text='BOOK NAME')
        self.treview.heading(3, text="BOOK AUTHOR")
        self.treview.heading(4,text='BOOK EDITION')
        self.treview.heading(5,text='BOOK PRICE')
        self.treview.heading(6,text='BOOK QUANTITy')
        self.treview.heading(7,text='PUBLISHER')

        self.treview.column(1, width=100, anchor=CENTER)
        self.treview.column(2, width=120, anchor=CENTER)
        self.treview.column(3, width=120, anchor=CENTER)
        self.treview.column(4, width=100, anchor=CENTER)
        self.treview.column(5, width=120, anchor=CENTER)
        self.treview.column(6,width=140,anchor=CENTER)
        self.treview.column(7,width=100,anchor=CENTER)
  
        self.treview.place(x=0, y=0, width=1495)
        self.treview.bind("<ButtonRelease-1>",self.click_insert)
        self.trre()
#====================== UPDATING TREEVIEW FUNCTION ===============================#

    def trre(self):
        con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
        cur = con.cursor()
        cur.execute("Select * from books_data ")
        self.row = cur.fetchall()
        if len(self.row) != 0:
            self.treview.delete(*self.treview.get_children())
            for i in self.row:
                self.treview.insert('', 'end', values=i)
                con.commit()
      
#==================== ADDING BOOK IN DATABASE FUNCTION =========================#
 
    def add_book(self):
        if self.book_id_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book_ID')
        elif self.book_name_entry.get()=='':
            messagebox.showerror("Library Managemet System",'Please Enter Book Name')
        elif self.book_author_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book Author')
        elif self.book_edition_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book Edition')
        elif self.book_price_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book Price')
        elif self.publish_by_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Publisher Name')
        else:
            con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
            cur = con.cursor()
            cur.execute("SELECT * FROM books_data WHERE book_Id=%s",self.book_id_entry.get())
            row=cur.fetchone()
            if row!=None:
                 messagebox.showwarning("Library Management",'Book already available')
            else: 
                query=("INSERT INTO books_data(book_id,Book_name,Book_author,Book_edition,Book_price,quantity,publish_BY) values ('%s','%s','%s','%s','%s','%s','%s')" %(self.book_id_entry.get(),self.book_name_entry.get(),self.book_author_entry.get(),self.book_edition_entry.get(),self.book_price_entry.get(),self.book_quantity_entry.get(),self.publish_by_entry.get()))
                cur.execute(query)
                con.commit()
                con.close()
                self.trre()
                messagebox.showinfo("Library Management",'Book Added successfully')
         
  #========================== UPDATE DATABASE FUNCTION FOR BOOKS =========================#
    def update(self):
        if self.book_id_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book_ID')
        elif self.book_name_entry.get()=='':
            messagebox.showerror("Library Managemet System",'Please Enter Book Name')
        elif self.book_author_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book Author')
        elif self.book_edition_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book Edition')
        elif self.book_price_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book Price')
        elif self.publish_by_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Publisher Name')
        else:
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("update books_data set Book_name=%s, Book_author=%s, Book_edition=%s, Book_price=%s, quantity=%s, publish_BY=%s where Book_Id=%s",(self.book_name_entry.get(),self.book_author_entry.get(),self.book_edition_entry.get(),self.book_price_entry.get(),self.book_quantity_entry.get(),self.publish_by_entry.get(),self.book_id_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Library Management System",'Book Update Successfully')
            self.trre()

 #===================== BOOK SEARCH FUNCTION ==========================#

    def search(self):
        if self.book_id_entry.get()!='':
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("select * from books_data where Book_Id=%s",self.book_id_entry.get())
            self.data=cur.fetchall()
            if len(self.data) !=0:
                self.treview.delete(*self.treview.get_children())
                for j in self.data:
                    self.treview.insert('','end',values=j)

        elif self.book_name_entry.get()!='':
            con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
            cur = con.cursor()
            cur.execute('SELECT * FROM books_data WHERE book_Name=%s',self.book_name_entry.get())
            self.data=cur.fetchall()
            if len(self.data) !=0:
                self.treview.delete(*self.treview.get_children())
                for j in self.data:
                    self.treview.insert('','end',values=j)
        else:
            messagebox.showerror("Library Management System",'Please Enter Valid Book Name OR BOOK ID')

   #================== BOOK DELETE FUNCTION ======================#
   
    def delete(self):
        if self.book_id_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Book_ID')
        else:
            con=pymysql.connect("localhost",'root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("Delete From books_data Where Book_Id=%s",self.book_id_entry.get())
            con.commit()
            con.close()
            messagebox.showinfo("Library Management System",'Book Delete Successfully')

  #================ CLICK INSERT FUNCTION =====================#
    def click_insert(self,ev):
        self.book_id_entry.delete(0,END)
        self.book_name_entry.delete(0,END)
        self.book_author_entry.delete(0,END)
        self.book_edition_entry.delete(0,END)
        self.book_price_entry.delete(0,END)
        self.book_quantity_entry.delete(0,END)
        self.publish_by_entry.delete(0,END)
        self.cur_rowb=self.treview.focus()
        self.contents=self.treview.item(self.cur_rowb)
        self.rowb=self.contents['values']
        print(self.rowb)
        self.book_id_entry.insert(0,self.rowb[0])
        self.book_name_entry.insert(0,self.rowb[1])
        self.book_author_entry.insert(0,self.rowb[2])
        self.book_edition_entry.insert(0,self.rowb[3])
        self.book_price_entry.insert(0,self.rowb[4])
        self.book_quantity_entry.insert(0,self.rowb[5])
        self.publish_by_entry.insert(0,self.rowb[6])
    
  #================= BACKWARD FUNCTION ===================================#
    def backward(self):
        self.manage.destroy()


#===================================================================== THE END ============================================================#
        



        
        


