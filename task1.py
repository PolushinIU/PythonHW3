# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

inp = list(map(int, input('введите числа => ').split()))
sum = 0
for i in range(1, len(inp), 2):
    sum += inp[i]
print(sum)