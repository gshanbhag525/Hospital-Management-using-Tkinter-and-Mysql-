import tkinter
from tkinter import *
from window2 import menu
import db.db
from tkinter import messagebox, Button
from PIL import ImageTk, Image

global username,userbox,login,passbox,password
'''
root=None
userbox=None
passbox=None
copy_of_image=None
label=None
login= None

#command for login button
def GET():
    global userbox,passbox,error
    S1 = userbox.get()
    S2 = passbox.get()
    data = (
        S1,S2
    )
    if S1 == "":
        messagebox.showinfo("Alert!", "Enter USERNAME First")
    elif S2 == "":
        messagebox.showinfo("Alert!", "Enter Password first")
    else:
        res = db.db.user_login(data)
        if res:
            root.destroy()
            menu()
        else:
            messagebox.showinfo("Alert!", "Wrong username/password")

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

root = Tk()
root.title("Title")
root.configure(background='black')
root.geometry('1920x1080')

frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open("images/hospital.jpeg")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

center_frame = Frame(frame, relief='raised', borderwidth=2)
center_frame.place(relx=0.5, rely=0.5, anchor=S)

username = Label(center_frame, text="USERNAME", width=18, font="helvetica 19 bold")
username.pack()

userbox = Entry(center_frame,  width=16)
userbox.pack()

password = Label(center_frame, text="Password", width=20, font="helvetica 19 bold")
password.pack()

passbox = Entry(center_frame, show="*",  width=16)
passbox.pack()

login = Button(center_frame, text="LOGIN", command=GET, font="helvetica 19 bold")
login.pack()

root.mainloop()
'''
menu()