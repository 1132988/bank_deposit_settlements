#Стандартный вклад в банке, под свои параметры
import matplotlib.pyplot as plt
s = int(input("Сумма вклада: "))
m = int(input("Количество месяцев: "))
p = int(input("Количество процентов годовых: "))
months = []
sums = []

for i in range(1, m+1):
    s = (s * p/100/12) + s
    months.append(i)
    sums.append(s)
    print('Сумма на ', i, 'месяц = ', s)
    s=s//1
print('Общая сумма: ', s)

plt.plot(months, sums)
plt.xlabel('Месяцы')
plt.ylabel('Сумма на вкладе')
plt.title('Динамика изменения суммы вклада')
plt.show()
