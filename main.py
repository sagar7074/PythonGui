from tkinter import *
from PIL import Image,ImageTk,ImageDraw,ImageFont
from tkinter import ttk
from tkinter import messagebox
import pymysql
import datetime
import issue
import return_window
import time
from  tkcalendar import *
import smtplib,ssl
from tkinter import filedialog
import os
from validate_email import validate_email
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import managebooks
import librarin
root=Tk()
class Mainwindow():

    def __init__(self):
            self.root=root
            self.root.title("STAFF LOGIN")
            self.root.geometry("1200x700+160+50")
            self.root.config(bg='black')
            self.root.resizable(FALSE,FALSE)
            self.root.grab_set()
            
            self.Login_label = Label(self.root, text="Library management system", font=("Elephant", 15, 'bold'))
            self.Login_label.place(x=200, y=5)
            self.photo=ImageTk.PhotoImage(file="images/best-colors-websites-1.jpg")
            self.blabel=Label(self.root,image=self.photo)
            self.blabel.pack()
                 
            
#================================== add libarain button ============================================#

            self.addlibrarian_button=Button(self.root,text="ADD LIBRARIAN",cursor='hand2',font=('times new roman',15,'bold'),fg='black'
                                ,bd=2,activebackground='brown',activeforeground='brown',command=lambda:l.add_librarian())
            self.addlibrarian_button.place(x=1000,y=100,width=200)

#===================================== creating frame ==============================================#

            self.frame=Frame(self.root)
            self.frame.place(x=390,y=170,width=400,height=450)

