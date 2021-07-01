a, b = map(int, input().split())

def gcd(a, b):  # 최대공약수
    r = a % b
    while True:
        if r != 0:
            new_b = r  # b에 1번 나머지를 대입해야해서 나머지가 바뀌기전에 잠깐 저장해 둠
            r = b % r  # 새롭게 위에서 나온 나머지 = new b를 나눠줄 2번째 나머지를 구함
            b = new_b  # b에 1번 나머지를 대입해주고 과정을 반복시킴
        else:
            result = b
            break
    return result


def lcm(a, b):  # 최소공배수는 두수의 곱 나누기 최대공약수
    return int(a * b / gcd(a, b))

print(gcd(a, b), lcm(a, b), sep='\n')