import random

random_number = [random.randint(0, 20) 
                 for _ in range(10)]

sorted_number = sorted(random_number)

min_namber = min(random_number)
max_namber = max(random_number)

sum_number=0
for number in random_number:
    sum_number= sum_number + number

print("Список случайных чисел:",random_number)
print("Сортировка случайных чисел:",sorted_number)
print("Список случайных чисел минимальные:",min_namber)
print("Список случайных чисел максимальные:",max_namber)
print("Сумма списка случайных чисел:",sum_number)