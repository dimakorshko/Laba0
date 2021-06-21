# Task 1
<br>Копіюємо файли:
<br>![image](https://user-images.githubusercontent.com/85683259/122770282-f9f9b980-d2ad-11eb-85f0-00290cfc5fd2.png)
<br>Переміщуємо файли до потрібних папок, та додаємо зміни в коміт. Перевіряємо за допомогою git status:
<br>![Screenshot_155](https://user-images.githubusercontent.com/85683259/122770669-5a88f680-d2ae-11eb-94df-79e4adbbd741.jpg)
<br>Виконуємо команду git commit та завантажуємо на сервер за допомогою команди push:
<br>![Screenshot_156](https://user-images.githubusercontent.com/85683259/122771167-dbe08900-d2ae-11eb-8902-bb000f7cba25.jpg)
<br>![Screenshot_157](https://user-images.githubusercontent.com/85683259/122771207-e3a02d80-d2ae-11eb-8009-2c648f6d1c9f.jpg)

<h1>Опис проекту:</h1>
        
<br>Завдання:
 
<br>Створити програму
<br>1 Яка на вхід приймає рядок 
<br>2 Та виділяє з нього всі числа в окремий масив, після чого програма друкує рядок без чисел і
масив чисел. 
<br>3 Змінити цей рядок таким чином, щоб кожне слово в ньому,
починалось і закінчувалось великою літерою. 
<br>4 Знайти максимальне значення в масиві чисел, а всі інші числа піднести до степеню по їх
індексу, та записати в інший масив.

<br>Пункт 1:
<pre>def input_line():
    line_1=input("Input your line:")
    return line_1</pre>
        
<br>Пункт 2:
<pre>numbers = re.findall(r"\d+", line)
numbers=[int(i) for i in numbers]
line=re.findall("\D", line)
line_2="".join(line)</pre>

Пункт 3:
<pre>def upper_first_and_last(line_for_upper):
    try:
        line_for_upper= line_for_upper.capitalize()
        line_for_upper = line_for_upper[:-1] + line_for_upper[-1].upper()
        return line_for_upper
    except:
        print("Невозможно вывести первую и последню букву в верхнем регистре, вы не ввели буквы в строку")</pre>
        
<br>Пункт 4:
<pre>def max_number(numbers_list):
    numbers_list_2=[]
    try:
        max_num=max(numbers_list)
        print("Максимальное число:", max_num)
        for i in range(len(numbers_list)):
            x=numbers_list[i]
            if(x!= max_num):
            numbers_list_2.append(x**i)
            else:
                continue
        print("Остальные числа возведенные в степень:",numbers_list_2)
    except:
        print("Максимальное число не может быть найдено, вы не ввели числа в строку")</pre>
