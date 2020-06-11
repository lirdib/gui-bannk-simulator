from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

from datetime import datetime as dt
import os.path
import date
import investment
#main function at line 109
def Si(x):#This function is shown when user clicks sing in button in main bank menu

    global balance # When a new user registers it is automaticaly generated a balance of 500(currency not determined what) as we suppose that this si a demo account
    balance=500
    destroy(x) # Function at line 140
    global moeney1
    global imageMoney1
    imageMoney1 = Image.open("money1.jpg")
    imageMoney1 = imageMoney1.resize((200, 250), Image.ANTIALIAS)
    moeney1 = ImageTk.PhotoImage(imageMoney1)
    photoLabe = Label(x, image=moeney1)
    photoLabe.grid(row=2, column=4, rowspan=5)
    global Leemri
    Leemri= Label(x, text="Ju lutem shkruani emrin tuaj")
    Leemri.grid(row=2,column=0)
    e= Entry(x)
    e.grid(row=3,column=0)
    global Lpass
    Lpass = Label(x, text="Ju lutem shkruani passwordin")
    Lpass.grid(row=4,column=0)

    p = Entry(x)
    p.grid(row=5,column=0)
    global sigin
    sigin=Button(x,text="Sign in",command=lambda:file(x,e,p)) #function at line 93
    sigin.grid(row=6,column=0)


def Login(x):# This function is called when user click log in button

    destroy(x)
    global rgrpah
    global imageR
    imageR = Image.open("risinggrap.jpg")
    imageR=imageR.resize((200,250),Image.ANTIALIAS)
    rgrpah = ImageTk.PhotoImage(imageR)
    photoLabe = Label(x,image = rgrpah)
    photoLabe.grid(row=3, column=4,rowspan=4)
    global fgrpah
    global imageF
    imageF = Image.open("fallgraph.jpg")
    imageF = imageF.resize((200, 250), Image.ANTIALIAS)
    fgrpah = ImageTk.PhotoImage(imageF)
    photoLabe = Label(x, image=fgrpah)
    photoLabe.grid(row=3, column=0, rowspan=4)
    global lem
    lem=Label(x,text="Please enter you name")
    lem.grid(row=3,column=1)
    global ee
    ee = Entry(x)
    ee.grid(row=4, column=1)
    global lpass
    lpass =  Label(x, text="Please enter your password")
    lpass.grid(row=5,column=1)
    global pp
    pp = Entry(x)
    pp.grid(row=6, column=1)
    global login
    login = Button(x, text ="Login",command=lambda:get_name_pass(x)) #Function at line72
    login.grid(row=7, column=1)


name= ' '
def get_name_pass(x): #This function is called inside Login function. This is used to read from the file where user's name and passwords are written and see if the match the input given by user who wants to log in
    global fname
    global name
    name = ee.get()
    fname = ee.get() + ".txt"
    if os.path.isfile(fname): #Check if file exists, if yes it means that user is already registered
        fi = open(fname, "r")
        if (fi.readline()) == (ee.get() + "." + pp.get()):
            global read_bal
            read_bal = read_balance()
            inner_menu(x)#Function at line 126
    else:
        response = messagebox.askyesno("Error", "Name or password not correct. Clik yes to try again or No no return back to main menu")
        if response == 1:
            ee.delete('0','end')
            pp.delete('0','end')
        elif response ==0:
            bank_menu(x)




def file(root,e,p): #This functions creates 2 new texts files when users signs in; one which writes users balance(which name is user name + "balance.txt") and another file where it writes username and password

    a=e.get()
    b=p.get()
    fname = e.get() + ".txt"
    if os.path.isfile(fname):
        response = messagebox.askyesno("Error", "User already registered. Clik yes to try again or No no return back to main menu")
        if response == 1:
            e.delete('0','end')
            p.delete('0','end')
        elif response ==0:
            bank_menu(root)
    else:
        f = open(fname, "w")
        f.write(a)
        f.write(".")
        f.write(b)
        f.close()
        balance_name = e.get() + "balance.txt"
        fil = open(balance_name, "w")
        fil.write(str(balance))
        fil.close()
        bank_menu(root)



