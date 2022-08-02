import tkinter as tk

disValue = 0
operator = {'+':1, '-':2, '÷':3,' * ':4, 'reset':5, '=':6}
stoValue = 0
opPre = 0

def number_click(value):
    print('숫자', value)
    global disValue
    disValue = (disValue*10) + value
    str_value.set(disValue)

def clear():
    global disValue, stoValue, opPre
    disValue = 0
    opPre = 0
    stoValue = 0
    str_value.set(disValue)

def oprator_click(value):
    print('명령', value)
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5:  #reset
        clear()
    elif disValue == 0: #reset을 제외한 다른 명령어
        opPre = 0 
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(disValue)
    elif op == 6:  #계산
        if opPre == 1: #더하기
            disValue = stoValue + disValue
        if opPre == 2: #빼기
            disValue = stoValue - disValue
        if opPre == 3: #나누기
            disValue = stoValue / disValue
        if opPre == 4: #곱하기
            disValue = stoValue * disValue  

        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        opPre = 0
    else:
        clear()




def button_click(value):
    print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        oprator_click(value)

window = tk.Tk()
window.title('계산기')

#숫자 출력


disvaValue = 0 
str_value = tk.StringVar()
str_value.set(str(disvaValue))
dis = tk.Entry(window, textvariable=str_value, justify='right')
dis.grid(column=0, row=0, columnspan = 4, ipadx=80, ipady=30)


#계산기 숫자, 연산 배치 
callable = [['1','2','3','4'],
            ['5','6','7','8'],
            ['9','0','+','-'],
            ['reset',' * ','÷','=']]

for i,item in enumerate(callable):
    for k,item in enumerate(item):
        bt = tk.Button(window, text=item, width=10, height=5, command=lambda cmd=item: button_click(cmd))
        bt.grid(column=k, row=(i+1))

#tk.Button(window, text='1', width=10, height=5, font=10).grid(column=0, row=1)

#tk.Button(window, text='2', width=10, height=5, font=10).grid(column=1, row=1)

#tk.Button(window, text='3', width=10, height=5, font=10).grid(column=2, row=1)

#tk.Button(window, text='÷', width=10, height=5, font=10).grid(column=3, row=1)

#tk.Button(window, text='4', width=10, height=5, font=10).grid(column=0, row=2)

#tk.Button(window, text='5', width=10, height=5, font=10).grid(column=1, row=2)

#tk.Button(window, text='6', width=10, height=5, font=10).grid(column=2, row=2)

#tk.Button(window, text='×', width=10, height=5, font=10).grid(column=3, row=2)

#tk.Button(window, text='7', width=10, height=5, font=10).grid(column=0, row=3)

#tk.Button(window, text='8', width=10, height=5, font=10).grid(column=1, row=3)

#tk.Button(window, text='9', width=10, height=5, font=10).grid(column=2, row=3)

#tk.Button(window, text='-', width=10, height=5, font=10).grid(column=3, row=3)

#tk.Button(window, text='reset', width=10, height=5, font=10).grid(column=0, row=4)

#tk.Button(window, text='0', width=10, height=5, font=10).grid(column=1, row=4)

#tk.Button(window, text='=', width=10, height=5, font=10).grid(column=2, row=4)

#tk.Button(window, text='+', width=10, height=5, font=10).grid(column=3, row=4)

window.mainloop()