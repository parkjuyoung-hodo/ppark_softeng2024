# ppark_softeng2024

# 과제 03_파이썬 복습 GUI
## chatgpt 질문 
def is_even(n):

    return n%2==0

def main():

    n=int(input('숫자를 입력하시오'))

    if n %2 ==0:
        print(f'{n}은 짝수입니다')

    else:
        print(f"{n}은 홀수입니다")

if __name__=='__main__':
    main()
 
이 코드로 gui를 짜달라는 질문을 하였습니다.

## chatgpt 답변 코드

import tkinter as tk
from tkinter import messagebox

### 짝수 판별 함수
def is_even(n):

    return n % 2 == 0

### 버튼 클릭 시 호출될 함수
def check_even_odd():

    num_str = ent_number.get()  
	
    if num_str.isdigit(): 
        num = int(num_str)
        if is_even(num):
            result = f"{num}은 짝수입니다."
        else:
            result = f"{num}은 홀수입니다."
        messagebox.showinfo("결과", result)  
    else:
        messagebox.showerror("오류", "유효한 숫자를 입력해주세요.")  

### 메인 함수
def main():

    # 창 설정
    window = tk.Tk()
    window.title("짝수/홀수 판별기")
    window.geometry("300x150")
    window.resizable(width=False, height=False)

    # 입력 필드와 레이블
    lbl_prompt = tk.Label(master=window, text="숫자를 입력하시오:")
    lbl_prompt.pack(pady=10)

    global ent_number  # Entry 위젯을 전역으로 사용
    ent_number = tk.Entry(master=window, width=20)
    ent_number.pack(pady=5)

    # 버튼
    btn_check = tk.Button(master=window, text="결과 확인", command=check_even_odd)
    btn_check.pack(pady=10)

    # GUI 창 실행
    window.mainloop()

if __name__ == "__main__":
    main()


    