def bank_menu(a):# This is the main bank function it show the bank menu where you can signin,login or exit.
    destroy(a)
    global photo
    photo = ImageTk.PhotoImage(Image.open("graph.jpg"))
    photoLabel = Label(a, image=photo)
    photoLabel.grid(row=2, column=0,columnspan=3)
    global l
    l=Label(a,text="Welome to our banks.         Please choose what do you want to do")
    l.grid(row=0,column=0,columnspan=3)
    global signin
    global login
    global exit
    signin = Button(a,text="Signin",padx=40,pady=20,command=lambda:Si(a),borderwidth=4) #Function at line 9
    login = Button(a,text="Login",padx=40,pady=20,command=lambda:Login(a),cursor="shuttle",borderwidth=4)
    exit=Button(a,text="Exit",padx=40,pady=20,command=a.quit,borderwidth=4)
    signin.grid(row=1,column=0)
    login.grid(row=1,column=1)
    exit.grid(row=1,column=2)



def inner_menu(a): # This function is used to display inner bank menu, by which is meant the menu which displays afet the user is loged in
    destroy(a)
    currBal= read_balance()
    l=Label(a,text="Welcome to bank menu " + name+"             Your balance is: "+ currBal)
    l.grid(row=0,column=0)
    investemnt=Button(a,text="Invest",padx=40,command=lambda:investment.invest(a)) # Function at investment file, line 44
    withdraw_from_investment=Button(a,text="Withdraw money from investment",command=lambda:withdraw_money_from_invest(a)) # Function at line 144
    investemnt.grid(row=1,column=0,padx=40)
    withdraw_from_investment.grid(row=1,column=1,padx=40)

def destroy(a): # This is a simple function called at same new pages to clear them and get a blank page to add new thigns to it.
    for widget in a.winfo_children():
        widget.destroy()


print()



def withdraw_money_from_invest(a):
    destroy(a)
    l = Label(a, text="from which investment do you want to withdraw moneys")
    l.grid(row=0,column=1)
    nje = Button(a, text="1 hour",command=lambda:one_hour_withdraw(a))
    two = Button(a, text="6hours",command=lambda:six_hour_withdraw(a))
    three = Button(a, text="One day")
    nje.grid(row=1, column=0)
    two.grid(row=1, column=1)
    three.grid(row=1, column=2)


def one_hour_withdraw(a):
    type= 'o'
    destroy(a)
    b=Button(a,text="Clcik me",command=lambda:calculations(type))
    b.grid(row=0,column=0)


def six_hour_withdraw(a):
    type= 's'
    destroy(a)
    b=Button(a,text="Clcik me",command=lambda:calculations(type))
    b.grid(row=0,column=0)


def calculations(type):

    n = dt.now()
    s = int(n.second)
    m = int(n.minute)
    o = int(n.hour)

    time =date.read_date(type)
    seconds = time[0]
    minutes = time[1]
    hour = time[2]
    if seconds > s:
        s = s + 60
        m = m - 1
        sec = s - seconds

        if minutes > m:
            m = m + 60
            o = o - 1
            min = m - minutes
            ho = o - hour
        else:

            min = m - minutes
            ho = o - hour
    else:
        sec = s - seconds
        min = m - minutes
        ho = o - hour

    if type=='o':
        if ho >= 1:
            c_b=read_balance()
            c_b = int(c_b)+200
            write_balance(c_b)
            os.remove(name+"dateone.txt")
    if type=='s':
        if ho >= 6:
            c_b=read_balance()
            c_b = int(c_b)+400
            write_balance(c_b)



def read_balance():
    global n
    n = name + "balance.txt"
    f=open(n,'r')
    current_balance=f.readline()
    f.close()

    return current_balance

def write_balance(bal):
    n = name + "balance.txt"
    f = open(n, 'w')
    f.write(str(bal))
    f.close()

name_one = name+ "dateone.txt"
name_two =  name+ "datesix.txt"
name_three= name+ "datetwelve.txt"

def chekck_for_file(a,type):
    if os.path.isfile(name_one)or os.path.isfile(name_two) or os.path.isfile(name_three):
        destroy(a)
        investment.invest(a)
    else:
        if type=='o':
            n = name + "dateone.txt"
            date.write_date(a, n)
        if type=='s':
            n = name + "datesix.txt"
            date.write_date(a, n)
        if type=='t':
            n = name + "datetwelve.txt"
            date.write_date(a, n)
        else:
            inner_menu(a)