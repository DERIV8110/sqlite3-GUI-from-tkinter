#conn= sqlite3.connect('intro.db'),c= conn.cursor(),conn.commit(),conn.close()
#should be written in every new area of code i.e. def,if, else etc

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()                                            #you can change root variable to anything
root.title("Vapid DB v1.1")
root.iconbitmap('C:/python images/vapidTechLOGO.ico')
root.geometry("300x300")

conn= sqlite3.connect('intro.db')

c= conn.cursor()                                     #cursor --> commits changes
                                                     #call cursor for any task in db

#cursor--> makes new table
c.execute("""CREATE TABLE IF NOT EXISTS intro(
          name TEXT,
          address TEXT,
          phone INTEGER
          
          )""")

#create entry boxes

name_edit=Entry(root,width=30).grid(row=0,column=1)
address_edit=Entry(root,width=30).grid(row=1,column=1)
phone_edit=Entry(root,width=30).grid(row=2,column=1)

#create text box labels

name_labels=Label(root,text='enter name').grid(row=0,column=0)
address_labels=Label(root,text='enter address').grid(row=1,column=0)
phone_labels=Label(root,text='enter phone').grid(row=2,column=0)
# define submit below
#delete pre-existing records before INSERTING.
def submit():
       conn= sqlite3.connect('intro.db')

       c= conn.cursor()

       c.execute("INSERT INTO intro VALUES(:name,:address,:phone)",
                 {"name":name_edit.get(),
                  "address":address_edit.get(),
                  "phone":phone_edit.get()
                  })

       conn.commit()

       conn.close()
       #delete pre-existing records before INSERTING.
       #delete syntax--> f_name.delete(start index,end index)
       name.delete(0,END)
       address.delete(0,END)
       phone.delete(0,END)


#submit button--> making button adds command to it--> define command above
sub_butt= Button(root,text="submit",command=submit).grid(row=3,columnspan=2)
#cursor connects to db-->commit changes
conn.commit()
#cursor closes connection to db
conn.close()
root.mainloop()