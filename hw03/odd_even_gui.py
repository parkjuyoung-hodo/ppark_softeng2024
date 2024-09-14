import tkinter as tk
from tkinter import simpledialog, messagebox


def gui_input(text: str) -> str:
    return simpledialog.askstring(title='홀짝 판별', prompt=text)


def is_even(n):
    return n % 2 == 0


def main():
    window = tk.Tk()
    window.withdraw()

    input_num = gui_input("숫자를 입력하세요:")

    n = int(input_num)
    if is_even(n):
        result= f'{n}은 짝수입니다'

        messagebox.showinfo("결과", result)

    else:
        result = f'{n}은 홀수입니다.'


        messagebox.showinfo("결과", result)

    window.destroy()



if __name__ == "__main__":
    main()