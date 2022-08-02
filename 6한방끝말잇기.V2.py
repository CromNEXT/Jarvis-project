import random
import time
from tkinter import *
from turtle import title 
root = Tk()
root.title('JARVIS')
root.geometry("200x100")

onepunch = ['나트륨','띄움닻','러시안룰렛','레쿠쟈','개뻘','내비게이션','마그네슘','반지름','버섯','밥그릇','로켓','히읗','아빠','이리듐','피읖','티읕','수산화나트륨']

def selectRandom(onepunch):
    return random.choice(onepunch)

def finish():
    print("제가 먼저 시작할게요.")
    time.sleep(0.5)
    print(selectRandom(onepunch))
    time.sleep(0.5)
    print("하하 제가 이겼네요.")

btn1 = Button(root,text='끝말잇기 도전',command=finish)
btn1.pack()
root.mainloop()        