from sys import stdin
import math

n = int(stdin.readline())


def lcm(a, b):  # 최소공배수는 두수의 곱 나누기 최대공약수
    return int(a * b / math.gcd(a, b))  #최대공약수 구하는 함수 있음...ㅋㅋ

for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split())

    print(lcm(a, b))