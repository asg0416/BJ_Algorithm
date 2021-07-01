from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())

def multiply(list):
    result = 1
    for i in range(len(list)):
        result *= list[i]

    return result

if k != 0:
    temp = set(range(1, n - k + 1))
    n = set(range(1,n + 1))
    k = set(range(1, k + 1))

    son = multiply(list(n - temp))
    mom = multiply(list(k))

    print(int(son/mom))

else:
    print(1)


