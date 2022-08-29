__author__ = "macaw"
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import datetime




main = Tk()
main.geometry("1366x768")
main.title("Supermarket Management System")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()
    


label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)



GMT = datetime.timezone(datetime.timedelta(hours=8)) 
a = tk.StringVar() 

def showTime():
    now = datetime.datetime.now(tz=GMT).strftime("%Y-%m-%d - %H:%M:%S")   # 取得目前的時間，格式使用 H:M:S
    a.set(now)                    # 設定變數內容
    main.after(1000, showTime)    # 視窗每隔 1000 毫秒再次執行一次 showTime()

tk.Label(main, textvariable=a, font=('Arial',12)).pack(side='bottom')   # 放入第二個 Label 標籤，內容是 a 變數

showTime() 

main.mainloop()
