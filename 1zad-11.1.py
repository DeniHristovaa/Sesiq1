import random

list1 = []
try:
    n = int(input())
    if n < 20 or n > 80:
        raise ValueError("n is not valid")
except ValueError as e:
    print(f"Error: {e}")

for i in range(n):
    num = random.randint(-800, 1001)
    list1.append(num)

lists = []
for num in list1:
    if num > 99 or num < -99:
        s = num // 100
        s = s % 10
        if s % 3 == 0:
            lists.append(num)

print(len(lists))

negative_max = None
index_negative = None
for i in list1:
    num = list1[i]
    if num < 0:
        if negative_max is None or negative_max < num:
            negative_max = num
            index_negative = i
print(f"Max odd number's index is {index_negative}")

# 2
# max_negative = max(l for l in list1 if l < 0)
# index_negative1 = list1.index(max_negative)
# print(index_negative1)

even_min = None
index_even = None
for i in list1:
    num = list1[i]
    if num is None or even_min > num:
        even_min = num
        index_even = i
print(f"Min even number's index is {index_even}")

list2 = [num for num in list1 if num % 7 == 0 and num % 2 != 0]

even_index_element = [list1[i] for i in range(0, len(list1), 2)]
average = sum(even_index_element) / len(even_index_element)
print(average)

for i in range(len(list2)):
    num = list2[i]
    if num > -9 and num < -100:
        print(num)

max_negative = None
for i in list2:
    num = list2[i]
    if num < 0:
        if max_negative is None or max_negative < num:
            max_negative = num

list.remove(max_negative)


