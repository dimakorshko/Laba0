import http.client
import json
from tkinter import *
from tkinter import Tk, Button
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title("CovidStats")
window.geometry('820x1080')
window.config(bg="white")

text_1 = Text(window, height=45, width = 33)
text_1.grid(row=0, column=0, columnspan=5)
entry = Entry(window, text="Поиск" ,width = 45)
entry.place(x=270, y=720)
entry.config(bg="#e9e9e9")

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "7c7462f4ecmshdbacb80693620b0p1ac60ejsna3ea048a05c5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
corona = data.decode("utf-8")
jso = json.loads(corona)

diction=[]
for item in jso:
    diction.append(item["Country"])
    diction.append(item["TotalCases"])
    diction.append(item["NewCases"])
    diction.append(item["TotalDeaths"])
    diction.append(item["NewDeaths"])
    diction.append(item["TotalRecovered"])
    diction.append(item["NewRecovered"])

#Вывод 5-и стран
def output(diction):
    text_1.delete("1.0","end")
    for i in range(len(diction)):
        if diction[i]=="France":
            textinsert="Страна:" + diction[i] + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых заболевших:" + str(diction[i+2]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во смертей:" + str(diction[i+3]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых смертей:" + str(diction[i+4]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Выздоровевших:" + str(diction[i+5]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="---------------------------------\n"
            text_1.insert(END, textinsert)
        elif diction[i]=="Russia":
            textinsert="Страна:" + diction[i] + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых заболевших:" + str(diction[i+2]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во смертей:" + str(diction[i+3]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых смертей:" + str(diction[i+4]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Выздоровевших:" + str(diction[i+5]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="---------------------------------\n"
            text_1.insert(END, textinsert)
        elif diction[i]=="Sweden":
            textinsert="Страна:" + diction[i] + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых заболевших:" + str(diction[i+2]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во смертей:" + str(diction[i+3]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых смертей:" + str(diction[i+4]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Выздоровевших:" + str(diction[i+5]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="---------------------------------\n"
            text_1.insert(END, textinsert)
        elif diction[i]=="Hungary":
            textinsert="Страна:" + diction[i] + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых заболевших:" + str(diction[i+2]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во смертей:" + str(diction[i+3]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых смертей:" + str(diction[i+4]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Выздоровевших:" + str(diction[i+5]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="---------------------------------\n"
            text_1.insert(END, textinsert)
        elif diction[i]=="Spain":
            textinsert="Страна:" + diction[i] + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых заболевших:" + str(diction[i+2]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Кол-во смертей:" + str(diction[i+3]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых смертей:" + str(diction[i+4]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Выздоровевших:" + str(diction[i+5]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            text_1.insert(END, textinsert)
            textinsert="---------------------------------\n"
            text_1.insert(END, textinsert)
#Обновление информации
def renew():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "7c7462f4ecmshdbacb80693620b0p1ac60ejsna3ea048a05c5",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    corona = data.decode("utf-8")
    jso = json.loads(corona)
    diction_new=[]
    for item in jso:
        diction_new.append(item["Country"])
        diction_new.append(item["TotalCases"])
        diction_new.append(item["NewCases"])
        diction_new.append(item["TotalDeaths"])
        diction_new.append(item["NewDeaths"])
        diction_new.append(item["TotalRecovered"])
        diction_new.append(item["NewRecovered"])
    output(diction_new)
    answer = messagebox.showinfo(
        title="Обновление", 
        message="Данные обновлены")
    

#Поиск
def searching():
    search=str(entry.get())
    if search not in diction:
        messagebox.showerror("Ошибка!", "Проверьте правильность ввода данных!")
    txt=Text(window,height=40,width = 33)
    txt.place(x=270, y=0)
    for i in range(len(diction)):
        if diction[i]==search:
            textinsert="Страна:" + diction[i] + "\n"
            txt.insert(END, textinsert)
            textinsert="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            txt.insert(END, textinsert)
            textinsert="Новых заболевших:" + str(diction[i+2]) + "\n"
            txt.insert(END, textinsert)
            textinsert="Кол-во смертей:" + str(diction[i+3]) + "\n"
            txt.insert(END, textinsert)
            textinsert="Новых смертей:" + str(diction[i+4]) + "\n"
            txt.insert(END, textinsert)
            textinsert="Выздоровевших:" + str(diction[i+5]) + "\n"
            txt.insert(END, textinsert)
            textinsert="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            txt.insert(END, textinsert)
            textinsert="---------------------------------\n"
            txt.insert(END, textinsert)

cmd=lambda: renew()
Button_1=Button(window, text="Обновить", command = cmd, width = 10)
Button_1.place(x=90, y=750)

cmd=lambda: searching()
Button_2=Button(window, text="Найти", command = cmd, width = 10)
Button_2.place(x=360 , y=750)

output(diction)

text=Text(window,height=50, width=35)
text.place(x=541, y=0)
text.insert(END, "Список стран доступных для поиска:\n")
for item in jso:
    inserttetx=item["Country"]+"\n"
    text.insert(END, inserttetx)

window.mainloop()

