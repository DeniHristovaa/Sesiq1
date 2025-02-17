from operator import index

try:
    n = int(input())
    if n < 15 or n > 35:
        raise ValueError("n must be in interval")
except ValueError as e:
    print(f"Error: {e}")

list1 = []

try:
    for i in range(n):
        num = int(input())
        if num < 30 or num > 300:
            raise ValueError("num must be in interval")
        else:
            list1.append(num)
except ValueError as e:
    print(f"Error: {e}")

list_des = []
for num in list1:
    dd = (num // 10) % 10
    if dd % 3 == 0:
        list_des.append(num)

print(len(list_des))
print(list_des)

listm = []
for num in list1:
    if num % 6 == 4:
        print(list1.index(num))

min_num = None
min_index = None
for i in range(n):
    num = list1[i]
    if min_num is None or num < min_num:
        min_num = num
        min_index = i
print(f"Min index is {min_index}.")

list2 = [num for num in list1 if num > 29 or num < 100 and num % 2 == 0 or num % 3 == 0]

# for num in list2:
#     sum = 0
#     if index(num) % 2 != 0:
#         sum += num
#     sa = sum / len(index(num) % 2 != 0)

odd_index_elements = [list2[i] for i in range(1, len(list2), 2)]
average =sum(odd_index_elements) / len(odd_index_elements)
print(average)

even = [num for num in list2 if num % 2 == 0]
print(min(even))

