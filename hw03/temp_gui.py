import tkinter as tk
from tkinter import messagebox

def f_to_c():
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    messagebox.showinfo("변환 결과", f"{round(celsius, 2)} \N{DEGREE CELSIUS}")

def c_to_f():
    celsius = ent_temperature.get()
    fahrenheit = (9 / 5) * float(celsius) + 32
    messagebox.showinfo("변환 결과", f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}")

window = tk.Tk()
window.title("단위 변환")
window.resizable(width=False, height=False)

window.geometry("250x100")

frm_entry = tk.Frame(master=window)
lbl_temp = tk.Label(master=frm_entry, text="온도를 입력해주세요: ")
ent_temperature = tk.Entry(master=frm_entry, width=10)

lbl_temp.grid(row=0, column=0, sticky="e")
ent_temperature.grid(row=0, column=1, sticky="w")

btn_convert_f_to_c = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW} F to C",
    command=f_to_c
)

btn_convert_c_to_f = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW} C to F",
    command=c_to_f
)

frm_entry.grid(row=0, column=0, padx=10)
btn_convert_f_to_c.grid(row=1, column=0, pady=5)
btn_convert_c_to_f.grid(row=2, column=0, pady=5)

window.mainloop()