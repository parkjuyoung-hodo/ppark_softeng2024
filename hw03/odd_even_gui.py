import tkinter as tk
from tkinter import simpledialog, messagebox


# GUI 입력 함수
def gui_input(text: str) -> str:
    return simpledialog.askstring(title='숫자 입력', prompt=text)


# 짝수 판별 함수
def is_even(n):
    return n % 2 == 0

# 메인 함수
def main():
    window = tk.Tk()
    window.withdraw()  # 기본 창 숨기기

    # 숫자 입력받기
    input_num = gui_input("숫자를 입력하세요:")


    n = int(input_num)
    if is_even(n):
        result= f'{n}은 짝수입니다'

    else:
        result = f'{n}은 홀수입니다.'

            # 결과 출력
        messagebox.showinfo("결과", result)


    window.destroy()  # 사용 후 창 닫기


if __name__ == "__main__":
    main()
