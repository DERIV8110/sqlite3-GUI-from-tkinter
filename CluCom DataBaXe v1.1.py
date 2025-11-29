from tkinter import *

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import ImageTk,Image
from tkinter import messagebox

import sqlite3

root= Tk()
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

my_img1 =ImageTk.PhotoImage(Image.open("C:/python images/login2.jpg"))
background_label = ttk.Label(root, image=my_img1)
background_label.place(x=0, y=0)
#above line--> places background without widget distortion using frame in tkinter.

# root.grid_rowconfigure(row number, weight=rows to occupy)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
# root.grid_columnconfigure(column number, weight=rows to occupy)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=2)
root.grid_columnconfigure(4, weight=2)

root.title("CluCom DataBaXe")
root.iconbitmap('C:/python images/vapidTech.ico')
#-------checking password----------
#------checking username---------
user = StringVar() 
user.set("Patient")

def clicked():
        global user
        if user.get()==1 or "Patient":
              
              conn= sqlite3.connect('OPD.db')
              c= conn.cursor()
              c.execute("SELECT Username FROM OPD WHERE Username = ?",(e.get(),))
              user_fetch = c.fetchone()
              conn.commit()
              conn.close()
              #c.fetchone()-->returns tuple-->use index to get string value of username

              if user_fetch[0]==e.get():
                      
                      #OPEN PATIENT TAB

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
                      
                      conn= sqlite3.connect('OPD.db')
                      c=conn.cursor()
                      
                      c.execute("""CREATE TABLE IF NOT EXISTS OPD(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                          Username TEXT NOT NULL,
                          Password TEXT NOT NULL
                      )""")
                      
                      def insert():
                              conn= sqlite3.connect('OPD.db')
                              c=conn.cursor()
                      
                              c.execute("INSERT INTO OPD(Username, Password) VALUES (?,?)", (username.get(),password.get()))
                              username.delete(0,END)
                              password.delete(0,END)
                      
                              conn.commit()
                              conn.close()
                              
                      def show():
                                conn= sqlite3.connect('OPD.db')
                                c= conn.cursor()
                      
                                #c.execute("""CREATE TABLE IF NOT EXISTS patients(
                                #  username TEXT,
                                #  password TEXT
                                #)""")
                                c.execute("PRAGMA table_info(OPD)")
                                columns_info = c.fetchall()
                                #col[1]--> selects all 2nd columns-->column names from entries table
                                col_names = [col[1] for col in columns_info]       
                                c.execute("SELECT * FROM OPD")
                                entries = c.fetchall()
                      
                                tree = ttk.Treeview(new_win,columns=col_names,show="headings")
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
                                conn= sqlite3.connect('OPD.db')
                         
                                c= conn.cursor()
                                #Delete the record from table intro where the internal unique ID (oid) matches the value entered by the user
                                c.execute("DELETE FROM OPD WHERE id=?",(id_no.get()))
                         
                                conn.commit()
                         
                                conn.close()        
                      
                      id_no_label = ttk.Label(new_win,text="ID>")
                      id_no_label.grid(column=1,row=0)
                      
                      id_no = ttk.Entry(new_win,width=30)
                      id_no.grid(column=2,row=0)
                      
                      username_label = ttk.Label(new_win,text="Username>")
                      username_label.grid(column=3,row=0)
                      
                      username = ttk.Entry(new_win,width=30)
                      username.grid(column=4,row=0)
                      
                      password_label = ttk.Label(new_win,text="Password>")
                      password_label.grid(column=5,row=0)
                      
                      password = ttk.Entry(new_win,width=30)
                      password.grid(column=6,row=0)
                      
                      button_insert = ttk.Button(new_win,text="Insert",command=insert)
                      button_insert.grid(column=7,row=0,ipadx=9)
                      
                      button_show_all= ttk.Button(new_win,text="Show All",command=show)
                      button_show_all.grid(column=7,row=2)
                      
                      button_delete = ttk.Button(new_win,text="Delete",command=delete_specific)
                      button_delete.grid(column=7,row=3,ipadx=7)
                      
                      conn.commit()
                      conn.close()

        else:
                messagebox.askokcancel(new_win,text="Username or Password doesn't Exist") 


              #if f.get()=="abcx":
              #       
              #       messagebox.showinfo(message="username and password found!")
              #
              #       top = Toplevel()
              #       
              #       top.geometry("720x480")                                                    # .geometry --> set window size in pixels
              #       top.title("Vapid comms.")
              #       
              #       #conn= sqlite3.connect('intro.db')    c= conn.cursor()    conn.commit()   conn.close() -->should be written in every new area of code i.e. def,if, else etc
              #       
              #       #don't put .grid or .pack with the variable itself--> always write in next line
              #       
              #       
              #       conn= sqlite3.connect('intro.db')
              #       
              #       c= conn.cursor()                                     #cursor --> commits changes
              #                                                            #call cursor for any task in db
              #       
              #       #cursor--> makes new table
              #       c.execute("""CREATE TABLE IF NOT EXISTS intro(
              #                 name TEXT,
              #                 address TEXT,
              #                 phone INTEGER
              #                 )""")
              #       
              #       #create entry boxes
              #       
              #       name_edit=Entry(top,width=30)
              #       name_edit.grid(row=0,column=1)
              #       address_edit=Entry(top,width=30)
              #       address_edit.grid(row=1,column=1)
              #       phone_edit=Entry(top,width=30)
              #       phone_edit.grid(row=2,column=1)
              #
              #       #only enter index not any other fields then click delete to delete row.
              #
              #       idx=Entry(top,width=30)
              #       idx.grid(row=3,column=1)
              #
              #       #create text box labels
              #       
              #       name_labels=   Label(top,text='enter name').grid(row=0,column=0)
              #       address_labels=Label(top,text='enter address').grid(row=1,column=0)
              #       phone_labels=  Label(top,text='enter phone').grid(row=2,column=0)
              #       idx_label=     Label(top,text='index no.').grid(row=3,column=0)
              #
              #       # define submit below
              #       #delete pre-existing records before INSERTING.
              #       def submit():
              #              conn= sqlite3.connect('intro.db')
              #       
              #              c= conn.cursor()
              #                   
              #        
              #                  #     (      syntax with keys                                    ,                        values corresponding to keys                )
              #              c.execute("INSERT INTO intro VALUES(:name,:address,:phone)",{"name":name_edit.get(),"address":address_edit.get(),"phone":phone_edit.get()})
              #       
              #              conn.commit()
              #       
              #              conn.close()
              #              #delete pre-existing records before INSERTING.
              #              #delete syntax--> f_name.delete(start index,end index)
              #              name_edit.delete(0,END)
              #              address_edit.delete(0,END)
              #              phone_edit.delete(0,END)
              #       
              #       #define show db function
              #       def shw_all():
              #              conn= sqlite3.connect('intro.db')
              #       
              #              c= conn.cursor()
              #       
              #              c.execute("SELECT *,oid FROM intro")
              #              recs= c.fetchall()
              #       
              #              #recs[i]--> fetches data at index i specified
              #              #to print all data in gui-->make loop with index
              #              print_recs = ''
              #              for records in recs:
              #                     print_recs += str(records) + "\n"
              #              
              #              #to print a function--> don't use double inverted commas
              #              mlabel= Label(top,text=print_recs)
              #              mlabel.grid(row=9,columnspan=2)
              #              conn.commit()
              #       
              #              conn.close()
              #       
              #       def shw_speci():
              #              
              #              conn= sqlite3.connect('intro.db')
              #       
              #              c= conn.cursor()
              #       
              #              c.execute("SELECT *,oid FROM intro WHERE oid=?",(idx.get()))
              #              recs2= c.fetchone()
              #              
              #              mlabel2= Label(top,text=recs2)
              #              mlabel2.grid(row=9,columnspan=2)
              #              conn.commit()
              #       
              #              conn.close()
              #       #define delete function
              #       def delete():
              #              conn= sqlite3.connect('intro.db')
              #       
              #              c= conn.cursor()
              #       #Delete the record from table intro where the internal unique ID (oid) matches the value entered by the user
              #              c.execute("DELETE FROM intro WHERE oid=?",(idx.get()))
              #       
              #              conn.commit()
              #       
              #              conn.close()
              #       #define update function from index/ primary key
              #       def updt():
              #              conn= sqlite3.connect('intro.db')
              #       
              #              c= conn.cursor()
              #       
              #              c.execute("""
              #           UPDATE intro
              #           SET name = :name,
              #               address = :address,
              #               phone = :phone
              #               WHERE oid = :oid
              #           """,
              #           {
              #               'name': name_edit.get(),
              #               'address': address_edit.get(),
              #               'phone': phone_edit.get(),
              #               'oid': idx.get()
              #           })
              #       
              #              conn.commit()
              #       
              #              conn.close()
              #       
              #       #show specific record--> with the help of oid
              #       shw_notall= Button(top,text="show not all",command=shw_speci).grid(row=7,columnspan=2)
              #       #update record-->updates pre-existing record to a new one
              #       up_btn=     Button(top,text="update record",command=updt).grid(row=8,columnspan=2)
              #       #delete record--> deletes specific record
              #       del_btn=    Button(top,text="delete record",command=delete).grid(row=6,columnspan=2)
              #       #show button--> shows items stored in db
              #       shw_btn=    Button(top,text="show all",command=shw_all).grid(row=5,columnspan=2)
              #       #submit button--> making button adds command to it--> define command above
              #       sub_butt=   Button(top,text="submit new",command=submit).grid(row=4,columnspan=2)
              #       #cursor connects to db-->commit changes
              #       conn.commit()
              #       #cursor closes connection to db
              #       conn.close()
                     

              #       else:
              #               messagebox.showerror(message="invalid username or password")
              #else:
              #              messagebox.showerror(message="invalid username!")
