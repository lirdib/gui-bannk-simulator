from tkinter import *
from datetime import datetime as dt
import os.path
import date
import investment
def Si(x):
    global balance
    balance=500
    destroy(x)
    global Leemri
    Leemri= Label(x, text="Ju lutem shkruani emrin tuaj")
    Leemri.grid(row=2,column=0)
    e= Entry(x)
    e.grid(row=3,column=0)
    global Lpass
    Lpass = Label(x, text="Ju lutem shkruani passwordin")
    Lpass.grid(row=4,column=0)
    global p
    p = Entry(x)
    p.grid(row=5,column=0)
    global sigin
    sigin=Button(x,text="Sign in",command=lambda:file(x,e))
    sigin.grid(row=6,column=0)
    fname = e.get() + ".txt"
    f= open(fname,"w")
    f.write(e.get())
    f.write(".")
    f.write(p.get())
    f.close()

def Login(x):

    destroy(x)
    global lem
    lem=Label(x,text="Ju lutem shkruani emrin tuaj")
    lem.grid(row=3,column=0)
    global ee
    ee = Entry(x)
    ee.grid(row=4, column=0)
    global lpass
    lpass =  Label(x, text="Ju lutem shkruani passwordin")
    lpass.grid(row=5,column=0)
    global pp
    pp = Entry(x)
    pp.grid(row=6, column=0)
    global login
    login = Button(x, text ="Login",command=lambda:get_name_pass(x))
    login.grid(row=7, column=0)


def get_name_pass(x):
    global fname
    global name
    name = ee.get()
    fname = ee.get() + ".txt"
    if os.path.isfile(fname):
        fi = open(fname, "r")
        if (fi.readline()) == (ee.get() + "." + pp.get()):
            global read_bal
            read_bal = read_balance()
            inner_menu(x)
    else:
        print("error")



def file(root,e):
    a=e.get()
    b=p.get()
    fname = e.get() + ".txt"
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



def bank_menu(a):
    destroy(a)
    global l
    l=Label(a,text="Please choose what do you want to do")
    l.grid(row=0,column=0,columnspan=3)
    global signin
    global login
    global exit
    signin = Button(a,text="Signin",padx=25,command=lambda:Si(a))
    login = Button(a,text="Login",padx=25,command=lambda:Login(a))
    exit=Button(a,text="Exit",padx=25)
    signin.grid(row=1,column=0)
    login.grid(row=1,column=1)
    exit.grid(row=1,column=2)

def inner_menu(a):
    destroy(a)
    l=Label(a,text="Welcome to bank menu")
    l.grid(row=0,column=0)
    investemnt=Button(a,text="Invest",padx=40,command=lambda:investment.invest(a))
    withdraw_from_investment=Button(a,text="Withdraw money from investment",command=lambda:withdraw_money_from_invest(a))
    investemnt.grid(row=1,column=0,padx=40)
    withdraw_from_investment.grid(row=1,column=1,padx=40)

def destroy(a):
    for widget in a.winfo_children():
        widget.destroy()






def withdraw_money_from_invest(a):
    destroy(a)
    l = Label(a, text="from which investment do you want to withdraw moneys")
    l.grid(row=0,column=1)
    nje = Button(a, text="1 hour",command=lambda:one_hour_withdraw(a))
    two = Button(a, text="6hours")
    three = Button(a, text="One day")
    nje.grid(row=1, column=0)
    two.grid(row=1, column=1)
    three.grid(row=1, column=2)

def one_hour_withdraw(a):

    type= 'o'
    destroy(a)
    b=Button(a,text="Clcik me",command=lambda:calculations(type))
    b.grid(row=0,column=0)

def calculations(type):
    date.read_date()
    n = dt.now()
    s = int(n.second)
    m = int(n.minute)
    o = int(n.hour)
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



def read_balance():
    global n
    n = name + "balance.txt"
    f=open(n,'r')
    current_balance=f.readline()
    f.close()
    print(current_balance)
    return current_balance

def write_balance(bal):
    n = name + "balance.txt"
    f = open(n, 'w')
    f.write(str(bal))
    f.close()