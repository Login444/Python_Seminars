# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

list = [1, 2, 3, 4, 5]
# count=0
# for i in range(1, len(list)-1):
#     if list[i]<list[i+1]:
#         count +=1
# print(count)

res = [list[i]>list[i-1] for i in range(1, len(list)-1)]
print(sum(res))