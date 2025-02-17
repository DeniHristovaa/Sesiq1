import random

while True:
    try:
        n = int(input())
        if n < 20 or n > 30:
            raise ValueError("n must be in interval")
        break
    except ValueError as e:
        print(f"Error: {e}")

list_n = []
for i in range(n):
    num = random.randint(-100,100)
    list_n.append(num)

odd_list = []
for i in range(len(list_n)):
    num = list_n[i]
    index_num = i
    if index_num % 2 != 0:
        odd_list.append(num)
print(sum(odd_list))

ed_list = []
for num in list_n:
    ed = num % 10
    if ed % 2 == 0:
        ed_list.append(num)
print(len(ed_list))

# odd_listt = []
result = 1
for num in list_n:
    if num < 0 and num % 2 == 0:
        num *= result
#         odd_listt.append(num)
# for num in odd_listt:
#     result = 1
print(result)

list_n.sort(reverse=True)
print(list_n)

list_2 = [num for num in list_n if num > n]

result = max(list_2) - min(list_2)

odd_list2 = []
for num in list_2:
    if num % 2 != 0:
        odd_list2.append(num)
print(odd_list2)
print(len(odd_list2))

min_num = min(list_2)
list_2.remove(min_num)