#module
import random
from tkinter import *
from turtle import title 
from time import*

#basic setting
root = Tk()
root.title('JARVIS')
root.geometry("250x200")

#time
time()
tm = localtime(time())
gmtime(time())

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

#time/daily button
dailybtn = Button(root,text='오늘의 날짜',command = showtime)
dailybtn.pack()
timebtn = Button(root,text='현재 시간',command = showtime2)
timebtn.pack()

#language game
#game list
onepunch = ['나트륨','띄움닻','러시안룰렛','레쿠쟈','개뻘','내비게이션','마그네슘','반지름','버섯','밥그릇','로켓','히읗','아빠','이리듐','피읖','티읕','수산화나트륨']

def selectRandom(onepunch):
    return random.choice(onepunch)

def finish():
    print("제가 먼저 시작할게요.")
    sleep(0.5)
    print(selectRandom(onepunch))
    sleep(0.5)
    print("하하 제가 이겼네요.")
#game button
gmbtn = Button(root,text='끝말잇기 도전',command=finish)
gmbtn.pack()

]


#endless loop
root.mainloop()