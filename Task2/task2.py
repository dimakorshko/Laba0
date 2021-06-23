from tkinter import *
import math
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title("Калькулятор")
window.geometry('350x170')

def equally(x):
    str1 = "-+0123456789.*/)("
    if entry.get()[0] not in str1:
        entry.insert(END, "Первый символ не является числом!")
        messagebox.showerror("Error!", "Не введено число!")
    try:
        result = eval(entry.get())
        entry.insert(END, "=" + str(result))
    except:
        entry.insert(END, "Error!")
        messagebox.showerror("Error!", "Введены неверные данные. Проверьте правильность ввода данных")

def func(x):
    try:
        a=entry.get()
        if x=="sin":
            entry.insert(END, "=" + str(math.sin(int(a))))
        elif x=="cos":
            entry.insert(END, "=" + str(math.cos(int(a))))
        elif x=="tan":
            entry.insert(END, "=" + str(math.tan(int(a))))
        elif x=="ctg":
            entry.insert(END, "=" + str(math.cos(int(a))/math.sin(int(a))))
        elif x=="ln":
            entry.insert(END, "=" + str(math.log(int(a))))
        elif x=="log10":
            entry.insert(END, "=" + str(math.log10(int(a))))
        elif x== "C":
            entry.delete(0, END)
        elif x=="⌫":
            entry.delete(len(entry.get())-1)
        elif x=="bin":
            b=[]
            a=int(a)
            while (a>0):
                b.append(a%2)
                a//=2
            c=''.join(str(e) for e in b)[::-1]
            entry.insert(END, "=" + str(c))
        elif x=="%":
            entry.insert(END, "=" + str(int(entry.get())*(int(entry.get())/100)))
        else:
            entry.insert(END, x)
    except:
        messagebox.showerror("Ошибка!", "Проверьте правильность ввода данных!")
    
buttons = [
"7", "8", "9",  "+", "cos", 
"4", "5", "6", "-", "sin",
"1", "2", "3", "*", "tan",
"0", ".", "bin", "/", "ctg",
"(" , ")" , "ln","log10", "%" ,
"C", "⌫", "=",]
r = 1
c = 0
for i in buttons:
       cmd=lambda x=i: func(x)
       if i=="=":
           cmd=lambda x=i: equally(x)
       ttk.Button(window, text=i, command = cmd, width = 10).grid(row=r, column = c)
       c += 1
       if c > 4:
           c = 0
           r += 1
entry = Entry(window, width = 33)
entry.grid(row=0, column=0, columnspan=5)

window.mainloop()
