

n = int(input('enter number'))
n_sum = 0
n_sum += n % 10 
n_sum += n // 10 % 10
n_sum += n // 100
print(n_sum )
