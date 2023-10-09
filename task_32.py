#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)


def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

arr = [1, 5, 3, 8, 4, 9, 2]
min_val = 3
max_val = 7
print(find_indexes(arr, min_val, max_val))