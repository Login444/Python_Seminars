# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.

list_a = [int(input(f'Введите {i+1}-й элемент: ')) for i in range (int(input('Введите N: ')))]

# list_b = [i for i in range(1,len(list_a)-1) if list_a[i-1]<list_a[i] and list_a[i+1]<list_a[i]]
list_b = [i for i in range(1,len(list_a)-1) if list_a[i-1] < list_a[i] > list_a[i+1]]
print(len(list_b))
