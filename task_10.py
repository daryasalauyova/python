# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input())
coins = input().split()
heads = coins.count('1')
tails = n - heads
if heads <= tails:
    flips = heads
    new_coins = ['1']*heads + ['0']*tails
else:
    flips = tails
    new_coins = ['0']*tails + ['1']*heads
print(flips)