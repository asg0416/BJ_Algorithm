import math
ind = int(input())
# 근의 공식
# c 는 나중에 입력값 차
def answer_n(c):
    return (-1 + math.sqrt(1+4*c))/2


def find_count(c):
    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
    if c == num ** 2:
        count = num * 2 - 1
    elif answer_n(c) <= num:
        count = num * 2
    else:
        count = num * 2 + 1
    
    return count
    

for i in range(ind):
    a, b = map(int, input().split())
    c = b - a
    print(find_count(c))



# import math
# ind = int(input())
# # 근의 공식
# # c 는 나중에 입력값 차
# def answer_n(c):
#     return (-1 + math.sqrt(1+4*c))/2


# def find_count(c):
#     count = 0
#     mid = math.trunc(answer_n(c) * 10)
#     num = mid / 10
#     if math.trunc(num) < num <= math.trunc(num) + 0.5:
#         count = 2 * math.trunc(num) + 1
#     elif num == 1:
#         count = 1
#     else:
#         count = 2 * round(num) + 2

#     return count

# for i in range(ind):
#     a, b = map(int, input().split())
#     c = b - a
#     print(find_count(c))