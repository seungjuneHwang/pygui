from tkinter import *
import random
#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자
# 1. 루트화면 (root window) 생성
tk = Tk() 
tk.title("점심 머먹지?")
tk.geometry("640x420")
tk.resizable(0, 0)

# 2. 텍스트 표시
label = Label(tk,text='오늘 점심 머먹지?') 
# 3. 레이블 배치 실행
label.pack()
label2 = Label(tk,text='메뉴출력') 
# 3. 레이블 배치 실행
label2.pack()
# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
menuname = '메인'  # 랜덤으로 메뉴를 저장하는 변수
image = PhotoImage(file=f"{menuname}.png") #PhotoImage를 통한 이미지 지정

def event():
    menu = ['학식','돈까스','짜장면', '김밥', '라면']
    menuname = random.choice(menu)
    label2['text'] = menuname
    image.config(file=f"{menuname}.png")


button = Button(tk,text='오늘 점심 고~',command=event)
# button2 = Button(tk,text='버튼2 입니다.')
# button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
button.pack() #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
# button2.pack(side=LEFT, padx=10, pady= 10)
label3 = Label(tk, image=image) #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
label3.pack()
# 4. 메인루프 실행
tk.mainloop()