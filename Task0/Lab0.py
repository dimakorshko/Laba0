import random
random.seed()

my_list=[]
my_list2=[]
index=0
n_index=0
biggest=-101

for i in range(30):
    my_list.append(random.randint(-100, 100))
print("Первый список: \n", my_list)

for number in my_list:
    index+=1
    if number>biggest:
        biggest=number
        n_index=index
print("Найбольшее число =", biggest, ". Его порядковый номер =" , n_index)

for i in range(len(my_list)):
    if my_list[i]%2!=0:
        my_list2.append(my_list[i])
my_list2.sort(reverse=True)
print("Список с нечетными числами в порядке убывания: \n", my_list2)
