from tkinter import *
import random
#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자
# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
label = Label(tk,text='오늘 점심 머먹지?') 
# 3. 레이블 배치 실행
label.pack()
label2 = Label(tk,text='메뉴출력') 
# 3. 레이블 배치 실행
label2.pack()
# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
def event():
    menu = ['학식','돈까스','짜장면', '김밥', '라면']
    label2['text'] = random.choice(menu)

button = Button(tk,text='오늘 점심 고~',command=event)
# button2 = Button(tk,text='버튼2 입니다.')
# button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
button.pack() #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
# button2.pack(side=LEFT, padx=10, pady= 10)
# 4. 메인루프 실행
tk.mainloop()