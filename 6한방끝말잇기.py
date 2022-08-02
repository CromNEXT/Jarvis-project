import random
import time
from tkinter import *
from turtle import title 

onepunch = ['마귀광대버섯', '나트륨','띄움닻','러시안룰렛','레쿠쟈','개뻘','나옹','내비게이션','마그네슘','반지름','버섯','밥그릇','로켓','히읗','아빠','이리듐']
def selectRandom(onepunch):
    return random.choice(onepunch)

R = 0
print("명령어를 입력하세요.")
a = str(input())
R = 1
while(R):    
    if a == '끝말잇기':
        print("제가 먼저 시작할게요.")
        time.sleep(0.5)
        print(selectRandom(onepunch))
        time.sleep(0.5)
        print("하하 제가 이겼네요.")
        time.sleep(0.5)
        print("명령어를 입력하세요.")
        a = str(input())
        
    else:
        print("잘 못 알아들었어요.")
        time.sleep(0.5)
        print("명령어를 입력하세요.")    
        a = str(input())