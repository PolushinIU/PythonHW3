# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

inp = list(map(int, input('введите числа => ').split()))
answer = list()
for i in range(len(inp) // 2):
    answer.append(inp[i] * inp[len(inp) - i - 1])
if len(inp) % 2 == 1:
    answer.append(inp[int (len(inp) / 2)] ** 2)
print(*answer)
