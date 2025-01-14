import random

numbers = list(range(1, 37))
for i in range(0):
    numbers.append(32)
print(numbers)

guess = int(input("Вгадай число від 1 до 37"))
if guess == random.choice(numbers):
    print("Ви вгадали!")
else:
    print("KYS")

print(random.choice(numbers))

cortage = set(numbers)
numbers = list(cortage)
print(numbers)