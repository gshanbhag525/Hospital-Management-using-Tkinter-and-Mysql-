from tkinter import *
import db.db
from tkinter import messagebox
from db.db import cursor,con
from PIL import ImageTk, Image

global label, copy_of_image, cursor
label = None
copy_of_image = None
rootE=None
var=None

def inp():
    global e1,e2,e3,e4,var
    e1=t1.get()
    e2=t2.get()
    # e3=str(var.get())
    e3=t3.get()
    e4=t4.get()
    con.connect()
    cursor.execute("INSERT INTO doctor VALUES('"+e1+"','"+e2+"','"+e3+"','"+e4+"')")
    con.commit()
    # cursor.close()
    messagebox.showinfo(" DATABASE SYSTEM", "DOCTOR DATA ADDED")

def ex():
    rootE.destroy()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    global label, copy_of_image
    rootE=Toplevel()
    rootE.title("DOCTOR registration")
    rootE.configure(background='black')
    rootE.geometry("1920x1080")
    copy_of_image = Image.open("images/hospital.jpeg")
    photo = ImageTk.PhotoImage(copy_of_image)

    label = Label(rootE, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    var = StringVar(master=rootE)
    H = Label(rootE,text="DOCTOR REGISTRATION",fg='BLACK',font="Arial 10 bold")
    H.place(x=50,y=20)

    l1=Label(rootE,text="DOCTOR ID")
    l1.place(x="50",y="50")
    t1=Entry(rootE)
    t1.place(x='170',y='50')
    l2 = Label(rootE, text="DOCTOR NAME")
    l2.place(x=50,y=80)
    t2 = Entry(rootE)
    t2.place(x='170', y='80')
    l3 = Label(rootE, text="SPECIALIZATION")
    l3.place(x=50,y=110)
    t3 = Entry(rootE)
    t3.place(x=170, y=110)
    l4 = Label(rootE, text="EXPERIENCE")
    l4.place(x=50, y=140)
    t4 = Entry(rootE)
    t4.place(x=170, y=140)

    b1=Button(rootE,text="SAVE",command=inp)
    b1.place(x=60,y=170)
    b2=Button(rootE,text="DELETE DOCTOR",command=delo)
    b2.place(x=120,y=170)
    b3=Button(rootE,text="EXIT",command=ex)
    b3.place(x=270,y=170)
    rootE.mainloop()


rootDE=None
def delo():
    global rootDE,d1
    rootDE=Tk()
    rootDE.geometry("250x250")
    rootDE.title("DOCTOR DELETION")
    h1=Label(rootDE,text="ENTER DOCTOR ID TO DELETE :")
    h1.place(x=20,y=10)
    d1=Entry(rootDE)
    d1.place(x=20,y=40)
    B1=Button(rootDE,text="DELETE",command=delling)
    B1.place(x=20,y=70)
    rootDE.mainloop()
p=None
def delling():
    global d1,de,p
    de=d1.get()
    de = str(de)
    con.connect()
    p = cursor.execute("select * from doctor where doc_id='"+de+"'")
    p = cursor.fetchone()
    if p != 0:
        cursor.execute("DELETE from doctor where doc_id='"+de+"'")
        dme = Label(rootDE, text=" DOCTOR DELETED FROM DATABASE", fg="green")
        dme.place(x=20, y=100)
        con.commit()
        # cursor.close()
        # con.close()
    else:
        error = Label(rootDE, text="DOCTOR DOESN'T EXIST", fg="Red")
        error.place(x=20, y=100)
