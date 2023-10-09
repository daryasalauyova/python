n = int(input("Введите число: "))
result = 1
while n > 1:
    print(result, '*', n)
    result *= n
    n -= 1
print(result)