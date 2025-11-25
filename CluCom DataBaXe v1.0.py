from tkinter import *

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import ImageTk,Image
from tkinter import messagebox

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
def check():
       if e.get()=="rishav":
              if f.get()=="abcx":
                     res = messagebox.askyesno(message="username and password found! login?")
                     if res=="True":
                            top = Toplevel()
                     if res=="False":
                            messagebox.showerror(message="username and password not found!")
              else:
                      messagebox.showerror(message="invalid password!")
       else:
                     messagebox.showerror(message="invalid username!")
#-----------changing bg and text colour of labels----------
style= ttk.Style()
style.configure("CustomLabel.TLabel",
                foreground="white",
                background="teal")   # background color
#dont use--> "Custom.label" or Custom.text--> both internal commands--> conflict.
#-----------enter username---------------
text2=ttk.Label(root, text="Enter Username",font=("Arial","14"),style="CustomLabel.TLabel")     
text2.grid(column=1,row=1)


e=ttk.Entry(root,width=30,bootstyle=INFO)                        
e.grid(column=2,row=1)

#-------enter password------------
text3=ttk.Label(root, text="Enter Password",font=("Arial","14"),style="CustomLabel.TLabel")     
text3.grid(column=1,row=2)



f=ttk.Entry(root,width=30,bootstyle=INFO)                             
f.grid(column=2,row=2)

#text1=ttk.Label(root,text="Login",font=("Arial","14"),style="CustomLabel.TLabel")
#text1.grid(column=1,row=3)



b1=ttk.Button(root,text="Login>",command=check,bootstyle=INFO)    
#BOOTSTYLE= SUCCESS IS A CONSTANT SO (from ttkbootstrap.constants import *)
b1.grid(column=4,row=3)


root.geometry("720x440")
root.mainloop()