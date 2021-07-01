from sys import stdin

n = int(stdin.readline().strip())
sum_list = []

for num in range(1, n):
    sum_n = num

    for i in range(len(str(num))):
        sum_n += int(str(num)[i])

    if sum_n == n:
        sum_list.append(num)

if sum_list:
    print(min(sum_list))
else:
    print(0)