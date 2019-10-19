import db.db
from tkinter import messagebox, Label, Toplevel, Frame, Entry, Button, W, NO
from tkinter.ttk import Treeview, Style
from db.db import cursor,con
from PIL import ImageTk, Image

global label,copy_of_image, right_frame, con, cursor

label = None
copy_of_image = None
rootd = None
right_frame = None


def clear_text():
    t_id.delete(0, 'end')
    t_name.delete(0, 'end')
    t_drug_cost.delete(0, 'end')
    t_formula.delete(0, 'end')

#EXIT for MENU
def ex():
    global rootd
    rootd.destroy()

p=None
#input patient form
def IN_DRUG():
    global pp1, pp2, pp3, pp4, pp5, pp6,ce1,conn
    pp1=t_id.get()
    pp2=t_name.get()
    pp3=t_formula.get()
    pp4 = t_drug_cost.get()

    drug_data = (
        pp1, pp2, pp3, pp4
    )
    if(pp1 == "" or pp2=="" or pp3=="" or pp4=="" ):
        messagebox.showinfo("insert status!", "ALL FIELDS ARE REQUIRED")
    else:
        con.connect()
        res = cursor.execute("insert into drug(drug_id,drug_name,formula,drug_cost) values(%s,%s,%s,%s)",drug_data)
        con.commit()

        if res:
            messagebox.showinfo("Message", "Add success")
        else:
            messagebox.showinfo("message", " Data Added Successfully")
        # cursor.close()
        # con.close()
        # cursor.execute("insert into patient values('"+ pp1 +"', '"+ pp2 +"') " )

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

def show_records():
    j = 0
    for i in db.db.show_drug_records():
        tr.insert('', index=j, text=j, values=(i[1], i[2], i[0], i[3]))
        j += 1

def clear_tree():
    tr.delete(*tr.get_children())

def drug():
    global t_id,t_name,t_formula,t_drug_cost
    global rootd,regform,id,name,formula,drug_cost,c1,c2,\
        SUBMIT,back,SEARCH,DELETE,UPDATE, CLEAR
    global copy_of_image, label, rootd
    global l_drug_name, l_drug_formula, l_drug_id, l_drug_price, right_frame, tr, count

    rootd= Toplevel()
    rootd.title("DRUG FORM")
    rootd.configure(background='black')
    rootd.geometry("1920x1080")
    copy_of_image = Image.open("images/hospital.jpeg")
    photo = ImageTk.PhotoImage(copy_of_image)

    label = Label(rootd, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.bind('<Configure>', resize_image)

    center_frame = Frame(rootd, relief='raised', borderwidth=2)
    # center_frame.pack(fill=None, expand=False)
    center_frame.place(relx=0.1, rely=0.2, anchor=W)

    regform= Label(center_frame,text="DRUG FORM",font="helvetica 19 bold")
    regform.pack()

    id= Label(center_frame,text="DRUG ID")
    id.pack()

    t_id= Entry(center_frame)
    t_id.pack()

    name= Label(center_frame,text="DRUG NAME")
    name.pack()

    t_name =  Entry(center_frame)
    t_name.pack()

    formula= Label(center_frame,text="FORMULA")
    formula.pack()

    t_formula= Entry(center_frame)
    t_formula.pack()

    drug_cost =  Label(center_frame, text="DRUG COST")
    drug_cost.pack()

    t_drug_cost =  Entry(center_frame)
    t_drug_cost.pack()

    SUBMIT = Button(center_frame, text="  SUBMIT  ", command=IN_DRUG)
    SUBMIT.pack()

    back= Button(center_frame,text="<< BACK",command=ex)
    back.pack()

    CLEAR = Button(center_frame, text=" CLEAR ", command=clear_text)
    CLEAR.pack()

    CLEAR_TREE = Button(rootd, text=" Clear the table ", command=clear_tree)
    CLEAR_TREE.place()
    CLEAR_TREE.pack()

    # right_frame = Frame(rootd, relief='raised', borderwidth=3)
    # # center_frame.pack(fill=None, expand=False)
    # right_frame.place(relx=0.65, rely=0.15, anchor=E)

    style = Style()
    style.configure("BW.TLabel", foreground="white", background="black")

    x, y = 70, 20

    # use tree view to show the data in forms of table
    # mention the number of columns
    tr = Treeview(rootd, columns=('A', 'B', 'C', 'D'), style="BW.TLabel", selectmode="extended")
    # heading key + text
    tr.heading('#0', text='Sr no')
    tr.column('#0', minwidth=0, width=100, stretch=NO)
    tr.heading('#1', text='Drug Name')
    tr.column('#1', minwidth=0, width=100, stretch=NO)
    tr.heading('#2', text='Drug Formula')
    tr.column('#2', minwidth=0, width=100, stretch=NO)
    tr.heading('#3', text='Drug Id')
    tr.column('#3', minwidth=0, width=100, stretch=NO)
    tr.heading('#4', text='Drug Price')
    tr.column('#4', minwidth=0, width=100, stretch=NO)

    show_records()

    tr.place(x=50, y=y + 50)
    tr.pack(expand=True, fill='y')
    # SEARCH= Button(center_frame,text="  SEARCH >>  ",command=P_display)
    # SEARCH.pack()
    # DELETE= Button(center_frame,text="  DELETE  ",command=D_display)
    # DELETE.pack()
    # UPDATE= Button(center_frame,text="  UPDATE  ",command=P_UPDATE)
    # UPDATE.pack()

    rootd.mainloop()

