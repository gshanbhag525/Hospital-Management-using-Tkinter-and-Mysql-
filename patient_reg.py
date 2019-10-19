from tkinter import messagebox, Label, Toplevel, Frame, Entry, Button, NO, S, E, W
from tkinter.ttk import Treeview, Style
import db.db
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from PIL import ImageTk, Image

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
#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None


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


#exit from patient form
def EXO():
    rootp.destroy()


p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6,ce1,conn
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4 = pat_address.get()
    pp5 = pat_contact.get()
    pp6 = pat_CT.get()

    data = (
        pp1, pp2, pp3, pp4, pp5,pp6
    )
    if(pp1 == "" or pp2=="" or pp3=="" or pp4=="" or pp5=="" or pp6==""):
        messagebox.showinfo("insert status!", "ALL FIELDS ARE REQUIRED")
    else:
        res = db.db.pat_insert(data)
        if res:
            messagebox.showinfo("Message", "Add success")
            # menu()
        else:
            messagebox.showerror("Alert!", "Check Doc Id OR the Insert Query")

        messagebox.showinfo("Hospital DATABSE SYSTEM", "DETAILS INSERTED INTO DATABASE")

        # cursor.execute("insert into patient values('"+ pp1 +"', '"+ pp2 +"') " )
#
# def clear_text():
#     t_id.delete(0, 'end')
#     t_name.delete(0, 'end')
#     t_drug_cost.delete(0, 'end')
#     t_formula.delete(0, 'end')
#
def show_records():
    j = 0
    for i in db.db.show_pat_records():
        tr.insert('', index=j, text=j, values=(i[1], i[2], i[0], i[3]))
        j += 1

def clear_tree():
    tr.delete(*tr.get_children())

def pat_list():
    global tr

    # CLEAR = Button(center_frame, text=" CLEAR ", command=clear_text)
    # CLEAR.pack()
    CLEAR_TREE = Button(rootp, text=" Clear the table ", command=clear_tree)
    CLEAR_TREE.place()
    # CLEAR_TREE.pack()

    # right_frame = Frame(rootd, relief='raised', borderwidth=3)
    # # center_frame.pack(fill=None, expand=False)
    # right_frame.place(relx=0.65, rely=0.15, anchor=E)

    style = Style()
    style.configure("BW.TLabel", foreground="white", background="black")

    x, y = 1000, 80

    # use tree view to show the data in forms of table
    # mention the number of columns
    tr = Treeview(rootp, columns=('A', 'B', 'C', 'D', 'E'), style="BW.TLabel", selectmode="extended")
    tr.place(anchor=W)
    # heading key + text
    tr.heading('#0', text='Sr no')
    tr.column('#0', minwidth=0, width=100, stretch=NO)
    tr.heading('#1', text='Patient Name')
    tr.column('#1', minwidth=0, width=100, stretch=NO)
    tr.heading('#2', text='Gender')
    tr.column('#2', minwidth=0, width=100, stretch=NO)
    tr.heading('#3', text='Patient Id')
    tr.column('#3', minwidth=0, width=100, stretch=NO)
    tr.heading('#4', text='Address')
    tr.column('#4', minwidth=0, width=100, stretch=NO)
    tr.heading('#5', text='Consulting Doc Id')
    tr.column('#5', minwidth=0, width=100, stretch=NO)

    show_records()

    tr.place(x=900, y=y + 100)
    # tr.pack(expand=True, fill='y')


def pat_screen():
    global pat_address, pat_contact, pat_CT, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,sex,ct,addr,c1,c2,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    global copy_of_image, label
    global rootp

    rootp= Toplevel()
    rootp.title("PATIENT FORM")
    rootp.geometry("1920x1080")

    copy_of_image = Image.open("images/hospital.jpeg")
    photo = ImageTk.PhotoImage(copy_of_image)

    label = Label(rootp, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    center_frame = Frame(rootp, relief='raised', borderwidth=2)
    # center_frame.pack(fill=None, expand=False)
    center_frame.place(relx=0.22, rely=0.6, anchor=S)

    regform = Label(center_frame, text="PATIENT REGISTRATION FORM", padx=5, pady=5,
                   fg='BLACK', bg='GREY', font="Helvetica 30 bold")
    regform.grid(columnspan=2, padx=5, pady=5) #, sticky=W+E)

    id = Label(center_frame,text="PATIENT ID", font='Helvetica 20 bold ')
    # id.pack(side=LEFT, padx=5, pady=5)
    id.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    pat_ID = Entry(center_frame)
    pat_ID.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    name = Label(center_frame,text="PATIENT NAME", font='Helvetica 20 bold ')
    name.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    pat_name =  Entry(center_frame)
    pat_name.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    sex= Label(center_frame,text="GENDER", font='Helvetica 20 bold')
    sex.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    pat_sex= Entry(center_frame)
    pat_sex.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    addr =  Label(center_frame, text="ADDRESS", font='Helvetica 20 bold')
    addr.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    pat_address =  Entry(center_frame)
    pat_address.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    c1 =  Label(center_frame, text="CONTACT NUMBER", font='Helvetica 20 bold')
    c1.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    pat_contact =  Entry(center_frame)
    pat_contact.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    ct =  Label(center_frame, text="CONSULTING TEAM / DOCTOR ID", font='Helvetica 20 bold')
    ct.grid(row=6, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    pat_CT =  Entry(center_frame)
    pat_CT.grid(row=6, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    SUBMIT = Button(center_frame, text="  SUBMIT  ",font='Helvetica 20 bold ',
                    command=IN_PAT)
    SUBMIT.grid(row=7, columnspan=2, padx=5, pady=10, ipadx=5, ipady=10)

    back= Button(center_frame,text="<< BACK", font='Helvetica 20 bold ',
                    command=EXO)
    back.grid(row=8, column=0, padx=5, pady=5, ipadx=5, ipady=10)

    SEARCH= Button(center_frame,text="  SEARCH >>  ", font='Helvetica 20 bold ',
                    command=P_display)
    SEARCH.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=10)

    DELETE= Button(center_frame,text="  DELETE  ", font='Helvetica 20 bold ',
                    command=D_display)
    DELETE.grid(row=9, column=0, padx=5, pady=5, ipadx=5, ipady=10)

    UPDATE= Button(center_frame,text="  UPDATE  ", font='Helvetica 20 bold ',
                    command=P_UPDATE)
    UPDATE.grid(row=9, column=1, padx=5, pady=5, ipadx=5, ipady=10)

    pat_list()

    rootp.mainloop()
