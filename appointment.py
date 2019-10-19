from tkinter import *
from db.db import cursor,con
from PIL import ImageTk, Image
from tkinter import  messagebox
rootAA=None
copy_of_image = None
label = None

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

e6=None
def set():
    global e3,e1,e4,e5,e6
    p1=e1.get()
    p3=e3.get(ACTIVE)
    p4=e4.get()
    p5=e5.get()
    con.connect()
    cursor.execute("Insert into appointment values(%s,%s,%s,%s)",(p1,p3,p4,p5))
    con.commit()
    messagebox.showinfo("DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")


def appo():
    global rootAA,L,e1,e2,e3,e4,e5,e6, copy_of_image,label
    rootAA= Toplevel()
    rootAA.geometry("1920x1080")
    rootAA.title("APPOINTMENTS")
    rootAA.configure(background='black')
    frame = Frame(rootAA, relief='raised', borderwidth=2)
    frame.pack(fill=BOTH, expand=YES)
    frame.pack_propagate(False)

    copy_of_image = Image.open("images/hospital.jpeg")
    photo = ImageTk.PhotoImage(copy_of_image)

    label = Label(frame, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    H= Label(rootAA,text="APOINTMENTS",fg="blue",font="Arial 10 bold")
    H.place(x=55,y=25)
    l1 =  Label(rootAA,text="PATIENT ID")
    l1.place(x=20,y=60)
    e1 =  Entry(rootAA)
    e1.place(x=100, y=60)
    l3 =  Label(rootAA,text="APPOINTMENT NO")
    l3.place(x=20,y=90)
    L=['1','2','3','4','5','6','7','8']
    e3= Listbox(rootAA, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert( END, jjj)
    e3.place(x=140,y=90)
    l4 =  Label(rootAA,text="APPOINTMENT TIME(HH:MM:SS)")
    l4.place(x=20,y=120)
    e4= Entry(rootAA)
    e4.place(x=20,y=145)
    l5 =  Label(rootAA,text="APPOINTMENT DATE(YYYY-MM-DD)")
    l5.place(x=20,y=170)
    e5= Entry(rootAA)
    e5.place(x=20,y=195)
    scrollbar =  Scrollbar(rootAA,orient= HORIZONTAL)
    scrollbar.place(x=235, y=90)
    e3.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=e3.yview)
    b1= Button(rootAA,text="SET APPOINTMENT",command=set)
    b1.place(x=20,y=220)
    b2= Button(rootAA,text="Delete Appointment",command=dela)
    b2.place(x=180,y=220)
    b4 = Button(rootAA, text=" << BACK", command=ex)
    b4.place(x=320,y=220)

    # b4= Button(rootAA,text="TODAYS APPOINTMENTS",command=va)
    # b4.place(x=320,y=220)
    rootAA.mainloop()

def ex():
    global rootAA
    rootAA.destroy()

def remove():
    global e7,edd
    edd=str(e7.get())
    v=(cursor.execute("select * from appointment where ap_no='"+edd+"'"))
    v = cursor.fetchall()
    if (len(v)==0):
        errorD =  Label(rootAA, text="PATIENT APPOINTMENT NOT FIXED",fg="red")
        errorD.place(x=20,y=420)
    else:
        cursor.execute("DELETE FROM appointment where ap_no='"+edd+"'")
        con.commit()
        disd1= Label(rootAA,text="PATIENT APPOINTMENT DELETED",fg='green')
        disd1.place(x=20,y=420)

def dela():
    global e1,e7
    l3 =  Label(rootAA, text="ENTER APPOINTMENT NO TO DELETE")
    l3.place(x=20, y=340)
    e7= Entry(rootAA)
    e7.place(x=20,y=360)
    b3= Button(rootAA,text="Delete",command=remove)
    b3.place(x=50,y=380)

rootAP=None

def viewappointment():
    global e8
    ap=str(e8.get())
    vv = list(conn.execute("select * from appointment where AP_DATE=?", (ap,)))
    if (len(vv) == 0):
        errorD =  Label(rootAA, text="NO APPOINTMENT FOR TODAY", fg="red")
        errorD.place(x=20, y=420)
    else:
        s=conn.execute("Select PATIENT_ID,NAME,AP_NO,EMP_NAME,AP_DATE,AP_TIME from PATIENT NATURAL JOIN employee NATURAL JOIN appointment where AP_DATE=?",(ap,))
        for i in s:
            s1= Label(rootAP,text=i,fg='green')
            s1.place(x=10,y=85)

#
# def va():
#     global rootAP,e8
#     rootAP= Tk()
#     rootAP.geometry("500x550")
#     rootAP.title("TODAYS APPOINTMENTS")
#     h1= Label(rootAP,text="ENTER DATE TO VIEW APPOINTMENTS")
#     h1.place(x=20,y=20)
#     e8= Entry(rootAP)
#     e8.place(x=20,y=40)
#     b5= Button(rootAP,text="SEARCH",command=viewappointment)
#     b5.place(x=30,y=65)
#     rootAP.mainloop()