from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().strip().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    R = [r, r1, r2]
    max_r = max(R)
    R.remove(max_r)
    if r == 0 and r1 == r2:
        print(-1)
    elif max_r > sum(R):
        print(0)
    elif max_r == sum(R):
        print(1)
    else:
        print(2)