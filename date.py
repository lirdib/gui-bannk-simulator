from datetime import datetime as dt
import func
import os.path
import investment
def write_date(a,n):
    N = dt.now()
    f = open(n, "w")
    s = str(N.second)
    m = str(N.minute)
    o = str(N.hour)
    f.write(s)
    f.write("\n")
    f.write(m)
    f.write("\n")
    f.write(o)
    f.close()

def read_date():
    n = name + "time.txt"
    if os.path.isfile(n):
        f=open(n,"r")
        global seconds
        global minutes
        global hour
        seconds=int(f.readline())
        minutes=int(f.readline())
        hour=int(f.readline())
        f.close()
    else:
        print("error")

name_one = func.name+ ",dateone.txt"
name_two =  func.name+ ",datesix.txt"
name_three= func.name+ ",datetwelve.txt"
def chekck_for_file(a,type):
    if os.path.isfile(number_one)or os.path.isfile(number_two) or os.path.isfile(number_three):
        func.destroy(a)
        investment.invest(a)
    else:
        if type=='o':
            n = func.name + ",dateone.txt"
            write_date(a, n, type)
        if type=='s':
            n = func.name + ",datesix.txt"
            write_date(a, n, type)
        if type=='t':
            n = func.name + ",datetwelve.txt"
            write_date(a, n, type)
        else:
            func.inner_menu(a)
