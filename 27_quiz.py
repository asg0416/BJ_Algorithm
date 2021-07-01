# 중복이 없고 순서가 있는 우측 m개 중 n개를 뽑는 조합 문제 (오른쪽 다리에서 n개 만큼 뽑으면 순서대로 다리가 결정되기 때문)

from sys import stdin

index = int(stdin.readline())

def factorial(num):
    facto = 1
    for i in range(1, num + 1):
        facto *= i

    return facto

for _ in range(index):
    n, m = map(int, stdin.readline().rstrip().split())

    result = factorial(m) / (factorial(n) * factorial(m - n))
    
    print(int(result))
