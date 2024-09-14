#소수 판별하기
import tkinter as tk
from tkinter import simpledialog, messagebox

def gui_input(text: str) -> str:
    return simpledialog.askstring(title='숫자 입력', prompt=text)

def is_prime(n:int)->bool:
    if n<2:
        return False

    for i in range(2,n):
        if n % i ==0:
            return False
    return True

def main():
    window = tk.Tk()
    window.withdraw()  # 기본 창 숨기기

    # 숫자 입력받기
    input_num = gui_input("숫자를 입력하세요:")

    n = int(input_num)
    if is_prime(n):
        result = f'{n}은 소수 입니다'

        messagebox.showinfo("결과", result)

    else:
        result = f'{n}은 소수가 아닙니다.'

        # 결과 출력
        messagebox.showinfo("결과", result)

    window.destroy()  # 사용 후 창 닫기



if __name__=="__main__":
    main()