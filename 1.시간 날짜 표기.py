from time import*
from tkinter import *
from turtle import title 

time()
tm = localtime(time())
gmtime(time())
root = Tk()
root.title('JARVIS')
root.geometry("380x200")

def showtime():
    time()
    tm = localtime(time())
    gmtime(time())
    print("오늘은",tm.tm_year,"년",tm.tm_mon,"월",tm.tm_mday,"일 입니다.")

def showtime2():
    time()
    tm = localtime(time())
    gmtime(time())
    a = tm.tm_hour
    print("지금은",tm.tm_hour,"시",tm.tm_min,"분",tm.tm_sec,"초 입니다.")    

btn1 = Button(root,text='오늘의 날짜',command = showtime,padx=30, pady=10,bg='yellow',font=25)
btn1.pack(side="left")
btn2 = Button(root,text='현재 시간',command = showtime2,padx=30, pady=10,bg='yellow',font=25)
btn2.pack(side="left")

root.mainloop()