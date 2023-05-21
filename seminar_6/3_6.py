list = [int(input(f'Введите {i+1}-й элемент списка: ')) for i in range(int(input('Введите колличество элементов списка: ')))]

def pair_list(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j]==a[i]:
                count +=1
    return count

print(f'В получившемся списке всего {pair_list(list)} пар чисел')


# list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
# count = [list_n[i] for i in range(len(list_n)) for j in range(i + 1, len(list_n)) if list_n[j] == list_n[i]]
# print(count, len(count))