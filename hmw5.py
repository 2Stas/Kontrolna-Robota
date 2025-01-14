import random

#Завдання 1
expression = input("Введіть арифметичний вираз (наприклад, 23+12): ")


if '+' in expression:
    num1, num2 = expression.split('+')
    result = int(num1) + int(num2)

elif '-' in expression:
    num1, num2 = expression.split('-')
    result = int(num1) - int(num2)

elif '*' in expression:
    num1, num2 = expression.split('*')
    result = int(num1) * int(num2)

elif '/' in expression:
    num1, num2 = expression.split('/')

    if int(num2) != 0:
        result = int(num1) / int(num2)
    else:
        result = "Помилка: ділення на нуль!"
else:
    result = "Не правильний вираз!"

print(f"Результат виразу {expression} = {result}\n\n")

#Завдання 2

numbers = [random.randint(-10, 10) for i in range(20)]

min_num = min(numbers)
max_num = max(numbers)

negative_c = len([num for num in numbers if num < 0])
positive_c = len([num for num in numbers if num > 0])
zero_c = len([num for num in numbers if num == 0])

print(f"Список чисел: {numbers}")
print(f"Мінімальний елемент: {min_num}")
print(f"Максимальний елемент: {max_num}")
print(f"Кількість від'ємних елементів: {negative_c}")
print(f"Кількість додатних елементів: {positive_c}")
print(f"Кількість нулів: {zero_c}")