#===========================  LABELS AND BUTTONS FOR LOGIN  ==========================================#

            self.photo0 = ImageTk.PhotoImage(file="images/unnamed.png")
            self.blabel0 = Label(self.root, image=self.photo0,bg='gold2')
            self.blabel0.place(x=0,y=0,width=1200,height=100)

            self.label=Label(self.frame,text="Email_ID",font=("Andalus",15,'bold'),fg='black')
            self.label.place(x=100,y=50)

            self.logo1 = PhotoImage(file='images/profile (2).png')
            self.label.config(image=self.logo1, compound=LEFT)


            self.user_entry=Entry(self.frame,font=('times new roman',15))
            self.user_entry.place(x=100,y=100,width=250)

            self.label = Label(self.frame, text="PASSWORD", font=("Andalus", 15,'bold'),fg='black')
            self.label.place(x=100, y=150)

            self.logo2= PhotoImage(file='images/lock (1).png')
            self.label.config(image=self.logo2, compound=LEFT)

            self.password_entry = Entry(self.frame, font=('times new roman', 15))
            self.password_entry.place(x=100, y=200,width=250)

            self.logo3 = PhotoImage(file='images/LOGIN.png')
            self.log_button=Button(self.frame,bg='#F0F8FF',image=self.logo3,activebackground='white'
                               ,command=lambda:self.admin_login(),font=('Arial Rounded MT Bold',15,'bold'),cursor='hand2',bd=0)
            self.log_button.place(x=125,y=270)

            self.forgett_button=Button(self.frame,text="Forget Password?",cursor='hand2',font=('times new roman',15,'bold'),fg='black'
                                ,bd=0,activebackground='brown',activeforeground='brown',command=lambda:self.adminforgett())
            self.forgett_button.place(x=50,y=380,width=250)

            self.logo4 = PhotoImage(file='images/forgot (1).png')
            self.forgett_button.config(image=self.logo4, compound=LEFT)
 

    #=================================   LIBRARIN RESET PASSWORD WINDOW   ===========================================#

    def adminforgett(self):
            if self.user_entry.get()=='':
                    messagebox.showwarning("LIBRARY MANAGEMENT","Please Enter User_ID To Procced")
            else:
                    con=pymysql.connect("localhost","root","Sagar123","libraray_management")
                    cur=con.cursor()
                    cur.execute("SELECT * FROM  librarin_table where Email=%s",self.user_entry.get())
                    self.row=cur.fetchone()
                    if(self.row==None):
                            messagebox.showwarning("LIBRARY MANAGEMENT","PLEASE ENTER VALID EMAIL ID TO PROCCED")
                    else:
                            forget=Tk()
                            self.forget=forget
                            self.forget.title("FORGET PASSWORD")
                            self.forget.geometry('800x400+390+200')
                            self.forget.resizable(FALSE,FALSE)

                            self.frame_librarin=Frame(self.forget,bg='lightblue')
                            self.frame_librarin.place(x=50,y=50,width=700,height=300)

                            self.ulabel=Label(self.frame_librarin,text='USER_ID',font=('Elephant',15,'bold'),fg='gray')
                            self.ulabel.place(x=60,y=50)

                            self.entry1=Entry(self.frame_librarin,font=('Elephant',15,'bold'),bd=2,relief=GROOVE)
                            i=self.user_entry.get()
                            self.entry1.insert(0,i)
                            self.entry1.config(state='readonly')
                            self.entry1.place(x=60,y=100,width=250)

                            i=[' What is your mothers maiden name?',' What is the name of your first pet? ','  What is the name of the town where you were born?  ']
                            self.comboentry1 = ttk.Combobox(self.frame_librarin,values=i,font=('times new roman',13, 'bold'))
                            self.comboentry1.set("       Select Security Question   ")
                            self.comboentry1.config(state='readonly')
                            self.comboentry1.place(x=360, y=50,width=300,height=30)

                            #self.Librarian_answer_label = Label(self.frame_librarin, text=" ", font=("Andalus", 17,'bold'),bg='lightblue',fg='red')
                            #self.Librarian_answer_label.place(x=360, y=200)

                            self.librarin_answer_entry=Entry(self.frame_librarin,font=('times new roman',15),bd=2,relief=GROOVE)
                            self.librarin_answer_entry.place(x=360,y=100,width=300)

                            self.plabel=Label(self.frame_librarin,text='New Password',font=('times new roman',15,'bold'),fg='gray')
                            self.plabel.place(x=60,y=150)

                            self.entry2=Entry(self.frame_librarin,font=('times new roman',15,'bold'),bg='white',bd=2,relief=GROOVE)
                            self.entry2.place(x=60,y=200,width=250)

                            self.clabel = Label(self.frame_librarin, text='Confirm Password', font=('times new roman', 15, 'bold'),
                                                fg='gray')
                            self.clabel.place(x=360, y=150)

                            self.entry3 = Entry(self.frame_librarin, font=('Elephant', 15, 'bold'),bd=2,relief=GROOVE)
                            self.entry3.place(x=360, y=200, width=250)

                            self.button = Button(self.frame_librarin, text="Change Password", bg='#F0F8FF', activebackground='#00B0F0',command=lambda:self.resetpassword(),
                                                 activeforeground="white", fg='gray',font=('Arial Rounded MT Bold', 15, 'bold'), cursor='hand2')
                            self.button.place(x=260, y=250, height=35)

                            
