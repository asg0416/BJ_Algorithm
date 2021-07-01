# 덱 사용 = deque

from sys import stdin
from collections import deque

deq = deque()
n = int(stdin.readline())
count = 0

for _ in range(n):
    cmd = stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        count += 1
        deq.append(cmd[1])
    elif cmd[0] == 'pop':
        if count == 0:
            print(-1)
        else:
            count -= 1
            print(deq.popleft())
    elif cmd[0] == 'size':
        print(count)
    elif cmd[0] == 'empty':
        if count == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if count == 0:
            print(-1)
        else:
            print(deq[0])  # deq = dequeue() 여기서 () 안에 리스트가 들어갈 수도 있고 그냥 쓰면 문자열 형태로 들어감 그래서 deq[0] 이렇게 쓸수있는 것
    elif cmd[0] == 'back':
        if count == 0:
            print(-1)
        else:
            print(deq[-1]) 