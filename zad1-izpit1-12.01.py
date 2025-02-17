n = 10
list_10 = []

try:
    for num in range(n):
        num = int(input())
        if num > 0:
            list_10.append(num)
        else:
            raise ValueError("num must be positive")
        break
except ValueError as e:
    print(f"Error: {e}")

odd_number = []
for num in list_10:
    if num % 2 != 0:
        odd_number.append(num)

print(len(odd_number))

average = sum(list_10)/len(list_10)
print(average)

# list_5 = []
# list_10.sort(reverse=True)
# for num in list_10:
#     if num % 2 == 0:
#         for i in range(5):
#             num = list_10[i]
#             list_5.append(num)

list_5 = []
list_10_5 = []
for num in list_10:
    if num % 2 == 0:
        list_10_5.append(num)
list_10_5.sort(reverse=True)
for i in range(5):
    num = list_10_5[i]
    list_5.append(num)

list_5.sort(reverse=True)

list_even = []
for i in range(len(list_5)):
    num = list_5[i]
    index_num = i
    if index_num % 2 == 0:
        list_even.append(num)

for num in list_even:
    list_5.remove(num)