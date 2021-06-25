import telebot
import json
import http.client
import sys

Token="1804236666:AAEbfBrlR61OpRGgTVA4pr2qpQL8KebqXIg"
diction=[]
bot = telebot.TeleBot(Token)
jso={}

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
    global jso
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
    return diction

@bot.message_handler(commands=['renew'])
def renew_cmd(message):
    renew()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Данный бот позволяет узнать статистику распостранения COVID-19 в старнах евпропы\n/renew обновит данные\n/search поиск по стране\n/txt вернёт текстовый файл с результатами поиска \n/list покажет список доступнх стран\n/help покажет список всех команд\n/txtreset очищение txt файла")
    global diction
    diction=renew()
    f = open('text.txt', 'w')
    f.write("")
    f.close()
    return diction

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"/renew обновит данные\n/search поиск по стране\n/txt вернёт текстовый файл с результатами \n/list покажет список доступнх стран\n/help покажет список всех команд\n/txtreset очищение txt файла")

@bot.message_handler(commands=['list'])
def list_of_countr(message):
    c_list=[]
    clist=""
    i=0
    for item in jso:
        c_list.append(item["Country"])
        clist+=str(c_list[i]) + "\n"
        i+=1
    bot.send_message(message.chat.id, clist)

@bot.message_handler(commands=['search'])
def search(message):
    chat_id = message.chat.id
    country = message.text
    msg = bot.send_message(chat_id, 'Введите страну')
    bot.register_next_step_handler(msg, countr)
    return country
    
def countr(message):
    chat_id = message.chat.id
    country = message.text
    country=searching(country)
    msg = bot.send_message(chat_id, country)
    if country=="Ошибка! Такой страны нет или она не сущевствует":
        country=""
    f = open('text.txt', 'a')
    f.write(str(country))
    f.close()

def searching(country):
    global diction
    search=str(country)
    if search not in diction:
        country="Ошибка! Такой страны нет или она не сущевствует"
    for i in range(len(diction)):
        if diction[i]==search:
            country="Страна:" + diction[i] + "\n"
            country+="Кол-во заболевших:" + str(diction[i+1]) + "\n"
            country+="Новых заболевших:" + str(diction[i+2]) + "\n"
            country+="Кол-во смертей:" + str(diction[i+3]) + "\n"
            country+="Новых смертей:" + str(diction[i+4]) + "\n"
            country+="Выздоровевших:" + str(diction[i+5]) + "\n"
            country+="Новых выздоровевших:" + str(diction[i+6]) + "\n"
            country+="---------------------------------\n"
    return country

@bot.message_handler(commands=['txt'])
def txt(message):
    try:
        file = open('text.txt', 'r')
        bot.send_document(message.chat.id, file)
        file.close()
    except:
        bot.send_message(message.chat.id, "Ошибка! Вы не производили поиск, поэтому текстовый файл пуст!")

@bot.message_handler(commands=['txtreset'])
def txtreset(message):
    f = open('text.txt', 'w')
    f.write("")
    f.close()
    bot.send_message(message.chat.id, "Текстовый файл теперь пуст!")

bot.polling(none_stop=True)
