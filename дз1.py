name = (input("Как тебя зовут?"))
print('Привет', name)
age = int(input("Сколько тебе лет?"))
if age<45:
    print("О ты еще молод)")
else:
    print("Ты уже повидал жизнь)")






n = int(input("введи любое число: "))
r = n+(n ** 2)+(n ** 3)
print(r)






a = int(input("Введите целое положительное число"))
b = a%10
c = a//10
while c > 0:
    if c%10 > b:
        b = c%10
    c = c//10
print(b)








v = int(input("Какова выручка фирмы?"))
i = int(input("Каковы затраты фирмы?"))
d = v - i
r = d / v
if v > i:
    print("Фирма работает в плюс)")
    print("Вот рентабельность фирмы", r, "%")
elif i > v:
    print("Фирма работает в минус")
s = int(input("Сколько сотрудников работает в фирме?"))
g = d/s
print("Вот расчет прибыли на одного сотрудника", g)








print("Введите результат в первый день:")
a = int(input())
print("Введите требуемый результат:")
b = int(input())
c = a
d = 1
while c <= b:
    d = d+1
    c = 1.1*c
print("Day = ", d, end = '')