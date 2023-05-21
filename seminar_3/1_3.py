# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

numbers = [input ('Введите число: ') for i in range(6)]
print(len(set(numbers)))