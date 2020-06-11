import func
from tkinter import *
import date

def one_hour_invest(a):
    global type_of_invest
    type_of_invest = 'o'
    func.destroy(a)
    file_name = func.name+"balance.txt"
    fi=open(file_name,"r")
    read_bal=fi.readline()
    if int(read_bal) > 0:
        n=func.name+"date.txt"
        func.balance =  int(func.read_bal)-50
    invest_button=Button(a,text="Invest",command=lambda:func.chekck_for_file(a,type_of_invest))
    invest_button.grid(row=1,column=1)
    fi.close()

def six_hour_invest(a):
    type_of_invest = 's'
    func.destroy(a)
    file_name = func.name+"balance.txt"
    fi=open(file_name,"r")
    read_bal=fi.readline()
    if int(read_bal) > 0:
        func.balance =  int(func.read_bal)-150
    invest_button=Button(a,text="Invest",command=lambda:func.chekck_for_file(a,type_of_invest))
    invest_button.grid(row=1,column=1)
    fi.close()

def twelve_hour_invest(a):
    type_of_invest = 't'
    func.destroy(a)
    file_name = func.name+"balance.txt"
    fi=open(file_name,"r")
    read_bal=fi.readline()
    if int(read_bal) > 0:
        n=func.name+"date.txt"
        func.balance =  int(func.read_bal)-300
    invest_button=Button(a,text="Invest",command=lambda:func.chekck_for_file(a,n,type_of_invest))
    invest_button.grid(row=1,column=1)
    fi.close()

def invest(a):
    func.destroy(a)
    l=Label(a,text="Chose one investment plan")
    one=Button(a,text="1 hour",command=lambda:one_hour_invest(a))
    two=Button(a,text="6hours",command=lambda:six_hour_invest(a))
    three=Button(a,text="One day",command=lambda:twelve_hour_invest(a))
    l.grid(row=0,column=0)
    one.grid(row=1,column=0)
    two.grid(row=1,column=1)
    three.grid(row=1,column=2)
