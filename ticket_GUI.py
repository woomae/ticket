from tkinter import *
from main import mainrun



# chg01111
# gudrms0!
# 22007717
# 20221001
# 001
# S
# B8
# 10
#14시 00분 00초

global dic
dic={}
def getdic():
  global dic
  dic["id"]=str(id_entry.get())
  dic["pw"]=str(pw_entry.get())
  dic["ln"]=str(ln_entry.get())
  dic["day"]=str(day_entry.get())
  dic["time"]=str(time_entry.get())
  dic["level"]=str(level_entry.get())
  dic["block"]=str(block_entry.get())
  dic["seat"]=str(seat_entry.get())
  dic["start"]=str(start_entry.get())
  mainrun(dic)


# GUI 생성
window=Tk()

# 화면크기 설정
window.title("ticket_macro")
window.geometry("450x400+100+100")
window.resizable(False, False)

# 텍스트 라벨 설정
label_id = Label(window, text="아이디")
label_pw = Label(window, text="비밀번호")
label_ln = Label(window, text="링크번호")
label_day = Label(window, text="날짜")
label_time = Label(window, text="시간")
label_level = Label(window, text="좌석의 등급")
label_block = Label(window, text="좌석의 구역")
label_seat = Label(window, text="열을 지정")
label_start = Label(window, text="시작시간")

#버튼 생성
start_button = Button(window,overrelief="solid",text ="예매 시작",width=15, command = getdic)
# 엔트리 설정
id_entry = Entry(window,width=15)
pw_entry = Entry(window,width=15)
ln_entry = Entry(window,width=15)
day_entry = Entry(window,width=15)
time_entry = Entry(window,width=15)
level_entry = Entry(window,width=15)
block_entry = Entry(window,width=15)
seat_entry = Entry(window,width=15)
start_entry = Entry(window,width=15)

#그리드로 위젯들 표시
label_id.grid(row=0, column=0, padx=5, pady=5)
label_pw.grid(row=1, column=0, padx=5, pady=5)
label_ln.grid(row=2, column=0, padx=5, pady=5)
label_day.grid(row=3, column=0, padx=5, pady=5)
label_time.grid(row=4, column=0, padx=5, pady=5)
label_level.grid(row=5, column=0, padx=5, pady=5)
label_block.grid(row=6, column=0, padx=5, pady=5)
label_seat.grid(row=7, column=0, padx=5, pady=5)
label_start.grid(row=8, column=0, padx=5, pady=5)


id_entry.grid(row=0,column=1, padx=5, pady=5)
pw_entry.grid(row=1,column=1, padx=5, pady=5)
ln_entry.grid(row=2,column=1, padx=5, pady=5)
day_entry.grid(row=3,column=1, padx=5, pady=5)
time_entry.grid(row=4,column=1, padx=5, pady=5)
level_entry.grid(row=5,column=1, padx=5, pady=5)
block_entry.grid(row=6,column=1, padx=5, pady=5)
seat_entry.grid(row=7,column=1, padx=5, pady=5)
start_entry.grid(row=8, column=1, padx=5, pady=5)

start_button.grid(row=9,column=2,padx=10, pady=10)



# level : VIP, R, A  등 좌석의 등급
# block : A, B, C 등 좌석의 구역을 설정
# seat : 숫자 또는 영어. 열을 지정
label_id=Label(window,text="id를 입력해주세요")
label_pw=Label(window,text="pw를 입력해주세요")
label_ln=Label(window,text="링크번호를 입력해주세요")
label_day=Label(window,text="날짜를 입력해주세요")
label_time=Label(window,text="시간를 입력해주세요")
label_level=Label(window,text="좌석의 등급를 입력해주세요 ex)20220914")
label_block=Label(window,text="좌석의 구역를 입력해주세요 ex)001, 002")
label_seat=Label(window,text="좌석의 열을 입력해주세요")
label_start=Label(window,text="예매시작시간을 입력하세요 ex)14시 00분 00초")

label_id.grid(row=0,column=2, padx=5, pady=5)
label_pw.grid(row=1,column=2, padx=5, pady=5)
label_ln.grid(row=2,column=2, padx=5, pady=5)
label_day.grid(row=3,column=2, padx=5, pady=5)
label_time.grid(row=4,column=2, padx=5, pady=5)
label_level.grid(row=5,column=2, padx=5, pady=5)
label_block.grid(row=6,column=2, padx=5, pady=5)
label_seat.grid(row=7,column=2, padx=5, pady=5)
label_start.grid(row=8,column=2, padx=5, pady=5)




window.mainloop()