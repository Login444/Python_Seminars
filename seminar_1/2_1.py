a = int(input('Введите сколько человек учится в классе А: '))
b = int(input('Введите сколько человек учится в классе Б: '))
c = int(input('Введите сколько человек учится в классе В: '))

x = a//2 + b//2 + c//2 + a%2 + b%2 + c%2 # добавляем еще деление с остаток, что мы конечный результат был корректным, т.к. не может быть пол парты
print('Для такого колличества учеников нужно', x, 'парт.')