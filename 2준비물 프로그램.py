from time import*
from tkinter import *
from turtle import title 

root = Tk()
root.title('JARVIS')
root.geometry("380x200")

suplist = []#준비물 리스트
OPR = 1

def put(): #준비물 입력
    suplist.append(supI)
    print(suplist)
def delete(): #준비물 제거
    supD = input('제거할 준비물의 이름을 말해주세요.')
    suplist.remove(supD)
    print(suplist)
putbtn = Button(root,text='준비물 입력',command=put)
putbtn.pack()
deletebtn = Button(root,text='준비물 제거',command=delete)
deletebtn.pack()

TxT = Text(root, width=30, height=5)
TxT.pack()

def btncmd():
    print(TxT.get("1.0", END))
    supI = TxT.get("1.0", END)
    TxT.delete("1.0", END)
btn = Button(root, text = '클릭', command=btncmd)
btn.pack()

root.mainloop()