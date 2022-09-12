from tkinter import *

def pr_id(event):
  label_id.config(text="출력 : "+str(id_entry.get()))
def pr_pw(event):
  label_pw.config(text="출력 : "+str(pw_entry.get()))
def pr_ln(event):
  label_ln.config(text="출력 : "+str(ln_entry.get()))


# GUI 생성
window=Tk()

# 화면크기 설정
window.title("ticket_macro")
window.geometry("450x400+100+100")
window.resizable(False, False)

# 텍스트 라벨 설정
bt_id = Label(window, text="아이디")
bt_pw = Label(window, text="비밀번호")
bt_ln = Label(window, text="링크번호")

bt_date = Label(window, text="날짜")
bt_hour = Label(window, text="시간")
bt_level = Label(window, text="좌석의 등급")
bt_block = Label(window, text="좌석의 구역")
bt_seat = Label(window, text="열을 지정")

# 엔트리 설정
id_entry = Entry(window,width=15)
pw_entry = Entry(window,width=15)
ln_entry = Entry(window,width=15)

# 엔트리와 함수 묶기
id_entry.bind("<Return>",pr_id)
pw_entry.bind("<Return>",pr_pw)
ln_entry.bind("<Return>",pr_ln)

#그리드로 위젯들 표시
bt_id.grid(row=0, column=0, padx=5, pady=5)
bt_pw.grid(row=1, column=0, padx=5, pady=5)
bt_ln.grid(row=2, column=0, padx=5, pady=5)
id_entry.grid(row=0,column=1, padx=5, pady=5)
pw_entry.grid(row=1,column=1, padx=5, pady=5)
ln_entry.grid(row=2,column=1, padx=5, pady=5)


label_id=Label(window,text="id를 입력해주세요")
label_pw=Label(window,text="pw를 입력해주세요")
label_ln=Label(window,text="링크번호를 입력해주세요")
label_id.grid(row=0,column=2, padx=5, pady=5)
label_pw.grid(row=1,column=2, padx=5, pady=5)
label_ln.grid(row=2,column=2, padx=5, pady=5)


window.mainloop()