from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import random
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

#================= ADD librarian function in database =====================#
class Library:
    def add_librarian(self):
        library=Toplevel()
        self.library=library
        self.library.title("ADD LIBRARIAN")
        self.library.geometry("950x400+300+200")
        self.library.configure(bg='white')
        self.library.resizable(FALSE,FALSE)
        self.library.grab_set()

        self.frame_add_librarin=Frame(self.library,bg='lightblue')
        self.frame_add_librarin.place(x=110,y=50,width=730,height=300)


        self.Librarianlabel = Label(self.frame_add_librarin, text="Librarian Name", font=("Andalus", 17,'bold'),bg='lightblue',fg='black')
        self.Librarianlabel.place(x=60, y=50)

        self.librarin_name_entry=Entry(self.frame_add_librarin,font=('times new roman',15,'bold'),bd=2,relief=GROOVE)
        self.librarin_name_entry.place(x=60,y=100,width=220)

        self.Librarian_email_label = Label(self.frame_add_librarin, text="Librarian Email", font=("Andalus", 17,'bold'),bg='lightblue',fg='black')
        self.Librarian_email_label.place(x=360, y=50)

        self.librarin_email_entry=Entry(self.frame_add_librarin,font=('times new roman',15,'bold'),bd=2,relief=GROOVE)
        self.librarin_email_entry.place(x=360,y=100,width=300)

        self.Librarian_contact_label = Label(self.frame_add_librarin, text="Librarian Contact", font=("Andalus", 17,'bold'),bg='lightblue',fg='black')
        self.Librarian_contact_label.place(x=60, y=150)

        self.librarin_contact_entry=Entry(self.frame_add_librarin,font=('times new roman',15,'bold'),bd=2,relief=GROOVE)
        self.librarin_contact_entry.place(x=60,y=200,width=210)


        i=[' What is your mothers maiden name?',' What is the name of your first pet? ','  What is the name of the town where you were born?  ']
        self.comboentry = ttk.Combobox(self.frame_add_librarin,values=i,font=('times new roman',13, 'bold'))
        self.comboentry.set("       Select Security Question   ")
        self.comboentry.config(state='readonly')
        self.comboentry.place(x=360, y=150,width=300,height=30)

        
        self.Librarian_answer_label = Label(self.frame_add_librarin, text=" ", font=("Andalus", 17,'bold'),bg='lightblue',fg='red')
        self.Librarian_answer_label.place(x=360, y=200)

        self.librarin_answer_entry=Entry(self.frame_add_librarin,font=('times new roman',15,'bold'),bd=2,relief=GROOVE)
        self.librarin_answer_entry.place(x=360,y=200,width=300)
       

        self.librarin_answer_entry.bind("<Enter>",self.hover)
        self.librarin_answer_entry.bind("<Leave>",self.hoverleave)


        self.addlibrarian_button=Button(self.frame_add_librarin,text="ADD LIBRARIAN",cursor='hand2',font=('times new roman',15,'bold'),fg='black'
                                ,bd=2,activebackground='brown',activeforeground='brown',command=lambda:self.sent())
        self.addlibrarian_button.place(x=250,y=250,width=200)
        
#======================= creating hover function for answer entry ========================#

    def hover(self,ev):
        self.Librarian_answer_label.configure(text='Enter Your Answer')

    def hoverleave(self,ev):
        self.Librarian_answer_label.configure(text='')
        
#========================== PASSWORD GENRATION USING RANDOM MODULE ======================#
    def Password_genrator(self):
      self.password=random.randrange(10000,90000)
      print(self.password)
      
#======================== ADDING LIBRARAIN IN DATABASE ===================================#

    def add_librarian_query(self):
        if self.librarin_name_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Admin Name')
        elif self.librarin_contact_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Contact No')
        elif self.librarin_email_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Email ID')
        elif self.comboentry.get()=='       Select Security Question   ':
            messagebox.showerror("Library Management system",'Please select Security Question')
        elif self.librarin_answer_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter Answer')
        else:
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("Select Email from librarin_table Where Email=%s",self.librarin_email_entry.get())
            email=cur.fetchone()
            print(email)
            if email==None:
                cur.execute("Insert Into librarin_table(Name, Password, Email, Contact, security_question, answer) values('%s','%s','%s','%s','%s','%s')" %( self.librarin_name_entry.get(),self.password,self.librarin_email_entry.get(),self.librarin_contact_entry.get(),self.comboentry.get(),self.librarin_answer_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Libaray Management System",'Librarrian Added Successfully')
            else:
                messagebox.showerror("Library Management System",'Email Id already exists')

    #========================= SENDING PASSWORD USING EMAIL ===================================#       

    def sent(self):
        self.Password_genrator()
        user=#========Enter You Email Id===================
        password='#===================PASSWORD==================='
        reciver=self.librarin_email_entry.get()
        msg=MIMEMultipart()
        msg['To']=reciver
        msg['Form']='Library Management System'+'<'+user+'>'
        msg['subject']=" Registration Successful "
        msg_ready=MIMEText('Your Password IS'+str(self.password))
        msg.attach(msg_ready)
        try:
                context_data=ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context_data) as mail:
                    mail.login(user,password)
                    mail.sendmail(user,reciver,msg.as_string())

        except:
            messagebox.showerror("Library Management system",'Invalid Email Address')
        
        else:
            self.add_librarian_query()
    #===================================================================== THE END =================================================================#         




    
    