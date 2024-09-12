#1-100까지 짝수의 합 구하기
import tkinter as tk
from tkinter import simpledialog, messagebox
from hw_03.hw_03_1 import is_even


# GUI 입력 함수
def gui_input(text: str) -> str:
    return simpledialog.askstring(title='숫자 입력', prompt=text)



# 메인 함수
def main():
    window = tk.Tk()
    window.withdraw()  # 기본 창 숨기기
    input_num = gui_input("1부터 100까지 짝수의 합은?")
    n = int(input_num)

    # 숫자 입력받기

    total = 0

    for i in range(1, 100):
        if is_even(i):
            total += i


    if n == 2450:
        result = f"정답입니다!"

    else:
        result = f"틀렸습니다! 정답은 {total}입니다"


            # 결과 출력
    messagebox.showinfo("결과", result)


    window.destroy()  # 사용 후 창 닫기


if __name__ == "__main__":
    main()
