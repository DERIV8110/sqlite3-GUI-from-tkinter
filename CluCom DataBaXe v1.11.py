from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import io
import threading
import webbrowser
import tempfile
from datetime import date


root= Tk()
frame = ttk.Frame(root)
frame.grid(row=0, column=0)
root.geometry("700x480")
my_img1 =ImageTk.PhotoImage(Image.open("C:/python images/highdef1.jpg"))
background_label = ttk.Label(root, image=my_img1)
background_label.place(x=0, y=0)
#above line--> places background without widget distortion using frame in tkinter.

# root.grid_rowconfigure(row number, weight=rows to occupy)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=0)
root.grid_rowconfigure(6, weight=1)
# root.grid_columnconfigure(column number, weight=rows to occupy)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

conn = sqlite3.connect('OPD2.db')
c = conn.cursor()                                   
        #cursor --> commits changes
        #call cursor for any task in db
        #cursor--> makes new table
c.execute("""CREATE TABLE IF NOT EXISTS OPD2(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Photo BLOB,
                                Name TEXT NOT NULL,
                                Username TEXT NOT NULL,
                                Password TEXT NOT NULL,
                                Age INTEGER NOT NULL,
                                Gender TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                Phone INTEGER NOT NULL,
                                Email TEXT NOT NULL,
                                Medical TEXT NOT NULL,
                                Doctor TEXT NOT NULL,
                                Department TEXT NOT NULL,
                                Diagnosis TEXT NOT NULL
                  )""")
conn.commit()
conn.close()
conn = sqlite3.connect('OPD2.db')
c = conn.cursor()  
c.execute("""CREATE TABLE IF NOT EXISTS REC(ID2 INTEGER PRIMARY KEY AUTOINCREMENT,
          Username TEXT,
          History TEXT,
          Documents BLOB,
          Doctor TEXT,
          Department TEXT,
          Diagnosis TEXT,
          DiagnosisDoc BLOB)""")
conn.commit()
conn.close()
conn = sqlite3.connect("APTT.db")
c = conn.cursor()  
c.execute("""CREATE TABLE IF NOT EXISTS APTT(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                USERNAME TEXT NOT NULL,
                                DEPARTMENT TEXT NOT NULL,
                                DOCTORNAME TEXT NOT NULL,
                                DATE TEXT NOT NULL,
                                DESCRIPTION TEXT NOT NULL)""")
conn.commit()
conn.close()

root.title("CluCom DataBaXe")
root.iconbitmap('C:/python images/vapidTech.ico')

