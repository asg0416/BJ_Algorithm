def prime_list(num):
    sieve = [True] * num  # 

    m = int(num ** 0.5)
    for i in range(2, m + 1):  # 해당 범위 i 의 배수를 지우겠다.
        if sieve[i] == True:  # i 번째 값이 소수일때
            for j in range(i+i, num, i):  # 그 다음 i의 배수부터 다 false로 지우겠다
                sieve[j] = False

    return [i for i in range(2, num) if sieve[i] == True]


def find_prime(n):
    list = prime_list(n * 2 + 1)  # 2배 한 수도 들어가야해서 + 1 해야함
    count = 0
    for i in list:
        if i > n:
            count += 1
    return count

from sys import stdin
while 1:
    number = int(stdin.readline())
    if number == 0:
        break
    print(find_prime(number))

# from sys import stdin
# while 1:
#     number = int(stdin.readline())
#     if number == 0:
# #         break
#     li = prime_list(2 * number +1)
#     print(len([i for i in li if i > number]))