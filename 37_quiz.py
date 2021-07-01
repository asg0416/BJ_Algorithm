from sys import stdin
n = int(stdin.readline())
arr = [0] * 300  # 계단 수가 3보다 작은 경우가 있어서 0으로 초기화 시켜주는 것
for i in range(n):
    arr[i] = int(stdin.readline())


dp = [0] * 300  # 계단 수가 3보다 작은 경우가 있어서 0으로 초기화 시켜주는 것

dp[0] = (arr[0])
dp[1] = (max(arr[1], arr[0] + arr[1]))
dp[2] = (max(arr[1] + arr[2], arr[0] + arr[2]))

for i in range(3, n):  # 맨 마지막으로 append 되는  값이 마지막 계단을 올랐을 때의 최대값
    dp[i] = (max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]))

print(dp[n - 1])  # n번째 계단에 해당하는 값 꺼내기