#Проценты начисляются каждый день
s=int(input("Сумма вклада: "))
d=int(input("Количество дней: "))
p=int(input("Количество процентов годовых: "))
for i in range(1, d+1):
    s=((s * p/100)/12/30) + s #расчёт суммы с набежавшими процентами каждый день
    print('Сумма на ', i, 'в день = ', s)
    s=s//1
print("Общая сумма", s)