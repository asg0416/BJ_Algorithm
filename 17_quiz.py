from sys import stdin

number = int(stdin.readline())

def make_room():
    H, W, N = map(int, input().split())

    if N % H == 0:
        y = str(H)
        x = str(N // H)
    else:
        y = str(N % H)
        x = str(N // H + 1)

    if len(x) == 1:
        result = y + x.zfill(2)
    else:
        result = y + x

    return result

for i in range(number):
    print(make_room())