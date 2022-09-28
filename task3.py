# Задайте список из вещественных чисел. Напишите программу, которая найдёт   
# разницу между максимальным и минимальным значением дробной части элементов.

inp = list(map(float, input('введите числа => ').split()))
answer = list()
for i in inp:
    x = i - int(i)
    if x != 0:
        answer.append(round(x, 5))
if max(answer) == min(answer):
    print(max(answer))
else:
    print(max(answer) - min(answer))