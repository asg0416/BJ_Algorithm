N = int(input())

index = N // 3 + 1  # 최대 이동 횟수 범위

sum_list = []
for i in range(index):  # 이동 횟수 시도
    mid = 3 * i  # 3kg 가 최소 몇번 필요할지
    if (N - mid) % 5 == 0:  
        x = i
        y = (N - mid) // 5
        sum_list.append(x + y)

if len(sum_list) >= 1:
    min_num = sum_list[0]
    for num in sum_list:
        if num < min_num:
            min_num = num
else:
    min_num = -1

print(min_num)