#=============================  RESET PASSWORD DATABASE QUERY ##########################

    def resetpassword(self):
            if self.entry2.get() != self.entry3.get():
                    messagebox.showwarning("Library Management",'Password Does Not Match')
            elif self.entry2.get()=='' and self.entry3.get()=='':
                    messagebox.showwarning("Library Management",'All fields Are Required')
            elif self.comboentry1.get()=='       Select Security Question   ':
                   messagebox.showerror("Library Management System",'Please Select Security Question')
            elif self.librarin_answer_entry.get()=='':
                messagebox.showerror("Library Management system",'Please Enter answer')
            else:
                 con=pymysql.connect('localhost','root','Sagar123','libraray_management')
                 cur=con.cursor()
                 cur.execute("Select security_question,answer from  librarin_table Where security_question=%s and answer=%s and Email=%s",(self.comboentry1.get(),self.librarin_answer_entry.get(),self.entry1.get()))
                 qa=cur.fetchone()
                 print(qa)
                 if qa!=None: 
                    cur.execute("UPDATE librarin_table SET Password=%s WHERE Email=%s",(self.entry3.get(),self.user_entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Library Management","Password Change Successfully")
                    self.forget.destroy()
                 else:
                    messagebox.showerror("Library Management system",'Wrong Question Or answer')

     #============================= ADMIN LOGIN DATABASE query ======================================#

    def admin_login(self):
            if self.user_entry.get=='' and self.password_entry.get()=='':
                    messagebox.showwarning("Library Management System","All Fields Are Required")
            else:
                 con=pymysql.connect("localhost",'root','Sagar123','libraray_management')
                 cur=con.cursor()
                 cur.execute("SELECT * FROM librarin_table WHERE Email=%s and Password=%s",(self.user_entry.get(),self.password_entry.get()))
                 self.row=cur.fetchone()
                 if(self.row==None):
                         answer=messagebox.askquestion('USER NOT FOUND','Do you want to retry')
                         if answer=='yes':
                             self.user_entry.delete(0,END)
                             self.password_entry.delete(0,END)
                         elif answer=='no':
                             self.root.withdraw()
                 else:
                      con.commit()
                      con.close()
                      self.user_entry.delete(0,END)
                      self.password_entry.delete(0,END)
                      self.root.withdraw()
                      Dashboard=Toplevel()
                      self.Dashboard=Dashboard
                      self.Dashboard.title("HOME PAGE")
                      self.Dashboard.geometry("1527x790+0+0")
                      self.Dashboard.config(bg='#DCDCDC')
                      self.Dashboard.resizable(FALSE,FALSE)

                      self.frame2 = Frame(self.Dashboard,bg='#FFDEAD' )
                      self.frame2.place(x=0, y=0, width=1527, height=80)

                      self.Heading_name = Label(self.frame2, text='!!! LIBRARY MANAGEMENT SYSTEM !!!', font=("Elephant", 20, 'bold'),
                                              bg='#FFDEAD', fg='#483D8B')
                      self.Heading_name.place(x=0, y=0,width=700,height=80)

                      self.name = Label(self.frame2, text="Librarian :",font=("times new roman",15, 'bold'),fg='black')
                      self.name.place(x=1200, y=0,width=165, height=30)

                      self.logo11 = PhotoImage(file='images/user.png')
                      self.name.config(image=self.logo11, compound=LEFT)
                      self.small_logo11 = self.logo11.subsample(1,1)
                      self.name.config(image=self.small_logo11)

                      self.admin_nam = Label(self.frame2, text=self.row[1], font=("times new roman", 15, 'bold'),
                                             fg='black')
                      self.admin_nam.place(x=1365, y=0,width=140, height=30)


       #=========================== DATE LABEL ================================#

                      self.now=datetime.datetime.now()
                      self.now.strftime("%H:%M:%S")

                      self.hdate = Label(self.frame2, text='      DATE       :',
                                        font=("times new roman", 15, 'bold'),
                                        fg='black')
                      self.hdate.place(x=1200, y=36,width=160, height=30)

                      self.date = Label(self.frame2, text=self.now.strftime("%d-%m-%y"), font=("times new roman", 15, 'bold'),fg='black')
                      self.date.place(x=1360, y=36,width=141, height=30)

                      self.frame3 = Frame(self.Dashboard, bg='#FFA500')
                      self.frame3.place(x=0, y=80, width=1527, height=40)

       #=====================================   HOME BUTTON  ===============================================#

                      self.homeb=PhotoImage(file='images/homeee.png')

                      self.Homebutton = Button(self.frame3,image=self.homeb, activebackground='#00B0F0',activeforeground="white",bg='#FFA500', fg='black', font=('times new roman', 12, 'bold'),
                                               cursor='hand2', bd=0)
                      self.Homebutton.place(x=0, y=0, width=100,height=40)

       #========================================  ISSUE BUTTON ===============================================#

                      self.Issuebutton = Button(self.frame3, text="ISUUE_BOOKS",activebackground='#00B0F0',activeforeground="white",
                                                command=lambda:o.issue_window(),bg='#FFA500',fg='black', font=('times new roman', 12, 'bold'), cursor='hand2',bd=0,)
                      self.Issuebutton.place(x=105, y=0, width=120,height=40)

      #=================================================  RETURN BOOK BUTTON =======================================#

                      self.Returnbutton = Button(self.frame3, text="RETURN BOOKS",bg='#FFA500', activebackground='#00B0F0',activeforeground="white",fg='black', font=('times new roman', 12, 'bold'), cursor='hand2',bd=0,command=lambda:r.first())
                      self.Returnbutton.place(x=230, y=0, width=130,height=40)

      #==============================================   MANAGE BOOK BUTTON   ==============================================#

                      self.Deletebutton = Button(self.frame3, text="MANAGE BOOKS", activebackground='#00B0F0',activeforeground="white",
                                                 command=lambda:m.M_window(),bg='#FFA500',fg='black',font=('times new roman', 12, 'bold'), cursor='hand2',bd=0)
                      self.Deletebutton.place(x=374, y=0, width=130,height=40)

      #========================================= REFRESH BUTTON ========================================#

                      self.rbuttonnn = Button(self.frame3, fg='black', activeforeground='white',
                                             bd=0, relief='flat',bg='#FFA500',cursor='hand2',command=lambda:self.trre() )
                      self.rbuttonnn.place(x=550, y=5, width=30)

                      self.log13 = PhotoImage(file='images/refresh-buttons.png')
                      self.rbuttonnn.config(image=self.log13, compound=LEFT)

      #============================================  LOGOUT BUTTON  ======================================#

                      self.logoutb=PhotoImage(file='images/logoutbutton-th.png')
                      self.Logoutbutton = Button(self.frame3,image=self.logoutb,bg='#FFA500',activebackground='#FFA500',command=lambda:self.logout(), cursor='hand2',bd=0)
                      self.Logoutbutton.place(x=1400,y=5)

           #==================================================================================================================#


           #======================================== STUDENT ADDING INFO ==========================================#

                      self.sframe=Frame(self.Dashboard,bg='#F5F5F5',relief=RIDGE,bd=2)
                      self.sframe.place(x=10,y=130,width=1505,height=300)


                      self.Name_label=Label(self.sframe,text='First-NAME',font=('times new roman',15,'bold'),fg='black',bg='#F5F5F5',relief='flat')
                      self.Name_label.place(x=10,y=40)

                      self.student_name_entry=Entry(self.sframe,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
                      self.student_name_entry.place(x=170,y=40,width=250)

                      self.lastName_label=Label(self.sframe,text='Last-Name',font=('times new roman',15,'bold'),fg='black',bg='#F5F5F5',relief='flat')
                      self.lastName_label.place(x=440,y=40)

                      self.student_lname_entry=Entry(self.sframe,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
                      self.student_lname_entry.place(x=580,y=40,width=250)

                      self.class_label=Label(self.sframe,text='Class',font=('times new roman',17,'bold'),fg='black',bg='#F5F5F5',relief='flat')
                      self.class_label.place(x=850,y=40)

                      self.student_class_entry=Entry(self.sframe,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
                      self.student_class_entry.place(x=940,y=40,width=250)

                      self.DOB_label=Label(self.sframe,text='D-O-B(yyyy-mm-dd)',font=('times new roman',13,'bold'),fg='black',bg='#F5F5F5',relief='flat')
                      self.DOB_label.place(x=10,y=100)

                      self.student_DOB_entry=DateEntry(self.sframe, date_pattern='yy-mm-dd',state='readonly',font=('times new roman',15, 'bold'),bg='#F5F5F5',fg='#F5F5F5',relief=GROOVE)
                      self.student_DOB_entry.place(x=170,y=100,width=250)

                      
                      self.Address_label=Label(self.sframe,text='Address',font=('times new roman',15,'bold'),fg='black',bg='#F5F5F5')
                      self.Address_label.place(x=10,y=160)

                      self.student_address_entry=Text(self.sframe,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
                      self.student_address_entry.place(x=170,y=160,width=250,height=70)

                      self.contact_label=Label(self.sframe,text='Cont-No',font=('times new roman',15,'bold'),fg='black',bg='#F5F5F5',relief='flat')
                      self.contact_label.place(x=440,y=100)

                      self.student_contact_entry=Entry(self.sframe,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
                      self.student_contact_entry.place(x=580,y=100,width=250)

                      self.EMAIL_label=Label(self.sframe,text='Email-ID',font=('times new roman',15,'bold'),fg='black',bg='#F5F5F5',relief='flat')
                      self.EMAIL_label.place(x=850,y=100)

                      self.student_EMAIL_entry=Entry(self.sframe,font=('times new roman',15,'bold'),relief=GROOVE ,bd=2)
                      self.student_EMAIL_entry.place(x=940,y=100,width=250)

                      self.genderlabel = Label(self.sframe, text='Gender', font=('times new roman', 15, 'bold'),fg='black', bg='#F5F5F5')
                      self.genderlabel.place(x=440,y=160)
                      i=['       Male       ','        Female      ']
                      self.comboentry = ttk.Combobox(self.sframe,values=i,font=('times new roman',13, 'bold'))
                      self.comboentry.set("       Select Gender   ")
                      self.comboentry.config(state='readonly')
                      self.comboentry.place(x=580, y=160,width=200,height=30)

                      self.upimag_student_button = Button(self.sframe,text='upload image',cursor='hand2', command=lambda: self.show_image(),bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=2,relief=RIDGE)
                      self.upimag_student_button.place(x=900, y=160,width=180)


                      self.bframe=Frame(self.sframe,bg='yellow',relief=RIDGE,bd=2)
                      self.bframe.place(x=1290,y=8,width=200,height=280)

                
                      self.add_student_button = Button(self.bframe,text='Register New',cursor='hand2', command=lambda: self.add_student(),bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=2,relief=RIDGE)
                      self.add_student_button.place(x=10, y=20,width=180)

                     
                      self.update_student_button = Button(self.bframe,text='Update',cursor='hand2', command=lambda: self.update_student(),bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=2,relief=RIDGE)
                      self.update_student_button.place(x=10, y=70,width=180)


                      self.delete_student_button = Button(self.bframe,text='Delete',cursor='hand2', command=lambda: self.delete_student(),bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=2,relief=RIDGE)
                      self.delete_student_button.place(x=10, y=120,width=180)

                      self.clear_student_button = Button(self.bframe,text='Clear',cursor='hand2', command=lambda: self.clear_student(),bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=2,relief=RIDGE)
                      self.clear_student_button.place(x=10, y=170,width=180)

                      self.genrateid_student_button = Button(self.bframe,text='Genrate ID Card',cursor='hand2',bg='#F5F5F5',fg='black',font=('times new roman',15,'bold'),bd=2,relief=RIDGE,command=lambda:self.genrate_card())
                      self.genrateid_student_button.place(x=10, y=220,width=180)
 
#====================== creating treeview ==============================================#

                      self.frame3 = Frame(self.Dashboard, relief='flat',bg='red')
                      self.frame3.place(x=10, y=440, width=1100, height=340)

                      self.scroll_x = ttk.Scrollbar(self.frame3, orient=VERTICAL)
                      self.scroll_y=ttk.Scrollbar(self.frame3,orient=HORIZONTAL)
                      self.treview = ttk.Treeview(self.frame3, columns=(1, 2, 3, 4, 5,6,7,8 ),show='headings',height=15, xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                      self.scroll_x.pack(side=RIGHT, fill=Y)
                      self.scroll_y.pack(side=BOTTOM, fill=X)
                      self.style=ttk.Style()
                      self.style.configure('Treeview',background='lightgray',foreground='black',rowheight=20)
                      self.style.map('Treeview',background=[('selected','green')])

                      self.scroll_x.config(command=self.treview.yview)
                      
                      self.treview.heading(1, text='FIRST NAME')
                      self.treview.heading(2, text='LAST_NAME')
                      self.treview.heading(3, text="CLASS")
                      self.treview.heading(4,text='CONTCAT NO')
                      self.treview.heading(5,text='EMAIL ID')
                      self.treview.heading(6,text='D-O-B')
                      self.treview.heading(7,text='ADDRESS')
                      self.treview.heading(8,text='GENDER')

                      self.treview.column(1, width=100, anchor=CENTER)
                      self.treview.column(2, width=120, anchor=CENTER)
                      self.treview.column(3, width=120, anchor=CENTER)
                      self.treview.column(4, width=100, anchor=CENTER)
                      self.treview.column(5, width=120, anchor=CENTER)
                      self.treview.column(6,width=140,anchor=CENTER)
                      self.treview.column(7,width=100,anchor=CENTER)
                      self.treview.column(8,width=140,anchor=CENTER)
                
                      self.treview.place(x=0, y=0, width=1084)
                      self.trre()
                      self.treview.bind("<ButtonRelease-1>",self.insertint_textbox)

#========================= CREATING FRAME FOR ID CARD =====================================#

    def genrate_card(self): 
        try:
            self.frame4 = Frame(self.Dashboard, relief=GROOVE,bg='lightblue',bd=2)
            self.frame4.place(x=1130, y=440, width=370, height=340)

            self.ID_label=Label(self.frame4,text='ID CARD',font=('times new roman',15,'bold'),fg='white',bg='lightblue',relief='flat')
            self.ID_label.place(x=0,y=0,width=360)

            self.image_label=Label(self.frame4,font=('times new roman',20,'bold'),fg='white',bg='lightblue',relief='flat')
            self.image_label.place(x=150,y=30)


            self.ig=Image.open(self.fln)
            self.ig.thumbnail((150,100))
            self.ig=ImageTk.PhotoImage(self.ig)
            self.image_label.configure(image=self.ig)
            self.image_label.image=self.ig

            self.n_label=Label(self.frame4,text='Name:- ' + self.student_name_entry.get() + self.student_lname_entry.get(),font=('times new roman',15,'bold'),fg='white',bg='lightblue',relief='flat')
            self.n_label.place(x=80,y=150)

            self.c_label=Label(self.frame4,text='Class:-'+ self.student_class_entry.get(),font=('times new roman',15,'bold'),fg='white',bg='lightblue',relief='flat')
            self.c_label.place(x=80,y=180)

            self.co_label=Label(self.frame4,text='Contact :- '+self.student_contact_entry.get(),font=('times new roman',15,'bold'),fg='white',bg='lightblue',relief='flat')
            self.co_label.place(x=80,y=210)

            self.do_label=Label(self.frame4,text='D-O-B:- '+  self.student_DOB_entry.get(),font=('times new roman',15,'bold'),fg='white',bg='lightblue',relief='flat')
            self.do_label.place(x=80,y=240)

            self.AA_label=Label(self.frame4,text='Address:- '+  self.student_address_entry.get(1.0,END),font=('times new roman',15,'bold'),fg='white',bg='lightblue',relief='flat')
            self.AA_label.place(x=80,y=270)

            self.EM_label=Label(self.frame4,text='Email:- '+  self.student_EMAIL_entry.get(),font=('times new roman',12,'bold'),fg='white',bg='lightblue',relief='flat')
            self.EM_label.place(x=80,y=300)
        

#============== CREATING IMAGE FOR IDCARD===========================#

            self.idimage = Image.new("RGB", (1000, 1350), (242, 242, 242))
            self.drawidimage = ImageDraw.Draw(self.idimage)

            (x, y) = (200, 30)
            self.idname = str("ID CARD")
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=150)
            self.drawidimage.text((x, y),self.idname, fill=self.color, font=self.font)

            (x,y)=(350,230)
            self.im=Image.open(self.fln)
            self.im.thumbnail((650,350))
            self.idimage.paste(self.im,(x,y))

            (x, y) = (80, 660)
            self.idname = str("Name:"   +self.student_name_entry.get() + self.student_lname_entry.get())
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=70)
            self.drawidimage.text((x, y), self.idname, fill=self.color, font=self.font)

            (x, y) = (80, 790)
            self.iddesignation = str("CLASS:"   + self.student_class_entry.get())
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=70)
            self.drawidimage.text((x, y), self.iddesignation, fill=self.color, font=self.font)

            (x, y) = (80, 910)
            self.idcontact = str("Contact:"   +self.student_contact_entry.get())
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=70)
            self.drawidimage.text((x, y), self.idcontact, fill=self.color, font=self.font)

            (x, y) = (80, 1030)
            self.iddoj = str("D.O.B:"    +  self.student_DOB_entry.get())
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=70)
            self.drawidimage.text((x, y), self.iddoj, fill=self.color, font=self.font)

            (x, y) = (80, 1150)
            self.idaddress = str("Address:"    +  self.student_address_entry.get(1.0,END))
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=70)
            self.drawidimage.text((x, y), self.idaddress, fill=self.color, font=self.font)
            
            (x,y)=(80,1260)
            self.email = str("Email:"    +  self.student_EMAIL_entry.get())
            self.color = 'rgb(0,0,0)'
            self.font = ImageFont.truetype("arial.ttf", size=70)
            self.drawidimage.text((x, y), self.email, fill=self.color, font=self.font)
            
            self.idimage.save(self.student_name_entry.get()+".png", "PNG")
        except:
            messagebox.showinfo('Library Management System','Please Select image')


    #============================== GETTING IMAGE FROM SYSTEM ===================================#
       
    def show_image(self):
        self.fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select image',filetype=(("jpg file","*.jpg"),("png file","*.png"),("all file","*.*")))

        self.Name_label=Label(self.sframe,text=self.fln,font=('times new roman',8,'bold'),fg='black',bg='#F5F5F5',relief='flat')
        self.Name_label.place(x=900,y=190)

                        
#======================== CLICK INSERT FUNCTION ==========================#

    def insertint_textbox(self,ev):
        self.clear_student()

        self.cur_row=self.treview.focus()
        self.contents=self.treview.item(self.cur_row)
        self.info=self.contents['values']
        print(self.info)
        self.student_name_entry.insert(0,self.info[0])
        self.student_lname_entry.insert(0,self.info[1])
        self.student_class_entry.insert(0,self.info[2])
        self.student_contact_entry.insert(0,self.info[3])
        self.student_EMAIL_entry.insert(0,self.info[4])
        self.student_DOB_entry.insert(0,self.info[5])
        self.student_address_entry.insert(1.0,self.info[6])
        self.comboentry.insert(0,self.info[7])

#=============== FETCHING DATA FROM DATABASE FOR TREEVIEW ======================#                    
                        
    def trre(self):
        con = pymysql.connect('localhost', 'root', 'Sagar123', 'libraray_management')
        cur = con.cursor()
        cur.execute("Select * from student_table ")
        self.row = cur.fetchall()
        if len(self.row) != 0:
            self.treview.delete(*self.treview.get_children())
            for i in self.row:
                self.treview.insert('', 'end', values=i)
                con.commit()

   #===================   ADDING STUDENT IN DATABASE  FUNCTION =============================#
             
    def add_student(self):
        self.n_label=Label(self.sframe,font=('times new roman',12,'bold'),fg='red',bg='white',relief='flat',bd=0)
        self.n_label.place(x=580,y=130)
        self.n_label.configure(text='')
        self.ID_label=Label(self.sframe,font=('times new roman',12,'bold'),fg='red',bg='white',relief='flat',bd=0)
        self.ID_label.place(x=940,y=140)
        self.ID_label.configure(text='')
        if self.student_name_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_lname_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_class_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_address_entry.get(1.0,END)=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_DOB_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_contact_entry.get()=='':
            messagebox.showinfo("Library Management system",'Contact No is Already Registerd')
        elif self.student_EMAIL_entry.get()=='':
            messagebox.showinfo("Library Management system",'Email is Already Registered')
        elif self.comboentry.get()=='Select Gender':
            messagebox.showerror('Library Management System','Please Select gender')
        else:
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("Select STUDENT_EMAIL from student_table where STUDENT_EMAIL=%s",self.student_EMAIL_entry.get())
            email=cur.fetchone()
            print('email=',email)
            if email==None:
                cur.execute("Select STUDENT_CONTACT from student_table where STUDENT_CONTACT=%s",self.student_contact_entry.get())
                contact=cur.fetchone()
                print('contact=',contact)
                if contact==None:
                    self.sent()
                else:
                    self.n_label.configure(text='*Contact No Already Exists')

            else:
                self.ID_label.configure(text='*Email Id Already Exists')
                
    #=======================  SENDING EMAIL ===================================#

    def sent(self):
        print(self.student_EMAIL_entry.get())
        user=#========Enter You Email Id===================
        password='#===================PASSWORD==================='
        reciver=self.student_EMAIL_entry.get()
        msg=MIMEMultipart()
        msg['To']=reciver
        msg['Form']='Library Management System'+'<'+user+'>'
        msg['subject']=" Registration Successful"
        msg_ready=MIMEText('Registration successful')
        msg.attach(msg_ready)
        img=open(self.student_name_entry.get()+".png",'rb').read()
        img_ready=MIMEImage(img,'png',name='Your ID Card')
        msg.attach(img_ready)
        try:
                context_data=ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context_data) as mail:
                    mail.login(user,password)
                    mail.sendmail(user,reciver,msg.as_string())
                
        except:
                self.EMAILerror_label=Label(self.sframe,text='*Invalid Email Address',font=('times new roman',13,'bold'),fg='red',bg='#F5F5F5',relief='flat')
                self.EMAILerror_label.place(x=940,y=140)
                self.student_EMAIL_entry.delete(0,END)

        else:
                con=pymysql.connect('localhost','root','Sagar123','libraray_management')
                cur=con.cursor()
                cur.execute("INSERT INTO student_table(STUDENT_FNAME,STUDENT_LNAME,STUDENT_CLASS, STUDENT_CONTACT, STUDENT_EMAIL, STUDENT_DOB,STUDENT_ADDRESS,GENDER) values ('%s','%s','%s','%s','%s','%s','%s','%s')" %(self.student_name_entry.get(),self.student_lname_entry.get(),self.student_class_entry.get(),self.student_contact_entry.get(),self.student_EMAIL_entry.get(),self.student_DOB_entry.get(),self.student_address_entry.get(1.0,END),self.comboentry.get()))
                con.commit()
                messagebox.showinfo('LIBRARY MANAGEENT SYSTEM','STUDENT ADDED SUCCESSFULLY')
                self.trre()
                self.clear_student()        
    
#===================== CLEARING STUDENT ENTRY FIELDS ========================#

    def clear_student(self):
            self.student_name_entry.delete(0,END)
            self.student_lname_entry.delete(0,END)
            self.student_class_entry.delete(0,END)
            self.student_address_entry.delete(1.0,END)
            self.student_DOB_entry.delete(0,END)
            self.student_contact_entry.delete(0,END)
            self.student_EMAIL_entry.delete(0,END)
            self.comboentry.set("       Select Gender   ")

#==========================    UPDATING STUDENT INFO =======================================#

    def update_student(self):
        if self.student_name_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_lname_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_class_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_address_entry.get(1.0,END)=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_DOB_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
            
        elif self.student_contact_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.student_EMAIL_entry.get()=='':
            messagebox.showinfo("Library Management system",'All Fieds Are Required')
        elif self.comboentry.get()=='Select Gender':
            messagebox.showerror('Library Management System','Please Select gender')
        else:
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("UPDATE student_table set STUDENT_FNAME=%s, STUDENT_LNAME=%s, STUDENT_CLASS=%s, STUDENT_CONTACT=%s, STUDENT_EMAIL=%s, STUDENT_DOB=%s, STUDENT_ADDRESS=%s,GENDER=%s Where STUDENT_CONTACT=%s",(self.student_name_entry.get(),self.student_lname_entry.get(),self.student_class_entry.get(),self.student_contact_entry.get(),self.student_EMAIL_entry.get(),self.student_DOB_entry.get(),self.student_address_entry.get(1.0,END),self.comboentry.get(),self.student_contact_entry.get()))
            con.commit()
            messagebox.showinfo("Library Management System",'Student Update Succesfully')
            self.trre()
        
 #======================= DELETEING STUDENT FROM DATABASE ============================#

    def delete_student(self):
        if self.student_contact_entry.get()=='':
            messagebox.showerror("Library Management System",'Please Enter contact number')
        else:
            con=pymysql.connect('localhost','root','Sagar123','libraray_management')
            cur=con.cursor()
            cur.execute("Delete from student_table where STUDENT_CONTACT=%s",self.student_contact_entry.get())
            con.commit()
            con.close()
            messagebox.showinfo("Library Management System",'Student Delete Successfully')
            self.trre()

    #================================== LOGOUT FUNCTION ======================================#

    def logout(self):
        self.Dashboard.withdraw()
        self.root.deiconify()

   #============================================= CREATING CLASS OBJECT  ==============================================#

o=issue.Opration()
r=return_window.Return()
m=managebooks.Manage()
l=librarin.Library()
ss=Mainwindow()
root.mainloop()

  #====================================================== THE END ==============================================================#
