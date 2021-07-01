from sys import stdin
import statistics

n = int(stdin.readline())

num = [int(stdin.readline().rstrip()) for _ in range(n)]
num.sort()

mean = statistics.mean(num)

median = statistics.median(num)

mode = statistics.multimode(num)
if len(mode) > 1:
    mode = mode[1]
else:
    mode = mode[0]


range = num[-1] - num[0]

print(round(mean), median, mode, range, sep='\n')