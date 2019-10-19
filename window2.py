from tkinter import *
from tkinter import messagebox
import db.db
from prescibe import prescribe
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from RooMT import Room_all
from BILLING import BILLING
from employee_reg import emp_screen
from patient_reg import pat_screen
from appointment import appo
# from drug import drug
from PIL import ImageTk, Image
from drugdetails import drug

global label,copy_of_image
#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_contact=None
pat_CT=None
label = None
copy_of_image = None


rootp

#EXIT for MENU
def ex():
    global root1
    root1.destroy()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4
    global m, label,copy_of_image,button5,button6,button7, button8

    root1 = Tk()
    root1.geometry("1920x1080")
    root1.title("MAIN MENU")

    frame = Frame(root1 , relief='raised', borderwidth=2)
    frame.pack(fill=BOTH, expand=YES)
    frame.pack_propagate(False)

    copy_of_image = Image.open("images/hospital.jpeg")
    photo = ImageTk.PhotoImage(copy_of_image)

    label = Label(frame, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    center_frame = Frame(rootp, relief='raised', borderwidth=2)
    # center_frame.pack(fill=None, expand=True)
    center_frame.place(relx=0.5, rely=0.7, anchor=S)

    m = Label(center_frame, text="MENU", font='Helvetica 40 bold',
              fg='BLACK', bg='GREY')

    button1 = Button(center_frame,text="PATIENT REGISTRATION",
                     font='Helvetica 20 bold ',bg='BLUE',fg='BLACK', command=pat_screen)
    # button2 = Button(root1, text="ROOM ALLOCATION",bg='light green',fg='black',command=Room_all)
    button3 = Button(center_frame, text="DOCTOR REGISTRATION",
                     font='Helvetica 20 bold ',bg='light blue',fg='black',command=emp_screen)
    button4 = Button(center_frame, text="BOOK APPOINTMENT",
                     font='Helvetica 20 bold ',bg='light green',fg='black',command=appo)
    button5 = Button(center_frame, text="PATIENT BILL",
                     font='Helvetica 20 bold ',bg='light green',fg='black',command=BILLING)
    button7 = Button(center_frame, text="DRUG REGISTRATION",
                     font='Helvetica 20 bold ',command=drug,bg='light blue',fg='black')
    button8 = Button(center_frame, text="PATIENT PRESCRIBE",
                     font='Helvetica 20 bold ', bg='light green', fg='black', command=prescribe)
    button6 = Button(center_frame, text="EXIT",
                     font='Helvetica 20 bold ', bg='red', fg='black', command=ex)

    # m.place(x=75,y=5)
    m.pack(padx=10, pady=20)

    button1.pack(side=TOP, padx=10, pady=20)
    # button1.place(x=80,y=50)

    button3.pack(side=TOP, padx=10, pady=20)
    # button3.place(x=80,y=100)

    button7.pack(side=TOP, padx=10, pady=20)
    # button7.place(x=80,y=150)

    button4.pack(side=TOP, padx=10, pady=20)
    # button4.place(x=80, y=200)

    button8.pack(side=TOP, padx=10, pady=20)
    # button8.place(x=80,y=250)

    button5.pack(side=TOP, padx=10, pady=20)
    # button5.place(x=80,y=300)

    button6.pack(side=TOP, padx=10, pady=20)
    # button6.place(x=80,y=350)

    root1.mainloop()



