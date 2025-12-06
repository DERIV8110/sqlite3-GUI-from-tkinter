from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import io
import threading

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

root.title("CluCom DataBaXe")
root.iconbitmap('C:/python images/vapidTech.ico')
#-------checking password----------
#------checking username---------


def sign_up():
        
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

               print(user_check)

               conn.commit()
               conn.close()
               
               if user_check is None:
                      

                      
                      conn= sqlite3.connect('OPD2.db')
                      c=conn.cursor()
                      c.execute("""INSERT INTO OPD2(Photo,Name,Username,Password,Age,Gender,Address,Phone,Email,Medical,Doctor,Department,Diagnosis) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                 (blob,name_entry.get(),username_entry.get(),password_entry.get(),age_entry.get(),gender_entry.get(),address_entry.get(),phone_entry.get(),email_entry.get(),NONE,NONE,NONE,NONE))
                      
                      conn.commit()
                      conn.close() 

               elif user_check[3]==username_entry.get():
                       messagebox.showinfo("Signup attempt","Username taken!")

        #photo_entry=ttk.Entry(signup_win,width=30)  # <-- DEF UPLOAD COMMAND AND ADD OPEN FILEMANAGER MODULE HERE
        #photo_entry.grid(row=1,column=2)

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

        medical_file_entry=ttk.Entry(signup_win,width=30)  # # <-- DEF UPLOAD COMMAND AND ADD OPEN FILEMANAGER MODULE HERE
        medical_file_entry.grid(row=10,column=2)
        medical_file_entry.insert(0,"Describe your medical history here or \nupload photo of prescription.")
       
        #create text box labels
               
        
                    
                      #conn= sqlite3.connect('OPD2.db')
                      #c=conn.cursor()
                      #c.execute("INSERT INTO OPD2 (Photo,Username) VALUES (?,?)",
                      #           (convert_to_binary(photo_store),username_entry.get()))
                      #
                      #conn.commit()
                      #conn.close() 
        photo_label          =ttk.Label(signup_win,                   text='Upload Photo',style="signuplabels.TLabel",font=("Arial","14")).grid(row=1,column=1)
        def convert_to_binary(img):       
                             with open(img,"rb") as file:
                                     data = file.read()
                             return data
        
        def open_file_manager():
                img = filedialog.askopenfilename(initialdir="C:/python images",title="Upload Photo",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
                if img:
                        global blob
                        blob = convert_to_binary(img)
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
        medical_history_upload = ttk.Button(signup_win,                     text="Upload",bootstyle=PRIMARY).grid(row=10,column=3)   # <-- GIVE COMMAND AND DEF HERE
        submit_button=         ttk.Button(signup_win,text="Submit",        command=submit,style="signupbuttons.TButton").grid(row=11,column=3,ipadx=10,ipady=5)



        ##define show db function
        #def shw_all():
        #       conn= sqlite3.connect('OPD.db')
        #
        #       c= conn.cursor()
        #
        #       c.execute("SELECT *,oid FROM OPD")
        #       recs= c.fetchall()
        #
        #       #recs[i]--> fetches data at index i specified
        #       #to print all data in gui-->make loop with index
        #       print_recs = ''
        #       for records in recs:
        #              print_recs += str(records) + "\n"
        #       
        #       #to print a function--> don't use double inverted commas
        #       mlabel= Label(signup_win,text=print_recs)
        #       mlabel.grid(row=9,columnspan=2)
        #       conn.commit()
        #
        #       conn.close()
        #
        #def shw_speci():
        #       
        #       conn= sqlite3.connect('intro.db')
        #
        #       c= conn.cursor()
        #
        #       c.execute("SELECT *,oid FROM OPD WHERE oid=?",(idx.get()))
        #       recs2= c.fetchone()
        #       
        #       mlabel2= Label(signup_win,text=recs2)
        #       mlabel2.grid(row=9,columnspan=2)
        #       conn.commit()
        #
        #       conn.close()
        ##define delete function
        #def delete():
        #       conn= sqlite3.connect('OPD.db')
        #
        #       c= conn.cursor()
        ##Delete the record from table intro where the internal unique ID (oid) matches the value entered by the user
        #       c.execute("DELETE FROM OPD WHERE oid=?",(idx.get()))
        #
        #       conn.commit()
        #
        #       conn.close()
        ##define update function from index/ primary key
        #def updt():
        #       conn= sqlite3.connect('OPD.db')
        #
        #       c= conn.cursor()
        #
        #       c.execute("""
        #    UPDATE OPD
        #    SET name = :name,
        #        address = :address,
        #        phone = :phone
        #        WHERE oid = :oid
        #    """,
        #    {
        #        'name': name_edit.get(),
        #        'address': address_edit.get(),
        #        'phone': phone_edit.get(),
        #        'oid': idx.get()
        #    })
        #
        #       conn.commit()
        #
        #       conn.close()
        #
        #
        #shw_notall= Button(signup_win,text="show not all",command=shw_speci).grid(row=7,columnspan=2)
        #up_btn=     Button(signup_win,text="update record",command=updt).grid(row=8,columnspan=2)
        #del_btn=    Button(signup_win,text="delete record",command=delete).grid(row=6,columnspan=2)
        #shw_btn=    Button(signup_win,text="show all",command=shw_all).grid(row=5,columnspan=2)
        #
        #
        #conn.commit()
        #
        #conn.close()


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
                      
                      #OPEN PATIENT TAB (FOR NOW IS ADMIN TAB)

                      new_win = Toplevel()
                      frame = ttk.Frame(new_win)
                      frame.grid(row=0, column=0)

                      new_win.geometry("1000x480")

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
                                conn= sqlite3.connect('OPD2.db')
                                c= conn.cursor()
                      
                                #c.execute("""CREATE TABLE IF NOT EXISTS patients(
                                #  username TEXT,
                                #  password TEXT
                                #)""")
                                c.execute("PRAGMA table_info(OPD2)")
                                columns_info = c.fetchall()
                                #col[1]--> selects all 2nd columns-->column names from entries table
                                col_names = [col[1] for col in columns_info]       
                                c.execute("SELECT * FROM OPD2")
                                entries = c.fetchall()
                      
                                tree = ttk.Treeview(new_win,columns=col_names,show="headings",bootstyle=INFO)
                                for colm in col_names:
                                       #for colm in col_names--> extracts all column names by help of [col[1] for col in columns_info] one by one
                                       tree.heading(colm, text=colm)
                                       #makes columns based on number of columns retreived using [col[1] for col in columns_info]-->headings
                                       tree.column(colm,width=60,anchor="center")
                                for row in entries:
                                       #inserts rows from db to treeview ""-->(start) to tk.END--> values=rows of db one by one
                                       tree.insert("", "end", values=row)
                                tree.grid(row=4,column=1,columnspan=6,sticky="nsew")
                                conn.commit()
                                conn.close()

                      def delete_specific():
                                conn= sqlite3.connect('OPD2.db')
                                c= conn.cursor()
                                #Delete the record from table intro where the internal unique ID (oid) matches the value entered by the user
                                c.execute("DELETE FROM OPD2 WHERE id=?",(id_no.get()))
                         
                                conn.commit()
                                conn.close()        
                      
                      id_no_label = ttk.Label(new_win,text="ID>")
                      id_no_label.grid(column=1,row=0)
                      
                      id_no = ttk.Entry(new_win,width=30)
                      id_no.grid(column=2,row=0)
                      
                      
                      button_show_all= ttk.Button(new_win,text="Show All",command=show)
                      button_show_all.grid(column=7,row=2)
                      
                      button_delete = ttk.Button(new_win,text="Delete",command=delete_specific)
                      button_delete.grid(column=7,row=3,ipadx=7)
                      
              else:
                      messagebox.showerror("Login attempt","Invalid Username or Password!")
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
                      frame = ttk.Frame(pat_dash)
                      frame.grid(row=0, column=0)
                      
                      pat_dash.geometry("1000x480")
                      my_img2 =ImageTk.PhotoImage(Image.open("C:/python images/dash.jpg"))
                      background_label2 = ttk.Label(pat_dash, image=my_img2)
                      background_label2.image = my_img2   # <-- attach reference to the widget
                      background_label2.place(x=0, y=0)
                      
                      style.configure("dashlabels.TLabel",
                      foreground="white",
                      background="black")
                      
                      style.configure("dashdatalabels.TLabel",
                      foreground="white",
                      background="black")
                      # root.grid_rowconfigure(row number, weight=rows to occupy)
                      pat_dash.grid_rowconfigure(0, weight=1)
                      pat_dash.grid_rowconfigure(1, weight=1)
                      pat_dash.grid_rowconfigure(2, weight=1)
                      pat_dash.grid_rowconfigure(3, weight=1)
                      pat_dash.grid_rowconfigure(4, weight=1)
                      pat_dash.grid_rowconfigure(5, weight=1)
                      pat_dash.grid_rowconfigure(6, weight=1)
                      pat_dash.grid_rowconfigure(7, weight=1)
                      # root.grid_columnconfigure(column number, weight=rows to occupy)
                      
                      pat_dash.grid_columnconfigure(0, weight=2)
                      pat_dash.grid_columnconfigure(1, weight=1)
                      pat_dash.grid_columnconfigure(2, weight=1)
                      pat_dash.grid_columnconfigure(3, weight=1)
                      pat_dash.grid_columnconfigure(4, weight=1)
                      pat_dash.grid_columnconfigure(5, weight=2)

                      
                      def show_db():
                                conn= sqlite3.connect('OPD2.db')
                                c= conn.cursor()
                      
                                #c.execute("""CREATE TABLE IF NOT EXISTS patients(
                                #  username TEXT,
                                #  password TEXT
                                #)""")
                                c.execute("PRAGMA table_info(OPD2)")
                                columns_info = c.fetchall()
                                #print(columns_info)
                                #col[1]--> selects all 2nd columns-->column names from entries table
                                col_names = [col[1] for col in columns_info] 
                                #print(col_names)      
                                c.execute("SELECT ID,Photo,Name,Age,Gender,Address,Phone,Email,Medical,Doctor,Department,Diagnosis FROM OPD2 WHERE Username = ?",(e.get(),))
                                entries = c.fetchall()
                                #print(entries)
                                binary_to_img = entries[0][1]
                                def convert_to_image(binary_to_img):       
                                      with io.BytesIO(binary_to_img) as file_like:
                                        converted = Image.open(file_like).convert("RGBA")
                                      return converted
                                blob_2 = convert_to_image(binary_to_img)
                                img_reference = ImageTk.PhotoImage(blob_2)
                                pat_img = ttk.Label(pat_dash, image=img_reference)
                                pat_img.image = img_reference  # <-- attach reference to the widget
                                pat_img.place(x=2, y=2)


                                ID_label = ttk.Label(pat_dash,text="ID",                font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=1,column=1)
                                photo_label = ttk.Label(pat_dash,text="Photo",          font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=1,column=2)
                                name_label = ttk.Label(pat_dash,text="Name",            font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=1,column=3)
                                age_label = ttk.Label(pat_dash,text="Age",              font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=1,column=4)
                                gender_label = ttk.Label(pat_dash,text="Gender",        font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=3,column=1)
                                address_label = ttk.Label(pat_dash,text="Address",      font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=3,column=2)
                                phone_label = ttk.Label(pat_dash,text="Phone",          font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=3,column=3)
                                email_label = ttk.Label(pat_dash,text="Email",          font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=3,column=4)
                                medical_label = ttk.Label(pat_dash,text="History",      font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=5,column=1)
                                doctor_label = ttk.Label(pat_dash,text="Doctor Name",   font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=5,column=2)
                                department_label = ttk.Label(pat_dash,text="Department",font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=5,column=3)
                                diagnosis_label = ttk.Label(pat_dash,text="Diagnosis",  font=("Segoe UI", 20, "bold"),style="dashlabels.TLabel").grid(row=5,column=4)
                                # DATA INPUT BELOW
                                ID2_label = ttk.Label(pat_dash,        text=entries[0][0],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=2,column=1)

                                #photo2_label = ttk.Label(pat_dash,image=img_reference).grid(row=2,column=2)

                                name2_label = ttk.Label(pat_dash,       text=entries[0][2],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=2,column=3)
                                age2_label = ttk.Label(pat_dash,        text=entries[0][3],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=2,column=4)
                                gender2_label = ttk.Label(pat_dash,     text=entries[0][4],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=4,column=1)
                                address2_label = ttk.Label(pat_dash,    text=entries[0][5],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=4,column=2)
                                phone2_label = ttk.Label(pat_dash,      text=entries[0][6],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=4,column=3)
                                email2_label = ttk.Label(pat_dash,      text=entries[0][7],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=4,column=4)
                                medical2_label = ttk.Label(pat_dash,    text=entries[0][8],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=6,column=1)
                                doctor2_label = ttk.Label(pat_dash,     text=entries[0][8],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=6,column=2)
                                departmen2t_label = ttk.Label(pat_dash,text=entries[0][10],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=6,column=3)
                                diagnosis2_label = ttk.Label(pat_dash, text=entries[0][11],font=("Segoe UI", 18),style="dashdatalabels.TLabel").grid(row=6,column=4)


                                #tree = ttk.Treeview(pat_dash,columns=col_names,show="headings",bootstyle=PRIMARY)
                                #for colm in col_names:
                                #       #for colm in col_names--> extracts all column names by help of [col[1] for col in columns_info] one by one
                                #       tree.heading(colm, text=colm)
                                #       #makes columns based on number of columns retreived using [col[1] for col in columns_info]-->headings
                                #       tree.column(colm,width=60,anchor="center")
                                #for row in entries:
                                #       #inserts rows from db to treeview ""-->(start) to tk.END--> values=rows of db one by one
                                #       tree.insert("", "end", values=row)
                                #tree.grid(row=1,column=2,columnspan=6,sticky="nsew")
                                conn.commit()
                                conn.close()
                      
                      dashboard_button    = ttk.Button(pat_dash,text="Dashboard"  ,bootstyle=PRIMARY,command=show_db).grid(column=0,row=1,ipadx=7)

                      appointment_button  = ttk.Button(pat_dash,text="Appointment",bootstyle=PRIMARY).grid(column=0,row=2)
                      # BELOW PAGES TO BE DESIGNED LATER
                      document_button  = ttk.Button(pat_dash,text="Dashboard",bootstyle=PRIMARY).grid(column=0,row=3,ipadx=7) 
                      
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

e.insert(0,'adi6')
#-------enter password------------
text3=ttk.Label(root, text="Password",font=("Arial","14"),style="CustomLabel.TLabel")     
text3.grid(column=1,row=3,ipadx=2)

f=ttk.Entry(root,width=30,bootstyle=PRIMARY)                             
f.grid(column=2,row=3)

#temporary insertion of username and pass--> quick opening
f.insert(0,'wxww')


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

sign_up_button = ttk.Button(root,text="SignUp",bootstyle=WARNING,command=sign_up)
sign_up_button.grid(column=4,row=0,ipadx=15,ipady=5)


root.mainloop()