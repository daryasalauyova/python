n = int(input("Введите кол-во дней: "))
days_plus = 0
max_days_plus = 0
for i in range(n):
    temp = int(input("Введите температуру: "))
    if temp > 0:
        days_plus += 1
        if max_days_plus < days_plus:
            max_days_plus = days_plus
    else:
        days_plus = 0
print(max_days_plus)