#  Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

def Fibonacci(number):
    if number == 1 or number == 2:
        return 1
    else:
        return Fibonacci(number - 1) + Fibonacci(number - 2)

num = int(input('введите числo => '))
answer = list()
for i in range(1, num + 1):
    answer.append(Fibonacci(i)*((-1)**(i+1)))
answer.reverse()
answer.append(0)
for i in range(1, num + 1):
    answer.append(Fibonacci(i))
print(*answer)