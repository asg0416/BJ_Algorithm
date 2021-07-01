from sys import stdin

n = int(stdin.readline())
stack = []

for _ in range(n):
    cmd_list = stdin.readline().rstrip().split()

    cmd = cmd_list[0]

    if cmd == 'push':
       stack.append(cmd_list[1])
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])