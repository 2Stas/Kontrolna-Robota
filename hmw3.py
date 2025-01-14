import random

list1 = [random.randint(1, 100) for i in range(10)]
list2 = [random.randint(1, 100) for i in range(10)]

print("Список 1:", list1)
print("Список 2:", list2)


list3_1 = list1 + list2
print("Список 3 (всі елементи обох списків):", list3_1)


list3_2 = list(set(list1 + list2))
print("Список 3 (без повторів):", list3_2)


list3_3 = list(set(list1) & set(list2))
print("Список 3 (спільні елементи):", list3_3)


list3_4 = list(set(list1) - set(list2)) + list(set(list2) - set(list1))
print("Список 3 (унікальні елементи кожного списку):", list3_4)


list3_4 = [min(list1), max(list1), min(list2), max(list2)]
print("Список 3 (мінімальне та максимальне значення кожного списку):", list3_4)
