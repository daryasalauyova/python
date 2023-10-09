n = int(input("Введите кол-во арбузов: "))
x = int(input("Введите массу арбуза: "))
min_massa = x
max_massa = x
for i in range(n - 1):
    x = int(input("Введите массу арбуза: "))
    if min_massa > x:
        min_massa = x
    elif max_massa < x:
        max_massa = x
print(min_massa, max_massa)