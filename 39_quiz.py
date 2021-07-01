from sys import stdin

n, m = map(int, stdin.readline().strip().split())
cards_num = list(map(int, stdin.readline().strip().split()))
result_guess = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_g = cards_num[i] + cards_num[j] + cards_num[k]
            if sum_g <= m:
                result_guess.append(sum_g)
print(max(result_guess))
