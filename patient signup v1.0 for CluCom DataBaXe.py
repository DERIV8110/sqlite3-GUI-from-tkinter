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

conn= sqlite3.connect('patient.db')
c=conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS patient(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)""")

def insert():
        conn= sqlite3.connect('patient.db')
        c=conn.cursor()

        c.execute("INSERT INTO patient(username, password) VALUES (?,?)", (username.get(),password.get()))
        username.delete(0,END)
        password.delete(0,END)

        conn.commit()
        conn.close()
        
def show():
          conn= sqlite3.connect('patient.db')
          c= conn.cursor()

          #c.execute("""CREATE TABLE IF NOT EXISTS patients(
          #  username TEXT,
          #  password TEXT
          #)""")
          c.execute("PRAGMA table_info(patient)")
          columns_info = c.fetchall()
          #col[1]--> selects all 2nd columns-->column names from entries table
          col_names = [col[1] for col in columns_info]       
          c.execute("SELECT * FROM patient")
          entries = c.fetchall()

          tree = ttk.Treeview(root,columns=col_names,show="headings")
          for colm in col_names:
                 #for colm in col_names--> extracts all column names by help of [col[1] for col in columns_info] one by one
                 tree.heading(colm, text=colm)
                 #makes columns based on number of columns retreived using [col[1] for col in columns_info]-->headings
                 tree.column(colm,width=60,anchor="center")
          for row in entries:
                 #inserts rows from db to treeview ""-->(start) to tk.END--> values=rows of db one by one
                 tree.insert("", tk.END, values=row)
          tree.grid(row=3,columnspan=3,sticky="nsew")
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

conn.commit()
conn.close()

root.geometry("720x480")
root.mainloop()
