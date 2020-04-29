from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

width,height="700","500"
framecolor="green"
framefg="white"
fontsize=20


t=Tk()
t.geometry(width+"x"+height)
t.resizable(0,0)

usern = StringVar ()
usern2 = StringVar ()
userp = StringVar ()
usercn = StringVar ()


def loggedin():
    notebookcolor="red"
    nb=ttk.Notebook()
    nb.place(x=0,y=0,width=width,height=height)


    f1=Frame(bg=notebookcolor)
    nb.add(f1,text="manan")
    Label(f1, text="Enter Roll.No. ", bg=notebookcolor, font=("", 17)).place(x=60, y=50)
    entryrn = Entry(f1, font=("", 15), width=18)
    entryrn.place(x=300, y=50)
    Label(f1, text="Enter Name", bg=notebookcolor, font=("", 17)).place(
        x=60, y=100)
    entryname = Entry(f1, font=("", 15), width=18)
    entryname.place(x=300, y=100)
    Label(f1, text="Physics Marks", bg=notebookcolor, font=("", 17)).place(
        x=60, y=150)
    entryphy = Entry(f1, font=("", 15), width=18)
    entryphy.place(x=300, y=150)
    Label(f1, text="Chemistry Marks", bg=notebookcolor, font=("", 17)).place(
        x=60, y=200)
    entrychem = Entry(f1, font=("", 15), width=18)
    entrychem.place(x=300, y=200)
    Label(f1, text="Mathematics Marks", bg=notebookcolor, font=("", 17)).place(
        x=60, y=250)
    entrymath = Entry(f1, font=("", 15), width=18)
    entrymath.place(x=300, y=250)
    Button(f1, text="Submit", font=("", 15), bg=notebookcolor,activebackground="blue"
           ).place(x=int(width) / 3, y=int(height) / 2 + 100)


    f2=Frame(bg="green")
    nb.add(f2,text="manan")

    f6=Frame(bg="black")
    nb.add(f6,text="Logout")
    Button(f6,text="logout",command=home).place(x=int(width)/2,y=int(height)/2)

def login():
    db = sqlite3.connect('projectdb.db')
    cr = db.cursor()
    got=cr.execute("select * from users where UNAME='"+usern.get()+"' AND UPASS='"+userp.get()+"'")
    for i in got :
        print(i)
        loggedin()
        usern2.set(usern.get())
        messagebox.showinfo("Its My First Python Project", "WELCOME "+usern2.get()+" !!")
        break
    else:
        messagebox.showinfo("Title","No such user found")
    db.commit()
    db.close()
    userp.set("")
    usern.set("")
    usercn.set("")

def testUserData():

    freeoferrors=[True,True,True]
    if len(usern.get())==0:
        freeoferrors[0]=False
        print("name short")
    if len(userp.get())<5:
        freeoferrors[1]=False
        print("pass short")
    if len (list (filter( lambda x:x!=" ", usern.get() ) ) ) == 0:
        print("done for n")
        freeoferrors[0]=False
    if len(userp.get()) != len (list (filter (lambda x:x!=" ", userp.get() ))):
        print("done for p")
        freeoferrors[1]=False
    if len(usercn.get())!=10:
        freeoferrors[2]=False
        print("contact error")

    try:
        for i in range(10):
            iWantNumbers = int(usercn.get()[i])
    except ValueError:
        freeoferrors[2]=False
        print("didnt get numbers")
    except IndexError:
        freeoferrors[2] = False
    return freeoferrors

def submit():
    emsg=""
    if testUserData()==[True,True,True]:
        db = sqlite3.connect('projectdb.db')
        cr = db.cursor()
       # cr.execute("create table users(UNAME text , UPASS text , UCN text)")
        cr.execute(
            "insert into users(UNAME , UPASS , UCN) VALUES('"+usern.get()+"','"+userp.get()+"','"+usercn.get()+"')")
        db.commit()
        db.close()
        print("User registered")
        messagebox.showinfo("Title", usern.get()+" succesfully Registered" )
        home()
    else:
        elist=testUserData()
        emsg=""
        if elist[0]==False:
            emsg=emsg+"* Please Enter User Name\n"
        if elist[1]==False :
            emsg = emsg + "* Password Too Short , min. 5 letters req.\n"
        if elist[2]==False :
            emsg = emsg + "* Enter Valid 10 Digit Contact no.\n"
        errormessage = Label( text=emsg, font=("Consolas", 11),
                                  fg="#aaff12", bg="red",width=47)
        errormessage.place(x=int(width) / 3-20, y=int(height) / 2 + 150)
        print("error")
    userp.set('')
    usern.set('')
    usercn.set('')



def loginPage():
    loginpage=Frame(bg=framecolor)
    loginpage.place(x=0,y=0,width=width,height=height)

    Label(loginpage,text="Enter Name ",bg=framecolor,font=("",20)).place(x=60,y=100)
    Label(loginpage,text="Enter Password ", bg=framecolor, font=("", 20)).place(
        x=60, y=190)
    entryname = Entry(loginpage,font=("", 20), width=18,textvariable=usern)
    entryname.place(x=300, y=100)
    entrypassword = Entry(loginpage,font=("", 20), width=18,show='*',textvariable=userp)
    entrypassword.place(x=300, y=190)
    Button(loginpage,text="LogIn",font=("",15),bg=framecolor,
           command=login).place(x=int(width)/3,y=int(height) / 2+50)
    Button(loginpage,text="Back to Home",font=("",15),bg=framecolor,
           command=home).place(x=0,y=int(height)-50)
    Button(loginpage,text="Register",font=("",15),bg=framecolor,
           command=registerPage).place(x=int(width)-100,y=int(height)-50)


def registerPage():
    framecolor = "green"
    registerpage = Frame(bg=framecolor)
    registerpage.place(x=0, y=0, width=width, height=height)

    Label(registerpage,text="Enter Name ", bg=framecolor, font=("", 20)).place(
        x=60, y=80)
    Label(registerpage,text="Enter Password ", bg=framecolor, font=("", 20)).place(
        x=60, y=170)
    Label(registerpage,text="Enter Contact no. ", bg=framecolor, font=("", 20)).place(
        x=60, y=260)
    entryname = Entry(registerpage,font=("", 20), width=18,textvariable=usern)
    entryname.place(x=300, y=80)
    entrypassword = Entry(registerpage,font=("", 20), width=18,textvariable=userp)
    entrypassword.place(x=300, y=170)
    entrycontact = Entry(registerpage,font=("", 20), width=18,textvariable=usercn)
    entrycontact.place(x=300, y=260)
    Button(registerpage,text="Submit", font=("", 15), bg=framecolor,
           command=submit).place(x=int(width) / 3, y=int(height) / 2+100)
    Button(registerpage,text="Back to Home", font=("", 15), bg=framecolor,
           command=home).place(x=0, y=int(height) - 50)
    Button(registerpage,text="Log in", font=("", 15), bg=framecolor,
           command=loginPage).place(x=int(width) - 100, y=int(height) - 50)

def home():
    homepage=Frame(bg=framecolor)
    homepage.place(x=0,y=0,width=width,height=height)

    Label(text="HOME PAGE",font=("",40)).place(x=int(width)/4,y=int(height)/10)  

    blg=Button(homepage,text="Log in",font=("",20),width=10,height=1,
               command=loginPage)
    blg.place(x=int(width)/4-50,y=int(height)/2)

    breg =Button(homepage,text="Register",font=("",20),width=10,height=1,
                 command=registerPage)
    breg.place(x=int(width)/2+50,y=int(height)/2)

home()


t.mainloop()