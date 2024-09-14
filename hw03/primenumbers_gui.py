import tkinter as tk
from tkinter import simpledialog, messagebox


def gui_input(text: str) -> str:
    return simpledialog.askstring(title='소수 구하기', prompt=text)


def primenumbers(n: int):
    primenums = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primenums.append(num)
    return primenums


def main():
    window = tk.Tk()
    window.withdraw()

    input_num = gui_input("2부터 입력한 숫자 사이의 소수를 구하고 싶은 숫자를 입력해주세요.")

    n = int(input_num)
    primenums = primenumbers(n)

    result = f'{n}까지의 소수: {primenums}'

    messagebox.showinfo("결과", result)

if __name__=="__main__":
    main()