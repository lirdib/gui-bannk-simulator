from datetime import datetime as dt
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
