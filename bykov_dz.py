
#name = input("Введите имя: ") # знакомство
#print('hello ' + name)

#age = input('Ваш возраст: ') # блок работы с типами данных, первая задача
#year = input('Год рождения: ')
#print(type(age))
#print(age + year)
#age_n = int(age)
#print(type(age_n))
#year_n = int(year)
#print(age_n + year_n)

#number = int(input(" Введите число: ")) # третья задача3
#n = number * (1 + 11 + 111)
#print(n)

#a = int(input(" Введите число: a=")) # седьмая задача 7
#b = int(input(" Введите число: b="))
#day = 0
#while a <= b:
    #a = 0.1 * a + a
    #day = day + 1
    #print(day, a)

#a = int(input(" Введите сумму выручки: ")) # задача 5,6
#b = int(input(" Введите суму издержек: "))
#if a - b < 0:
        #print('убыток')
#else:
        #print('прибыль')
        #iz = a / b
        #print('издержки= ', iz)
        #rab = int(input(" Введите количество сотрудников: "))
        #dohod = (a - b) // rab
        #print('доход на человека= ', dohod)

a = int(input(" Введите количество секунд: ")) # вторая задача
h = a // 3600
m = a % 3600 // 60
s = a % 3600 % 60
print('часы', h, 'минуты', m, 'секунды', s)

print('godbye')