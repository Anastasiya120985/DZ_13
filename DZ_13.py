# Два списка целых заполняются случайными числами. Необходимо:
# 1. Сформировать третий список, содержащий элементы обоих списков;
# 2. Сформировать третий список, содержащий элементы обоих списков без повторений;
# 3. Сформировать третий список, содержащий элементы общие для двух списков;
# 4. Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# 5. Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков

import random
lst_1 = [random.randrange(0, 30) for i in range(10)]
lst_2 = [random.randrange(0, 30) for i in range(10)]

print(*lst_1)
print(*lst_2)

lst_3_1 = [i for i in lst_1] + [j for j in lst_2]
print(f'1. Элементы обоих списков:')
print(*lst_3_1)

lst_3_2 = [i for i in lst_1 if not (i in lst_2)] + [j for j in lst_2 if not (j in lst_1)]
print(f'2. Элементы обоих списков без повторений:')
print(*lst_3_2)

lst_3_3 = [i for i in lst_1 if i in lst_2]
print(f'3. Элементы общие для двух списков:')
print(*lst_3_3)

lst_3_4 = [i for i in lst_1 if lst_1.count(i) == 1] + [j for j in lst_2 if lst_2.count(j) == 1]
print(f'4. Уникальные элементы каждого из списков:')
print(*lst_3_4)

lst_3_5 = []
max_1 = lst_1[0]
max_2 = lst_2[0]
min_1 = lst_1[0]
min_2 = lst_2[0]
for i in lst_1:
    if i > max_1:
        max_1 = i
    if i < min_1:
        min_1 = i
for i in lst_2:
    if i > max_2:
        max_2 = i
    if i < min_2:
        min_2 = i
lst_3_5 = [min_1, min_2, max_1, max_2]
print(f'5. Минимальное и максимальное значение каждого из списков:')
print(*lst_3_5)