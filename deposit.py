#Стандартный вклад в банке, под свои параметры
s=int(input("Сумма вклада: "))
m=int(input("Количество месяцев: "))
p=int(input("Количество процентов годовых: "))
for i in range(1, m+1):
    s=(s * p/100/12) + s #расчёт суммы с набежавшими процентами каждый месяц
    print('Сумма на ', i, 'месяц = ', s)
    s=s//1
print("Общая сумма", s)