def sign_up_patient():
        
        signup_win = Toplevel()               
        signup_win.geometry("700x480")                                                    # .geometry --> set window size in pixels
        signup_win.title("Signup")

        frame = ttk.Frame(signup_win)
        frame.grid(row=0, column=0)
        my_img2 =ImageTk.PhotoImage(Image.open("C:/python images/highdef2.jpg"))
        background_label2 = ttk.Label(signup_win, image=my_img2)
        background_label2.image = my_img2   # <-- attach reference to the widget
        background_label2.place(x=0, y=0)
        style= ttk.Style()
        style.configure("signuplabels.TLabel",
                foreground="white",
                background="crimson")
        style.configure("signupbuttons.TButton",
                foreground="white",
                background="red")
        signup_win.grid_rowconfigure(0,weight= 1)   # <-- ADD HEADING OF WELCOME AND HOSPITAL NAME FOR SIGNUP IN THIS ROW
        signup_win.grid_rowconfigure(1,weight= 0)
        signup_win.grid_rowconfigure(2,weight= 0)
        signup_win.grid_rowconfigure(3,weight= 0)
        signup_win.grid_rowconfigure(4,weight= 0)
        signup_win.grid_rowconfigure(5,weight= 0)
        signup_win.grid_rowconfigure(6,weight= 0)
        signup_win.grid_rowconfigure(7,weight= 0)
        signup_win.grid_rowconfigure(8,weight= 0)
        signup_win.grid_rowconfigure(9,weight= 0)
        signup_win.grid_rowconfigure(10,weight=0)
        signup_win.grid_rowconfigure(11,weight=2)   # <-- PUT SUBMIT BUTTON HERE

        signup_win.grid_columnconfigure(0,weight= 1)   # <-- LIL SPACED FROM LEFT
        signup_win.grid_columnconfigure(1,weight= 1)   # <-- LABELS
        signup_win.grid_columnconfigure(2,weight= 1)   # <-- ENTRY BOXES
        signup_win.grid_columnconfigure(3,weight= 1)   # <-- BUTTONS
        signup_win.grid_columnconfigure(4,weight= 1)   # <-- LIL SPACED FROM RIGHT


        conn= sqlite3.connect('OPD2.db')
        c= conn.cursor()                                     
        #cursor --> commits changes
        #call cursor for any task in db
        #cursor--> makes new table
        c.execute("""CREATE TABLE IF NOT EXISTS OPD2(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Photo BLOB,
                                Name TEXT NOT NULL,
                                Username TEXT NOT NULL,
                                Password TEXT NOT NULL,
                                Age INTEGER NOT NULL,
                                Gender TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                Phone INTEGER NOT NULL,
                                Email TEXT NOT NULL,
                                Medical TEXT NOT NULL,
                                Doctor TEXT NOT NULL,
                                Department TEXT NOT NULL,
                                Diagnosis TEXT NOT NULL
                  )""")
        conn.commit()
        conn.close()
        def submit():
              
               conn= sqlite3.connect('OPD2.db')
               c= conn.cursor()
               c.execute("SELECT * FROM OPD2 WHERE Username = ?",(username_entry.get(),))
               user_check = c.fetchone()
               #print(user_check)
               conn.commit()
               conn.close()
               
               if user_check is None:
                      conn= sqlite3.connect('OPD2.db')
                      c=conn.cursor()
                      c.execute("""INSERT INTO OPD2(Photo,Name,Username,Password,Age,Gender,Address,Phone,Email,Medical,Doctor,Department,Diagnosis) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                 (blob,name_entry.get(),username_entry.get(),password_entry.get(),age_entry.get(),gender_entry.get(),address_entry.get(),phone_entry.get(),email_entry.get(),medical_file_entry.get(),NONE,NONE,NONE))
                      c.execute("""INSERT INTO REC(Username,DiagnosisDoc,Diagnosis) VALUES (?,?,?)""",(username_entry.get(),doc_convert,medical_file_entry.get()))
                      conn.commit()
                      conn.close()
               elif user_check[3]==username_entry.get():
                       messagebox.showinfo("Signup attempt","Username taken!")

        name_entry=ttk.Entry(signup_win,width=30)
        name_entry.grid(row=2,column=2)
        
        username_entry=ttk.Entry(signup_win,width=30)
        username_entry.grid(row=3,column=2)

        password_entry=ttk.Entry(signup_win,width=30)
        password_entry.grid(row=4,column=2)
        
        age_entry=ttk.Entry(signup_win,width=30)
        age_entry.grid(row=5,column=2)

        gender_entry=ttk.Entry(signup_win,width=30)
        gender_entry.grid(row=6,column=2)
        
        address_entry=ttk.Entry(signup_win,width=30)
        address_entry.grid(row=7,column=2)

        phone_entry=ttk.Entry(signup_win,width=30)
        phone_entry.grid(row=8,column=2)

        email_entry=ttk.Entry(signup_win,width=30)
        email_entry.grid(row=9,column=2)

        medical_file_entry=ttk.Entry(signup_win,width=30)  
        medical_file_entry.grid(row=10,column=2)
        medical_file_entry.insert(0,"Describe your medical history here or \nupload photo of prescription.")

        def convert_to_binary(doc):       
                     with open(doc,"rb") as file:
                             doc_upload = file.read()
                     return doc_upload
        def get_docs():
                doc = filedialog.askopenfilename(initialdir="C:/",title="Upload Photo or Document",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("pdf files","*.pdf"),("all files","*.*")))
                if doc:
                        global doc_convert
                        doc_convert = convert_to_binary(doc)
                else:
                        messagebox.showinfo("Error!","No Documents selected")
        medical_history_upload = ttk.Button(signup_win,text="Upload",bootstyle=PRIMARY,command=get_docs).grid(row=10,column=3)   # <-- GIVE COMMAND AND DEF HERE
        photo_label = ttk.Label(signup_win,text='Upload Photo',style="signuplabels.TLabel",font=("Arial","14")).grid(row=1,column=1)
        
        def convert_to_binary(img):       
                             with open(img,"rb") as file:
                                     data = file.read()
                             return data
        
        def open_file_manager():
                img = filedialog.askopenfilename(initialdir="C:/python images",title="Upload Photo",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
                if img:
                        global blob
                        blob = convert_to_binary(img)
                else:
                        messagebox.showinfo("Error!","No Images selected")
        photo_upload_button = ttk.Button(signup_win,                        text="Upload(100x100 pixels*)",bootstyle=PRIMARY,command=open_file_manager).grid(row=1,column=3)   # <-- GIVE COMMAND AND DEF HERE
        name_label           =ttk.Label(signup_win,                           text='Name',style="signuplabels.TLabel",font=("Arial","14")).grid(row=2,column=1,ipadx=25)
        username_label       =ttk.Label(signup_win,                       text='Username',style="signuplabels.TLabel",font=("Arial","14")).grid(row=3,column=1,ipadx=7)
        password_label       =ttk.Label(signup_win,                       text='Password',style="signuplabels.TLabel",font=("Arial","14")).grid(row=4,column=1,ipadx=8)
        age_label            =ttk.Label(signup_win,                            text='Age',style="signuplabels.TLabel",font=("Arial","14")).grid(row=5,column=1,ipadx=17)
        gender_label         =ttk.Label(signup_win,                         text='Gender',style="signuplabels.TLabel",font=("Arial","14")).grid(row=6,column=1,ipadx=3)
        address_label        =ttk.Label(signup_win,                        text='Address',style="signuplabels.TLabel",font=("Arial","14")).grid(row=7,column=1)
        phone_label          =ttk.Label(signup_win,                   text='Phone',style="signuplabels.TLabel",font=("Arial","14")).grid(row=8,column=1,ipadx=10)
        email_label          =ttk.Label(signup_win,                       text='Email ID',style="signuplabels.TLabel",font=("Arial","14")).grid(row=9,column=1,ipadx=2)
        medical_history_label=ttk.Label(signup_win,text='Enter/Upload History',style="signuplabels.TLabel",font=("Arial","14")).grid(row=10,column=1)

        submit_button=        ttk.Button(signup_win,text="Submit",        command=submit,style="signupbuttons.TButton").grid(row=11,column=3,ipadx=10,ipady=5)

def sign_up_staff():
        auth_win = Toplevel()
        auth_win.geometry("700x480")                                                    # .geometry --> set window size in pixels
        auth_win.title("Signup")

        frame = ttk.Frame(auth_win)
        frame.grid(row=0, column=0)
        #my_img2 =ImageTk.PhotoImage(Image.open("C:/python images/highdef2.jpg"))
        #background_label2 = ttk.Label(auth_win, image=my_img2)
        #background_label2.image = my_img2   # <-- attach reference to the widget
        #background_label2.place(x=0, y=0)
        style= ttk.Style()
        style.configure("signuplabels.TLabel",
                foreground="black",
                background="white")
        style.configure("signupbuttons.TButton",
                foreground="black",
                background="white")
        auth_win.grid_rowconfigure(0,weight= 1)   # <-- ADD HEADING OF WELCOME AND HOSPITAL NAME FOR SIGNUP IN THIS ROW
        auth_win.grid_rowconfigure(1,weight= 0)
        auth_win.grid_rowconfigure(2,weight= 0)
        auth_win.grid_rowconfigure(3,weight= 0)
        auth_win.grid_rowconfigure(4,weight= 0)
        auth_win.grid_rowconfigure(5,weight= 0)
        auth_win.grid_rowconfigure(6,weight= 0)
        auth_win.grid_rowconfigure(7,weight= 0)
        auth_win.grid_rowconfigure(8,weight= 0)
        auth_win.grid_rowconfigure(9,weight= 0)
        auth_win.grid_rowconfigure(10,weight=0)
        auth_win.grid_rowconfigure(11,weight=2)   # <-- PUT SUBMIT BUTTON HERE

        auth_win.grid_columnconfigure(0,weight= 1)   # <-- LIL SPACED FROM LEFT
        auth_win.grid_columnconfigure(1,weight= 1)   # <-- LABELS
        auth_win.grid_columnconfigure(2,weight= 1)   # <-- ENTRY BOXES
        auth_win.grid_columnconfigure(3,weight= 1)   # <-- BUTTONS
        auth_win.grid_columnconfigure(4,weight= 1)   # <-- LIL SPACED FROM RIGHT
        
        def verify_auth_code():
                
                if auth_entry.get()=="1234":
                        auth_win.destroy()
                        signup_win = Toplevel()               
                        signup_win.geometry("700x480")                                                    # .geometry --> set window size in pixels
                        signup_win.title("Signup")
                
                        frame = ttk.Frame(signup_win)
                        frame.grid(row=0, column=0)
                        #my_img2 =ImageTk.PhotoImage(Image.open("C:/python images/highdef2.jpg"))
                        #background_label2 = ttk.Label(signup_win, image=my_img2)
                        #background_label2.image = my_img2   # <-- attach reference to the widget
                        #background_label2.place(x=0, y=0)
                        style= ttk.Style()
                        style.configure("signuplabels.TLabel",
                                foreground="black",
                                background="white")
                        style.configure("signupbuttons.TButton",
                                foreground="white",
                                background="cyan")
                        signup_win.grid_rowconfigure(0,weight= 1)   # <-- ADD HEADING OF WELCOME AND HOSPITAL NAME FOR SIGNUP IN THIS ROW
                        signup_win.grid_rowconfigure(1,weight= 0)
                        signup_win.grid_rowconfigure(2,weight= 0)
                        signup_win.grid_rowconfigure(3,weight= 0)
                        signup_win.grid_rowconfigure(4,weight= 0)
                        signup_win.grid_rowconfigure(5,weight= 0)
                        signup_win.grid_rowconfigure(6,weight= 0)
                        signup_win.grid_rowconfigure(7,weight= 0)
                        signup_win.grid_rowconfigure(8,weight= 0)
                        signup_win.grid_rowconfigure(9,weight= 0)
                        signup_win.grid_rowconfigure(10,weight=0)
                        signup_win.grid_rowconfigure(11,weight=2)   # <-- PUT SUBMIT BUTTON HERE
                
                        signup_win.grid_columnconfigure(0,weight= 1)   # <-- LIL SPACED FROM LEFT
                        signup_win.grid_columnconfigure(1,weight= 1)   # <-- LABELS
                        signup_win.grid_columnconfigure(2,weight= 1)   # <-- ENTRY BOXES
                        signup_win.grid_columnconfigure(3,weight= 1)   # <-- BUTTONS
                        signup_win.grid_columnconfigure(4,weight= 1)   # <-- LIL SPACED FROM RIGHT
                
                
                        conn= sqlite3.connect('STAFF.db')
                        c= conn.cursor()                                     
                        #cursor --> commits changes
                        #call cursor for any task in db
                        #cursor--> makes new table
                        c.execute("""CREATE TABLE IF NOT EXISTS STAFF(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                  Username TEXT NOT NULL,
                                  password INTEGER NOT NULL,
                                  Photo BLOB,
                                  Name TEXT NOT NULL,
                                  Email TEXT NOT NULL,
                                  phone INTEGER,
                                  Department TEXT NOT NULL
                                  )""")
                        conn.commit()
                        conn.close()
                        def submit():
                              
                               conn= sqlite3.connect('STAFF.db')
                               c= conn.cursor()
                               c.execute("SELECT * FROM STAFF WHERE Username = ?",(username_entry.get(),))
                               user_check = c.fetchone()
                               #print(user_check)
                               conn.commit()
                               conn.close()
                               
                               if user_check is None:
                                      conn= sqlite3.connect('STAFF.db')
                                      c=conn.cursor()
                                      c.execute("""INSERT INTO STAFF(Username,password,Photo,Name,Email,phone,Department) VALUES (?,?,?,?,?,?,?)""",
                                                 (username_entry.get(),password_entry.get(),blob,name_entry.get(),email_entry.get(),phone_entry.get(),dept.get()))
                                      #c.execute("""INSERT INTO REC(Username,DiagnosisDoc,Diagnosis) VALUES (?,?,?)""",(username_entry.get(),doc_convert,medical_file_entry.get()))
                                      conn.commit()
                                      conn.close()
                                # FIX-->ELIF SHOULD HAVE LOOP TO CHECK THRU ALL EXISTING USERS
                                # FIX-->NORMAL USER HAS ADMIN PRIVILEG
                               elif user_check[3]==username_entry.get():
                                       messagebox.showinfo("Signup attempt","Username taken!")
                        # ENTRY WIDGET SYNTAX AND GRID SYNTAX MUST BE ON DIFFERENT LINES.
                        name_entry=ttk.Entry(signup_win,width=30)
                        name_entry.grid(row=2,column=2)
                        
                        username_entry=ttk.Entry(signup_win,width=30)
                        username_entry.grid(row=3,column=2)
                
                        password_entry=ttk.Entry(signup_win,width=30)
                        password_entry.grid(row=4,column=2)
                
                        phone_entry=ttk.Entry(signup_win,width=30)
                        phone_entry.grid(row=8,column=2)
                
                        email_entry=ttk.Entry(signup_win,width=30)
                        email_entry.grid(row=9,column=2)

                        dept=ttk.Entry(signup_win,width=30)
                        dept.grid(row=10,column=2)
                
                        #medical_file_entry=ttk.Entry(signup_win,width=30)  
                        #medical_file_entry.grid(row=10,column=2)
                        #medical_file_entry.insert(0,"Describe your medical history here or \nupload photo of prescription.")
                        
                        #CONVERTS SELECTED FILE TO BINARY
                        #def convert_to_binary(doc):       
                        #             with open(doc,"rb") as file:
                        #                     doc_upload = file.read()
                        #             return doc_upload
                        ##OPENS FILE EXPLORER TO SELECT FILES
                        #def get_docs():
                        #        doc = filedialog.askopenfilename(initialdir="C:/",title="Upload Photo or Document",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("pdf files","*.pdf"),("all files","*.*")))
                        #        if doc:
                        #                global doc_convert
                        #                doc_convert = convert_to_binary(doc)
                        #        else:
                        #                messagebox.showinfo("Error!","No Documents selected")
                        #medical_history_upload = ttk.Button(signup_win,text="Upload",bootstyle=PRIMARY,command=get_docs).grid(row=10,column=3)   # <-- GIVE COMMAND AND DEF HERE
                        
                        
                        def convert_to_binary(img):       
                                             with open(img,"rb") as file:
                                                     data = file.read()
                                             return data
                        
                        def open_file_manager():
                                img = filedialog.askopenfilename(initialdir="C:/python images",title="Upload Photo",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
                                if img:
                                        global blob
                                        blob = convert_to_binary(img)
                                else:
                                        messagebox.showinfo("Error!","No Images selected")

                        photo_label = ttk.Label(signup_win,text='Upload Photo',style="signuplabels.TLabel",font=("Arial","14")).grid(row=1,column=1)
                        photo_upload_button = ttk.Button(signup_win,                        text="Upload(100x100 pixels*)",bootstyle=PRIMARY,command=open_file_manager).grid(row=1,column=2)   # <-- GIVE COMMAND AND DEF HERE
                        name_label           =ttk.Label(signup_win,                           text='Name',style="signuplabels.TLabel",font=("Arial","14")).grid(row=2,column=1,ipadx=25)
                        username_label       =ttk.Label(signup_win,                       text='Username',style="signuplabels.TLabel",font=("Arial","14")).grid(row=3,column=1,ipadx=7)
                        password_label       =ttk.Label(signup_win,                       text='Password',style="signuplabels.TLabel",font=("Arial","14")).grid(row=4,column=1,ipadx=8)
                        #age_label            =ttk.Label(signup_win,                            text='Age',style="signuplabels.TLabel",font=("Arial","14")).grid(row=5,column=1,ipadx=17)
                        #gender_label         =ttk.Label(signup_win,                         text='Gender',style="signuplabels.TLabel",font=("Arial","14")).grid(row=6,column=1,ipadx=3)
                        #address_label        =ttk.Label(signup_win,                        text='Address',style="signuplabels.TLabel",font=("Arial","14")).grid(row=7,column=1)
                        phone_label          =ttk.Label(signup_win,                   text='Phone',style="signuplabels.TLabel",font=("Arial","14")).grid(row=8,column=1,ipadx=10)
                        email_label          =ttk.Label(signup_win,                       text='Email ID',style="signuplabels.TLabel",font=("Arial","14")).grid(row=9,column=1,ipadx=2)
                        dept_label=ttk.Label(signup_win,text='Department',style="signuplabels.TLabel",font=("Arial","14")).grid(row=10,column=1)
                
                        submit_button=        ttk.Button(signup_win,text="Submit",        command=submit,style="signupbuttons.TButton").grid(row=11,column=3,ipadx=10,ipady=5)
                else:
                        messagebox.showerror("Authenticator","authentication failed!")
        auth_label = ttk.Label(auth_win,text="Enter Authentication Key>", font=("Segoe UI", 24, "bold")).grid(row=6,column=0,columnspan=2)
        global auth_entry
        auth_entry = ttk.Entry(auth_win,width=30)
        auth_entry.grid(row=6,column=2)
        auth_button = ttk.Button(auth_win,text="Verify",command=verify_auth_code).grid(row=6,column=3)

def Login():
        global user
        #print(user.get())
        if user.get()==3:
              
              conn= sqlite3.connect('OPD2.db')
              c= conn.cursor()
              c.execute("SELECT * FROM OPD2 WHERE Username = ? AND Password = ?",(e.get(),f.get()))
              user_fetch = c.fetchall()
              conn.commit()
              conn.close()
              #print(user_fetch) # <-- LIFE SAVER!!!!


              #c.fetchone()-->returns tuple-->use index to get string value of username
              if len(user_fetch)==0:
                      messagebox.showerror("Login attempt","Invalid Username or Password!")
              elif user_fetch is None:
                      messagebox.showerror("Login attempt","Username does not exist")

              elif user_fetch[0][3]==e.get() and user_fetch[0][4]==f.get():
                      
                      #OPEN ADMIN TAB

                      new_win = Toplevel()
                      frame = ttk.Frame(new_win)
                      frame.grid(row=0, column=0)
                      new_win.geometry("1200x700")

                      my_tab2 = ttk.Notebook(new_win,bootstyle=DARK)
                      my_tab2.grid(row=0,column=0)
                      #JUST ADD MORE FRAMES IN NOTEBOOK--> MORE TABS
                      #NOTEBOOK IS BUILD ON TOPLEVEL PATDASH--> USE my_frame instead of pat_dash
                      my_frame11 = Frame(my_tab2)
                      my_frame21 = Frame(my_tab2)

                      #my_frame1.grid()
                      #my_frame2.grid()

                      my_tab2.add(my_frame11,text="Patient Data")
                      my_tab2.add(my_frame21,text="Staff Data"  )

                      # root.grid_rowconfigure(row number, weight=rows to occupy)
                      new_win.grid_rowconfigure(0, weight=0)
                      new_win.grid_rowconfigure(1, weight=0)
                      new_win.grid_rowconfigure(2, weight=0)
                      new_win.grid_rowconfigure(3, weight=0)
                      new_win.grid_rowconfigure(4, weight=1)
                      # root.grid_columnconfigure(column number, weight=rows to occupy)
                      
                      new_win.grid_columnconfigure(0, weight=1)
                      new_win.grid_columnconfigure(1, weight=0)
                      new_win.grid_columnconfigure(2, weight=0)
                      new_win.grid_columnconfigure(3, weight=0)
                      new_win.grid_columnconfigure(4, weight=0)
                      new_win.grid_columnconfigure(5, weight=0)
                      new_win.grid_columnconfigure(6, weight=0)
                      new_win.grid_columnconfigure(7, weight=1)
                      
                      conn= sqlite3.connect('OPD2.db')
                      c=conn.cursor()
                      
                      c.execute("""CREATE TABLE IF NOT EXISTS OPD2(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Photo BLOB,
                                Name TEXT NOT NULL,
                                Username TEXT NOT NULL,
                                Password TEXT NOT NULL,
                                Age INTEGER NOT NULL,
                                Gender TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                Phone INTEGER NOT NULL,
                                Email TEXT NOT NULL,
                                Medical TEXT NOT NULL,
                                Doctor TEXT NOT NULL,
                                Department TEXT NOT NULL,
                                Diagnosis TEXT NOT NULL

                              )""")
                      
                      conn.commit()
                      conn.close() 
                      def show():
                                # FOR PATIENT DB
                                conn= sqlite3.connect('OPD2.db')
                                c= conn.cursor()
                                c.execute("PRAGMA table_info(OPD2)")
                                columns_info = c.fetchall()
                                #col[1]--> selects all 2nd columns-->column names from entries table
                                col_names = ["ID","Name","Username","Password","Age","Gender","Address","Phone","Email","Medical History","Doctor","Department","Diagnosis"]     
                                c.execute("SELECT ID,Name,Username,Password,Age,Gender,Address,Phone,Email,Medical,Doctor,Department,Diagnosis FROM OPD2")
                                entries = c.fetchall()
                      # STAFF and PATIENT FETCH CAN BE INTEGRATED INTO ONE ONE CURSOR FETCH 
                      # INSTEAD OF TWO
                                conn.commit()
                                conn.close()
                                # FOR STAFF DB
                                conn= sqlite3.connect('STAFF.db')
                                c= conn.cursor()
                                c.execute("PRAGMA table_info(STAFF)")
                                columns_info2 = c.fetchall()
                                #col[1]--> selects all 2nd columns-->column names from entries table
                                col_names2 = ["ID","Username","Password","Name","Email","Phone","Department"]     
                                c.execute("SELECT ID,Username,Password,Name,Email,Phone,Department FROM STAFF")
                                entries2 = c.fetchall()
                      
                                conn.commit()
                                conn.close()
                                # FOR PATIENT DB
                                tree = ttk.Treeview(my_frame11,columns=col_names,show="headings",bootstyle=INFO)
                                for colm in col_names:
                                      
                                       tree.heading(colm, text=colm)
                                       
                                       tree.column(colm,width=90)
                                for row in entries:
                                       
                                       tree.insert("", "end", values=row)
                                tree.grid(row=4,column=2,columnspan=5,sticky="nsew")

                                # FOR STAFF DB
                                tree = ttk.Treeview(my_frame21,columns=col_names2,show="headings",bootstyle=INFO)
                                for colm in col_names2:
                                       #for colm in col_names--> extracts all column names by help of [col[1] for col in columns_info] one by one
                                       tree.heading(colm, text=colm)
                                       #makes columns based on number of columns retreived using [col[1] for col in columns_info]-->headings
                                       tree.column(colm,width=90,anchor="center")
                                for row in entries2:
                                       #inserts rows from db to treeview ""-->(start) to tk.END--> values=rows of db one by one
                                       tree.insert("", "end", values=row)
                                tree.grid(row=4,column=2,columnspan=5,sticky="nsew")

        
                      button_show_all= ttk.Button(new_win,text="Show All",command=show)
                      button_show_all.grid(column=0,row=1,columnspan=2)
                      
                      
              else:
                      messagebox.showerror("Login attempt","Invalid Username or Password!")
        if user.get()==2:
                conn= sqlite3.connect('STAFF.db')
                c= conn.cursor()
                c.execute("SELECT * FROM STAFF WHERE Username = ? AND Password = ?",(e.get(),f.get()))
                staff_lst_fetch = c.fetchall()
                staff_img = staff_lst_fetch[0][3]
                conn.commit()
                conn.close()
                #print(staff_lst_fetch[0]) # <-- LIFE SAVER!!!!
  
  
                #c.fetchone()-->returns tuple-->use index to get string value of username
                if len(staff_lst_fetch)==0:
                        messagebox.showerror("Login attempt","Invalid Username or Password!")
                elif staff_lst_fetch is None:
                        messagebox.showerror("Login attempt","Username does not exist")
  
                elif staff_lst_fetch[0][1]==e.get() and staff_lst_fetch[0][2]==f.get():
                       med_win = Toplevel()
                       med_win.geometry("720x360")
                       frame = ttk.Frame(med_win)
                       frame.grid(row=0, column=0)
                                             # root.grid_rowconfigure(row number, weight=rows to occupy)
                       med_win.grid_rowconfigure(0, weight=2)
                       med_win.grid_rowconfigure(1, weight=2)
                       med_win.grid_rowconfigure(2, weight=2)
                       med_win.grid_rowconfigure(3, weight=2)
                       med_win.grid_rowconfigure(4, weight=2)
                       med_win.grid_rowconfigure(5, weight=2)
                       med_win.grid_rowconfigure(6, weight=2)
                       med_win.grid_rowconfigure(7, weight=2)
                       # root.grid_columnconfigure(column number, weight=rows to occupy)
                       
                       med_win.grid_columnconfigure(0, weight=2)
                       med_win.grid_columnconfigure(1, weight=2)
                       med_win.grid_columnconfigure(2, weight=2)
                       med_win.grid_columnconfigure(3, weight=2)
                       med_win.grid_columnconfigure(4, weight=2)
                       med_win.grid_columnconfigure(5, weight=2)
                       #Notebook function creates navigation pages/tabs based on same frame but different page
                       med_tab = ttk.Notebook(med_win,bootstyle=INFO)
                       med_tab.grid(row=0,column=0,rowspan=8,columnspan=6,sticky="nsew")
                       #JUST ADD MORE FRAMES IN NOTEBOOK--> MORE TABS
                       #NOTEBOOK IS BUILD ON TOPLEVEL PATDASH--> USE my_frame instead of pat_dash
                       my_frame31 = Frame(med_tab)
                       my_frame32 = Frame(med_tab)
                       my_frame33 = Frame(med_tab)
                       med_tab.add(my_frame31,text="Dashboard")
                       med_tab.add(my_frame32,text="Manage Aptts"  )
                       med_tab.add(my_frame33,text="Log Out")
                       my_frame31.grid_rowconfigure(0, weight=2)
                       my_frame31.grid_rowconfigure(1, weight=2)
                       my_frame31.grid_rowconfigure(2, weight=2)
                       my_frame31.grid_rowconfigure(3, weight=2)
                       my_frame31.grid_rowconfigure(4, weight=2)
                       my_frame31.grid_rowconfigure(5, weight=2)
                       my_frame31.grid_rowconfigure(6, weight=2)
                       my_frame31.grid_rowconfigure(7, weight=2)
                       my_frame31.grid_columnconfigure(0, weight=2)
                       my_frame31.grid_columnconfigure(1, weight=2)
                       my_frame31.grid_columnconfigure(2, weight=2)
                       my_frame31.grid_columnconfigure(3, weight=2)
                       my_frame31.grid_columnconfigure(4, weight=2)
                       my_frame31.grid_columnconfigure(5, weight=2)
                       my_frame31.grid_columnconfigure(6, weight=2)
                       my_frame31.grid_columnconfigure(7, weight=2)
                       my_frame31.grid_columnconfigure(8, weight=2)
                       my_frame31.grid_columnconfigure(9, weight=2)
                       my_frame32.grid_rowconfigure(0, weight=2)
                       my_frame32.grid_rowconfigure(1, weight=2)
                       my_frame32.grid_rowconfigure(2, weight=2)
                       my_frame32.grid_rowconfigure(3, weight=2)
                       my_frame32.grid_rowconfigure(4, weight=2)
                       my_frame32.grid_rowconfigure(5, weight=2)
                       my_frame32.grid_rowconfigure(6, weight=2)
                       my_frame32.grid_rowconfigure(7, weight=2)
                       my_frame32.grid_columnconfigure(0, weight=2)
                       my_frame32.grid_columnconfigure(1, weight=2)
                       my_frame32.grid_columnconfigure(2, weight=2)
                       my_frame32.grid_columnconfigure(3, weight=2)
                       my_frame32.grid_columnconfigure(4, weight=2)
                       my_frame32.grid_columnconfigure(5, weight=2)
                       my_frame33.grid_rowconfigure(0, weight=2)
                       my_frame33.grid_rowconfigure(1, weight=2)
                       my_frame33.grid_rowconfigure(2, weight=2)
                       my_frame33.grid_rowconfigure(3, weight=2)
                       my_frame33.grid_rowconfigure(4, weight=2)
                       my_frame33.grid_rowconfigure(5, weight=2)
                       my_frame33.grid_rowconfigure(6, weight=2)
                       my_frame33.grid_rowconfigure(7, weight=2)
                       my_frame33.grid_columnconfigure(0, weight=2)
                       my_frame33.grid_columnconfigure(1, weight=2)
                       my_frame33.grid_columnconfigure(2, weight=2)
                       my_frame33.grid_columnconfigure(3, weight=2)
                       my_frame33.grid_columnconfigure(4, weight=2)
                       my_frame33.grid_columnconfigure(5, weight=2)
       
                       style.configure("medlabels.TLabel",
                       foreground="black",
                       background="white")
                       
                       style.configure("meddatalabels.TLabel",
                       foreground="black",
                       background="white")
       
                       style.configure("meddatabtns.TButton",
                       foreground="black",
                       background="white")

                       # FOR STAFF DB
                       conn= sqlite3.connect('APTT.db')
                       c= conn.cursor()
                       c.execute("PRAGMA table_info(APTT)")
                       columns_info3 = c.fetchall()
                       #col[1]--> selects all 2nd columns-->column names from entries table
                       col_names3 = ["ID","USERNAME","DEPARTMENT","DOCTORNAME","DATE","DESCRIPTION"]     
                       c.execute("SELECT ID,USERNAME,DEPARTMENT,DOCTORNAME,DATE,DESCRIPTION FROM APTT")
                       entries3 = c.fetchall()
                       
                       conn.commit()
                       conn.close()

                       doc_label = ttk.Label(my_frame31,text="Welcome Dr.",style="medlabels.TLabel",font=("Arial","16")).grid(row=1,column=0)
                       for docs in staff_lst_fetch:
                               #print(docs)
                               if docs[1]==e.get():
                                       #print(docs[4])
                                       doc_name_label = ttk.Label(my_frame31,text=docs[4],style="medlabels.TLabel",font=("Arial","16")).grid(row=1,column=1)
                                       with io.BytesIO(staff_img) as file_like:
                                           converted2  = Image.open(file_like).convert("RGBA")
                                       img_reference2 = ImageTk.PhotoImage(converted2)
                                       staff_img_place = ttk.Label(my_frame31, image=img_reference2)
                                       staff_img_place.image = img_reference2  # <-- attach reference to the widget
                                       staff_img_place.grid(row=1,column=2)    
                               else:
                                       pass
                       # FOR STAFF DB--> SEEING APTTS
                       tree = ttk.Treeview(my_frame32,columns=col_names3,show="headings",bootstyle=PRIMARY)
                       for colm in col_names3:
                              tree.heading(colm, text=colm)
                              tree.column(colm,width=90,anchor="center")
                       for row in entries3:
                              tree.insert("", "end", values=row)
                       tree.grid(row=3,column=4,columnspan=5)
                       
                       def delete_appt():
                                
                                appt_id = ttk.Entry(my_frame32,width=30)
                                appt_id.insert(0,"Enter Appointment ID to delete")
                                appt_id.grid(row=2,column=0)
                                def delete_id():

                                        conn= sqlite3.connect('APTT.db')
                                        c= conn.cursor()
                                        c.execute("DELETE FROM APTT WHERE id=?",(appt_id.get(),))   # DONT FORGET THE COMMA--> MAKE A TUPLE
                                 
                                        conn.commit()
                                        conn.close()
                                Delete_aptts = ttk.Button(my_frame32,text="Delete",command=delete_id,bootstyle=DANGER).grid(row=4,column=0,columnspan=2)
                                
                       Delete_aptts = ttk.Button(my_frame32, text="Delete Appointments",command=delete_appt,bootstyle=INFO).grid(row=0,column=0)

                       def refresh_treeview():
                               conn= sqlite3.connect('APTT.db')
                               c= conn.cursor()
                               c.execute("PRAGMA table_info(APTT)")
                               columns_info3 = c.fetchall()
                               col_names3 = ["ID","USERNAME","DEPARTMENT","DOCTORNAME","DATE","DESCRIPTION"]     
                               c.execute("SELECT ID,USERNAME,DEPARTMENT,DOCTORNAME,DATE,DESCRIPTION FROM APTT")
                               entries3 = c.fetchall()
                       
                               conn.commit()
                               conn.close()

                               tree = ttk.Treeview(my_frame32,columns=col_names3,show="headings",bootstyle=PRIMARY)
                               for colm in col_names3:
                                        tree.heading(colm, text=colm)
                                        tree.column(colm,width=90,anchor="nsew")
                               for row in entries3:
                                        tree.insert("", "end", values=row)
                               tree.grid(row=4,column=2,columnspan=5,sticky="w")
                       refresh_aptts = ttk.Button(my_frame32,text="Refresh Appointments",command=refresh_treeview,bootstyle=INFO).grid(row=5,column=0)
                       def staff_logout():
                              med_win.destroy()
                       staff_logout_label =ttk.Label(my_frame33,   text="Log off your Account>",font=("Segoe UI", 24)).grid(row=3,column=1) 
                       staff_logout_button = ttk.Button(my_frame33,text="LOG OUT",bootstyle=DANGER,command=staff_logout).grid(column=5,row=3,ipadx=7)
        if user.get()==1:
              
              conn= sqlite3.connect('OPD2.db')
              c= conn.cursor()
              c.execute("SELECT * FROM OPD2 WHERE Username = ? AND Password = ?",(e.get(),f.get()))
              user_fetch = c.fetchall()
              conn.commit()
              conn.close()
              #print(user_fetch) # <-- LIFE SAVER!!!!
              #c.fetchone()-->returns tuple-->use index to get string value of username
              if len(user_fetch)==0:
                      messagebox.showerror("Login attempt","Invalid Username or Password!")
              elif user_fetch is None:
                      messagebox.showerror("Login attempt","Username does not exist")

              elif user_fetch[0][3]==e.get() and user_fetch[0][4]==f.get():
                      
                      #PATIENT TAB
                      
                      pat_dash = Toplevel()
                      pat_dash.geometry("720x360")
                      frame = ttk.Frame(pat_dash)
                      frame.grid(row=0, column=0)
                                            # root.grid_rowconfigure(row number, weight=rows to occupy)
                      pat_dash.grid_rowconfigure(0, weight=2)
                      pat_dash.grid_rowconfigure(1, weight=2)
                      pat_dash.grid_rowconfigure(2, weight=2)
                      pat_dash.grid_rowconfigure(3, weight=2)
                      pat_dash.grid_rowconfigure(4, weight=2)
                      pat_dash.grid_rowconfigure(5, weight=2)
                      pat_dash.grid_rowconfigure(6, weight=2)
                      pat_dash.grid_rowconfigure(7, weight=2)
                      # root.grid_columnconfigure(column number, weight=rows to occupy)
                      
                      pat_dash.grid_columnconfigure(0, weight=2)
                      pat_dash.grid_columnconfigure(1, weight=2)
                      pat_dash.grid_columnconfigure(2, weight=2)
                      pat_dash.grid_columnconfigure(3, weight=2)
                      pat_dash.grid_columnconfigure(4, weight=2)
                      pat_dash.grid_columnconfigure(5, weight=2)
                      #Notebook function creates navigation pages/tabs based on same frame but different page
                      my_tab = ttk.Notebook(pat_dash,bootstyle=DARK)
                      my_tab.grid(row=0,column=0,rowspan=8,columnspan=6,sticky="nsew")
                      #JUST ADD MORE FRAMES IN NOTEBOOK--> MORE TABS
                      #NOTEBOOK IS BUILD ON TOPLEVEL PATDASH--> USE my_frame instead of pat_dash
                      my_frame1 = Frame(my_tab)
                      my_frame2 = Frame(my_tab)
                      my_frame3 = Frame(my_tab)
                      my_frame4 = Frame(my_tab)
                      my_frame5 = Frame(my_tab)
                      my_frame6 = Frame(my_tab)
                      #my_frame1.grid()
                      #my_frame2.grid()

                      my_tab.add(my_frame1,text="Dashboard")
                      my_tab.add(my_frame2,text="Documents"  )
                      my_tab.add(my_frame3,text="Appointment")
                      my_tab.add(my_frame4,text="Update details")
                      my_tab.add(my_frame5,text="Settings")
                      my_tab.add(my_frame6,text="Log Out"  )
                      my_frame1.grid_rowconfigure(0, weight=2)
                      my_frame1.grid_rowconfigure(1, weight=2)
                      my_frame1.grid_rowconfigure(2, weight=2)
                      my_frame1.grid_rowconfigure(3, weight=2)
                      my_frame1.grid_rowconfigure(4, weight=2)
                      my_frame1.grid_rowconfigure(5, weight=2)
                      my_frame1.grid_rowconfigure(6, weight=2)
                      my_frame1.grid_rowconfigure(7, weight=2)

                      my_frame1.grid_columnconfigure(0, weight=2)
                      my_frame1.grid_columnconfigure(1, weight=2)
                      my_frame1.grid_columnconfigure(2, weight=2)
                      my_frame1.grid_columnconfigure(3, weight=2)
                      my_frame1.grid_columnconfigure(4, weight=2)
                      my_frame1.grid_columnconfigure(5, weight=2)

                      my_frame2.grid_rowconfigure(0, weight=2)
                      my_frame2.grid_rowconfigure(1, weight=2)
                      my_frame2.grid_rowconfigure(2, weight=2)
                      my_frame2.grid_rowconfigure(3, weight=2)
                      my_frame2.grid_rowconfigure(4, weight=2)
                      my_frame2.grid_rowconfigure(5, weight=2)
                      my_frame2.grid_rowconfigure(6, weight=2)
                      my_frame2.grid_rowconfigure(7, weight=2)

                      my_frame2.grid_columnconfigure(0, weight=2)
                      my_frame2.grid_columnconfigure(1, weight=2)
                      my_frame2.grid_columnconfigure(2, weight=2)
                      my_frame2.grid_columnconfigure(3, weight=2)
                      my_frame2.grid_columnconfigure(4, weight=2)
                      my_frame2.grid_columnconfigure(5, weight=2)

                      my_frame3.grid_rowconfigure(0, weight=2)
                      my_frame3.grid_rowconfigure(1, weight=2)
                      my_frame3.grid_rowconfigure(2, weight=2)
                      my_frame3.grid_rowconfigure(3, weight=2)
                      my_frame3.grid_rowconfigure(4, weight=2)
                      my_frame3.grid_rowconfigure(5, weight=2)
                      my_frame3.grid_rowconfigure(6, weight=2)
                      my_frame3.grid_rowconfigure(7, weight=2)

                      my_frame3.grid_columnconfigure(0, weight=2)
                      my_frame3.grid_columnconfigure(1, weight=2)
                      my_frame3.grid_columnconfigure(2, weight=2)
                      my_frame3.grid_columnconfigure(3, weight=2)
                      my_frame3.grid_columnconfigure(4, weight=2)
                      my_frame3.grid_columnconfigure(5, weight=2)

                      my_frame6.grid_rowconfigure(0, weight=2)
                      my_frame6.grid_rowconfigure(1, weight=2)
                      my_frame6.grid_rowconfigure(2, weight=2)
                      my_frame6.grid_rowconfigure(3, weight=2)
                      my_frame6.grid_rowconfigure(4, weight=2)
                      my_frame6.grid_rowconfigure(5, weight=2)
                      my_frame6.grid_rowconfigure(6, weight=2)
                      my_frame6.grid_rowconfigure(7, weight=2)

                      my_frame6.grid_columnconfigure(0, weight=2)
                      my_frame6.grid_columnconfigure(1, weight=2)
                      my_frame6.grid_columnconfigure(2, weight=2)
                      my_frame6.grid_columnconfigure(3, weight=2)
                      my_frame6.grid_columnconfigure(4, weight=2)
                      my_frame6.grid_columnconfigure(5, weight=2)
                     
                      style.configure("dashlabels.TLabel",
                      foreground="black",
                      background="white")
                      
                      style.configure("dashdatalabels.TLabel",
                      foreground="black",
                      background="white")

                      style.configure("welcomelabel.TLabel",
                      foreground="black",
                      background="white")
                      #def show_dash():
                                                                 
                      conn= sqlite3.connect('OPD2.db')
                      c= conn.cursor()
                      c.execute("PRAGMA table_info(OPD2)")
                      columns_info = c.fetchall()
                      #print(columns_info)
                      #col[1]--> selects all 2nd columns-->column names from entries table
                      col_names = [col[1] for col in columns_info]
                      #print(col_names)      
                      c.execute("SELECT ID,Photo,Name,Age,Gender,Address,Phone,Email,Medical,Doctor,Department,Diagnosis FROM OPD2 WHERE Username = ?",(e.get(),))
                      entries = c.fetchall()
                      #print(entries)
                      conn.commit()
                      conn.close()
                      binary_to_img = entries[0][1]
                      def convert_to_image(binary_to_img):       
                            with io.BytesIO(binary_to_img) as file_like:
                              converted = Image.open(file_like).convert("RGBA")
                            return converted
                      blob_2 = convert_to_image(binary_to_img)
                      img_reference = ImageTk.PhotoImage(blob_2)
                      pat_img = ttk.Label(my_frame1, image=img_reference)
                      pat_img.image = img_reference  # <-- attach reference to the widget
                      pat_img.grid(row=2,column=1)               
                      welcome_patient = ttk.Label(my_frame1,text="Welcome!",   font=("Segoe UI", 24, "bold"),style="dashlabels.TLabel").grid(column=0,row=1)   
                      ID_label =        ttk.Label(my_frame1,text="ID",         font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=2)
                      photo_label =     ttk.Label(my_frame1,text="Photo",      font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=1)
                      name_label =      ttk.Label(my_frame1,text="Name",       font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=3)
                      age_label =       ttk.Label(my_frame1,text="Age",        font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=4)
                      gender_label =    ttk.Label(my_frame1,text="Gender",     font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=3,column=1)
                      address_label =   ttk.Label(my_frame1,text="Address",    font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=3,column=2)
                      phone_label =     ttk.Label(my_frame1,text="Phone",      font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=3,column=3)
                      email_label =     ttk.Label(my_frame1,text="Email",      font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=3,column=4)
                      medical_label =   ttk.Label(my_frame1,text="History",    font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=5,column=1)
                      doctor_label =    ttk.Label(my_frame1,text="Doctor Name",font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=5,column=2)
                      department_label =ttk.Label(my_frame1,text="Department", font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=5,column=3)
                      diagnosis_label = ttk.Label(my_frame1,text="Diagnosis",  font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=5,column=4)
                      # DATA INPUT BELOW
                      ID2_label =       ttk.Label(my_frame1,       text=entries[0][0],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=2,column=2)      
                                #photo2_label = ttk.Label(pat_dash,image=img_reference).grid(row=2,column=2)      
                      name2_label =     ttk.Label(my_frame1,       text=entries[0][2],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=2,column=3)
                      age2_label =      ttk.Label(my_frame1,       text=entries[0][3],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=2,column=4)
                      gender2_label =   ttk.Label(my_frame1,       text=entries[0][4],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=4,column=1)
                      address2_label =  ttk.Label(my_frame1,       text=entries[0][5],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=4,column=2)
                      phone2_label =    ttk.Label(my_frame1,       text=entries[0][6],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=4,column=3)
                      email2_label =    ttk.Label(my_frame1,       text=entries[0][7],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=4,column=4)
                      medical2_label =  ttk.Label(my_frame1,       text=entries[0][8],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=6,column=1)
                      doctor2_label =   ttk.Label(my_frame1,       text=entries[0][9],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=6,column=2)
                      departmen2t_label=ttk.Label(my_frame1,      text=entries[0][10],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=6,column=3)
                      diagnosis2_label =ttk.Label(my_frame1,      text=entries[0][11],font=("Segoe UI", 12),style="dashdatalabels.TLabel").grid(row=6,column=4)      
                                
                      
                      # DOCUMENTS PAGE                        
                      conn= sqlite3.connect('OPD2.db')
                      c= conn.cursor()
                      c.execute("SELECT Diagnosis,DiagnosisDoc,Documents,History FROM REC WHERE Username = ?",(e.get(),))
                      doc_out = c.fetchall()
                      conn.commit()
                      conn.close()      
                      print(doc_out)   # <----CHECK OUTPUT      
                      if len(doc_out)==0:
                              messagebox.showinfo("Attention!","Medical Documents\nnot found.")
                      elif len(doc_out)>0:
                              
                              pdf_doc = doc_out[0][1]
                      def open_file():
                                      #write to a temporary file
                                      #pdf is converted by with and stored locally on a temp location with temp path
                                      with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
                                              tmp_file.write(pdf_doc)
                                              temp_pdf_path = tmp_file.name  
                                              webbrowser.open_new(temp_pdf_path)
                            
                              
                      diagnosis4_label   =  ttk.Label(my_frame2,text="Diagnosis",     font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=1)
                      diagnosisdoc2_label = ttk.Label(my_frame2,text="Diagnosis Docs",font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=2)
                      documents2_label    = ttk.Label(my_frame2,text="Other Docs",    font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=3)
                      #history2_label      = ttk.Label(my_frame2,text="History",       font=("Segoe UI", 14, "bold"),style="dashlabels.TLabel").grid(row=1,column=4)
 
                      diagnosisdoc_button =ttk.Button(my_frame2,text="Open in Browser",bootstyle=DARK,command=open_file).grid(row=2,column=2)
                      if len(doc_out)==0:
                              messagebox.showinfo("Attention!","No Diagnosis Found.")
                      else:
                              diagnosis3_label    = ttk.Label(my_frame2,text=doc_out[0][0],font=("Segoe UI", 12, "bold"),style="dashdatalabels.TLabel").grid(row=2,column=1)
                              documents_label     = ttk.Label(my_frame2,text=doc_out[0][2],font=("Segoe UI", 12, "bold"),style="dashdatalabels.TLabel").grid(row=2,column=3)
                      

                      #BOOK APPOINTMENT PAGE
                      conn= sqlite3.connect('APTT.db')
                      c= conn.cursor()
                      c.execute("""CREATE TABLE IF NOT EXISTS APTT(ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                USERNAME TEXT NOT NULL,
                                DEPARTMENT TEXT NOT NULL,
                                DOCTORNAME TEXT NOT NULL,
                                DATE TEXT NOT NULL,
                                DESCRIPTION TEXT NOT NULL)""")
                      
                      conn.commit()
                      conn.close()
                      # FETCH ALL INFO FROM OPD2 DB --> USING USERNAME
                      # USE THIS USERNAME TO FETCH BOOKED APPOINTMENTS 
                                              
                      style.configure("apttlabels.TLabel",
                      foreground="black",
                      background="white")
                      style.configure("apttbuttons.TButton",
                      foreground="black",
                      background="white")
                      global date_entry
                      start_date = date(2026, 1, 15) 
                      date_entry = ttk.DateEntry(my_frame3,dateformat='%Y-%m-%d',firstweekday=0,
                      startdate=start_date,bootstyle=PRIMARY)
                      date_entry.grid(row=2,column=2)
                      aptt_user = ttk.Label(my_frame3,text="Patient Username",font=("Segoe UI", 18, "bold")).grid(row=1,column=1)
                      aptt_user_entry = ttk.Entry(my_frame3,width=30)
                      aptt_user_entry.grid(row=1,column=2)
                      
                      def verify_user():
                              conn = sqlite3.connect('OPD2.db')
                              c=conn.cursor()
                              c.execute("""SELECT * FROM OPD2""")
                              usernames = c.fetchall()
                              conn.commit()
                              conn.close()

                              
                              #print(usernames)
                              # VERIFY AND FETCH DESIRED USERNAME FROM EVERY USERNAME USING FOR LOOP
                              def book_aptt():
                                        
                                        conn= sqlite3.connect('APTT.db')
                                        c= conn.cursor()
                                        # NO NEED TO USE FOR LOOP TO SEARCH FOR MATCHES--> SQL ONLY FETCHES MATCHING RESULTS...
                                        c.execute("SELECT * FROM APTT WHERE USERNAME = ?",(aptt_user_entry.get(),))
                                        user_book = c.fetchone()
                                        #print(user_check)
                                        conn.commit()
                                        conn.close()
                                        
                                        if user_book is None:
                                               
                                               conn= sqlite3.connect('APTT.db')
                                               c=conn.cursor()
                                               c.execute("""INSERT INTO APTT(USERNAME,DEPARTMENT,DOCTORNAME,DATE,DESCRIPTION) VALUES (?,?,?,?,?)""",
                                                          (aptt_user_entry.get(),selected_value.get(),NONE,date_entry.entry.get(),desc_entry.get()))
                                               conn.commit()
                                               conn.close()
                                               messagebox.showinfo("Appts sys","Appointment booked successfully!")        
                                         # FIX-->ELIF SHOULD HAVE LOOP TO CHECK THRU ALL EXISTING USERS
                                         # FIX-->NORMAL USER HAS ADMIN PRIVILEG

                                         # CREATE COMMANDS FOR DROPDOWN MENU WHICH STORES DEPT NAME IN A VARIABLE WHEN EXECUTED-->DEF
                                        elif user_book[1]==aptt_user_entry.get():
                                                messagebox.showinfo("Appts sys","Appointment Already booked!")

                              for users in usernames:
                                      if aptt_user_entry.get() in users:
                                              messagebox.showinfo("Verify","Verification Successful!")
                                              #COMMAND TO BE ADDED IN book_butt TO ADD APPOINTMENTS WITH PAT_DATA INTO APTT TABLE                
                                              book_butt = ttk.Button(my_frame3,text="Book",command=book_aptt,bootstyle=DANGER).grid(row=5,column=3)
                                              break
                              else:
                                       messagebox.showerror("Verify","Invalid Username!")
                                          
                      
                      aptt_user_verify = ttk.Button(my_frame3,text="Verify",command=verify_user).grid(row=1,column=3)
                      date_label = ttk.Label(my_frame3,text="Choose Date",font=("Segoe UI", 18, "bold")).grid(row=2,column=1)
                              
                      date_label = ttk.Label(my_frame3,text="Description(if any)",font=("Segoe UI", 18, "bold")).grid(row=4,column=1)
                      desc_entry = ttk.Entry(my_frame3,width=30)
                      desc_entry.grid(row=4,column=2)
                      def show_date():
                              
                              show_date = ttk.Label(my_frame3,text=date_entry.entry.get(),font=("Segoe UI", 18, "bold")).grid(row=2,column=3)

                              # INSERT DATE INTO DB-- date_entry.get() 
                      show_chosen_date = ttk.Button(my_frame3,text="Get Date",command=show_date).grid(row=2,column=3)
                      select_dept_label = ttk.Label(my_frame3,text="Choose Department",font=("Segoe UI", 18, "bold")).grid(row=3,column=1)
                      dept_menu = ttk.Menubutton(my_frame3, text="Select")
                      
                      selected_value = ttk.StringVar(value="None")
                      menu = Menu(dept_menu,tearoff=0)
                      dept_menu.config(menu=menu)
                      for option in ["Orthopaedics","Opthalmology","General medicine","Gastroenterology"]:
                              menu.add_radiobutton(label=option,variable=selected_value,value=option)
                      dept_menu.grid(row=3,column=2)
                      # WRITE A COMMAND FOR MNUBTN --> INSERT DEPARTMENT AND USERNAME INTO APTT DB
                      #CHECK FOR EXISTING APTT IN APTT.DB FOR SAME USER BEFORE INSERTING NEW APTT
                      dept_menu.config(menu=menu)
                      def logout():
                              pat_dash.destroy()
                      logout_label =ttk.Label(my_frame6,      text="Log off your Account>",font=("Segoe UI", 24)).grid(row=3,column=1,columnspan=3) 
                      logout_button = ttk.Button(my_frame6,text="LOG OUT",bootstyle=DANGER,command=logout).grid(column=5,row=3,ipadx=7)
              else:
                      messagebox.showerror("Login attempt","Invalid Username or Password!")
                      
        elif user.get()>3:
                
                messagebox.showinfo("Login attempt","Select User Type!")


user = IntVar() 
                
#-----------changing bg and text colour of labels----------
style= ttk.Style()
style.configure("CustomLabel.TLabel",
                foreground="white",
                background="black",
                font=("Segoe UI", 24, "bold"))   # background color
#dont use--> "Custom.label" or Custom.text--> both internal commands--> conflict.
#-----------enter username---------------
text2=ttk.Label(root, text="Username",font=("Arial","14"),style="CustomLabel.TLabel")     
text2.grid(column=1,row=2)


e=ttk.Entry(root,width=30,bootstyle=PRIMARY)                        
e.grid(column=2,row=2)
#temporary insertion of username and pass--> quick opening

e.insert(0,'Doomall')
#-------enter password------------
text3=ttk.Label(root, text="Password",font=("Arial","14"),style="CustomLabel.TLabel")     
text3.grid(column=1,row=3,ipadx=2)

f=ttk.Entry(root,width=30,bootstyle=PRIMARY)                             
f.grid(column=2,row=3)

#temporary insertion of username and pass--> quick opening
f.insert(0,'abcx')


# Place radio buttons inside role_frame instead of root
rb1 = ttk.Radiobutton(root, text="Patient", variable=user, value="1")
rb1.grid(column=1,row=4,ipadx=27,ipady=5)

rb2 = ttk.Radiobutton(root, text="Medical Staff", variable=user, value="2")
rb2.grid(column=2,row=4,ipadx=11,ipady=5)

rb3 = ttk.Radiobutton(root, text="Administrator", variable=user, value="3")
rb3.grid(column=3,row=4,ipadx=9,ipady=5)

#select_user = ttk.Button(root, text="select",bootstyle=INFO, command=lambda: clicked(user.get()))     #lambda command-->controls commands involving numbers-->, command=lambda: clicked(user.get())
#select_user.grid(column=4,row=3,ipadx=5)

button_login=ttk.Button(root,text="LOGIN",command=lambda: Login(),style="signupbuttons.TButton")    
#BOOTSTYLE= SUCCESS IS A CONSTANT SO (from ttkbootstrap.constants import *)
button_login.grid(column=4,row=6,ipadx=15,ipady=8)

#res_user = ttk.Label(root,textvariable=user)
#res_user.grid(column=4,row=3)

sign_up_button = ttk.Button(root,text="Register Patient",bootstyle=WARNING,command=sign_up_patient).grid(column=4,row=0,ipadx=15,ipady=5)
sign_up_button2 = ttk.Button(root,text="Register Staff",bootstyle=INFO,command=sign_up_staff).grid(column=3,row=0,ipadx=15,ipady=5)

root.mainloop()