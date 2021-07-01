n = int(input())
divisor_list = list(map(int, input().split()))

number = 1
for num in divisor_list:
    number *= num

real_num = (number ** 2) ** (1/n)

print(round(real_num))  # 제곱근 계산하면 정확히 정수로 나누어 떨어지지 않는 경우 있어서 반올림해야함. 예로 16찾을때 4096의 세제곱근은 15.999999 임....