import tkinter as tk
from tkinter import simpledialog, messagebox


def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def gui_input(text: str) -> str:
    return simpledialog.askstring(title='팩토리얼', prompt=text)


def main():
    window = tk.Tk()
    window.withdraw()

    input_num = gui_input("팩토리얼을 구할 숫자를 입력하세요:")

    n = int(input_num)
    if n >= 0:
        result = factorial(n)
        messagebox.showinfo("결과", f"{n}! = {result} 입니다.")
    else:
        messagebox.showwarning("결과", "자연수를 입력해주세요.")


if __name__ == "__main__":
    main()