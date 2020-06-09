from tkinter import *
#This is the main file where root is created
import func
root = Tk()
root.title('International Investment Bank')
root.iconbitmap("lgi.ico")


func.bank_menu(root)
root.mainloop()