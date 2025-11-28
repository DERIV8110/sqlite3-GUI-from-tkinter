from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter import messagebox

import sqlite3

root = Tk()
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

# root.grid_rowconfigure(row number, weight=rows to occupy)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

# root.grid_columnconfigure(column number, weight=rows to occupy)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)



def insert():
        conn= sqlite3.connect('patient.db')
        c=conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS patients(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )""")

        c.execute("INSERT INTO patients(username, password) VALUES (?,?)", (username.get(),password.get()))
        username.delete(0,END)
        password.delete(0,END)

        conn.commit()
        conn.close()
        
def show():
          conn= sqlite3.connect('patients.db')
          c= conn.cursor()

          c.execute("""CREATE TABLE IF NOT EXISTS patients(
            username TEXT,
            password TEXT
          )""")
          c.execute("SELECT * FROM patients")
          entries = c.fetchall()

          tree= ttk.Treeview(root,columns=("ID","Username","Password"),show="headings")
          tree.heading("Username", text="Username")
          tree.heading("Password", text="Password")

          for row in entries:
            tree.insert("", tk.END, values=row)

          tree.grid(column=0,row=3)


          conn.commit()
          conn.close()
        
        
username = ttk.Entry(root,width=30)
username.grid(column=0,row=0)

password = ttk.Entry(root,width=30)
password.grid(column=1,row=0)

b6 = ttk.Button(root,text="Insert",command=insert)
b6.grid(column=2,row=0,ipadx=9)

b7 = ttk.Button(root,text="Show All",command=show)
b7.grid(column=2,row=2)

root.geometry("720x480")
root.mainloop()
