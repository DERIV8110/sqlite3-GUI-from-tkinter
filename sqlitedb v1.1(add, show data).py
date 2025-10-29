#conn= sqlite3.connect('intro.db'),c= conn.cursor(),conn.commit(),conn.close()
#should be written in every new area of code i.e. def,if, else etc
#don't put .grid/ .pack with the variable itself--> always write in next line

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()                                            #you can change root (variable) to anything
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

name_edit=Entry(root,width=30)
name_edit.grid(row=0,column=1)
address_edit=Entry(root,width=30)
address_edit.grid(row=1,column=1)
phone_edit=Entry(root,width=30)
phone_edit.grid(row=2,column=1)

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
       name_edit.delete(0,END)
       address_edit.delete(0,END)
       phone_edit.delete(0,END)

#define show db function
def shw():
       conn= sqlite3.connect('intro.db')

       c= conn.cursor()

       c.execute("SELECT * FROM intro")
       recs= c.fetchall()

       #recs[i]--> fetches data at index i specified
       #to print all data in gui-->make loop with index
       print_recs = ''
       for records in recs:
              print_recs += str(records) + "\n"
       
       #to print a function--> don't use double inverted commas
       mlabel= Label(root,text=print_recs)
       mlabel.grid(row=5,columnspan=2)
       conn.commit()

       conn.close()


#show button--> shows items stored in db
shw_btn= Button(root,text="show items in database",command=shw).grid(row=4,columnspan=2)
#submit button--> making button adds command to it--> define command above
sub_butt= Button(root,text="submit",command=submit).grid(row=3,columnspan=2)
#cursor connects to db-->commit changes
conn.commit()
#cursor closes connection to db
conn.close()
root.mainloop()