#-----------changing bg and text colour of labels----------
style= ttk.Style()
style.configure("CustomLabel.TLabel",
                foreground="white",
                background="teal")   # background color
#dont use--> "Custom.label" or Custom.text--> both internal commands--> conflict.
#-----------enter username---------------

text2=ttk.Label(root, text="Username",font=("Arial","14"),style="CustomLabel.TLabel")     
text2.grid(column=1,row=1)


e=ttk.Entry(root,width=30,bootstyle=INFO)                        
e.grid(column=2,row=1)
#temporary insertion of username and pass--> quick opening

e.insert(0,'rishav')
#-------enter password------------
text3=ttk.Label(root, text="Password",font=("Arial","14"),style="CustomLabel.TLabel")     
text3.grid(column=1,row=2)

f=ttk.Entry(root,width=30,bootstyle=INFO)                             
f.grid(column=2,row=2)

#temporary insertion of username and pass--> quick opening
f.insert(0,'abcx')


rb1 = ttk.Radiobutton(root, text="Patient", variable=user, value="1")
rb1.grid(column=1,row=3)

rb2 = ttk.Radiobutton(root, text="Medical Staff", variable=user, value="2")
rb2.grid(column=2,row=3)

rb3 = ttk.Radiobutton(root, text="Administrator", variable=user, value="3")
rb3.grid(column=3,row=3)

#select_user = ttk.Button(root, text="select",bootstyle=INFO, command=lambda: clicked(user.get()))     #lambda command-->controls commands involving numbers-->, command=lambda: clicked(user.get())
#select_user.grid(column=4,row=3,ipadx=5)

b1=ttk.Button(root,text="Login>",command=lambda: clicked(),bootstyle=INFO)    
#BOOTSTYLE= SUCCESS IS A CONSTANT SO (from ttkbootstrap.constants import *)
b1.grid(column=4,row=4)

res_user = ttk.Label(root,textvariable=user)
res_user.grid(column=4,row=3)

root.geometry("720x440")
root.mainloop()