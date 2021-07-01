from sys import stdin

n = int(stdin.readline())

stack = []

for _ in range(n):
    num = int(stdin.readline())

    if num != 0:
        stack.append(num)
    else:
        stack.pop()

sum = sum(stack)
print(sum)