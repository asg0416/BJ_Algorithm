# PyPy3 으로는 맞다고 나옴
from sys import stdin

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, data):
        new_data = Node(data)
        self.len += 1
        
        if self.head == None:
            self.head = new_data
            self.tail = new_data
        else:
            self.tail.next = new_data
            self.tail = new_data
        return

    def empty(self):
        if self.head is None:
            return 1
        else:
            return 0

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            pop_data = self.head.data
            self.head = self.head.next
            self.len -= 1
            return pop_data

    def size(self):
        return self.len

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.head.data

    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.tail.data

queue = Queue()
n = int(stdin.readline())
for _ in range(n):
    cmd = stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        queue.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(queue.pop())
    elif cmd[0] == 'size':
        print(queue.size())
    elif cmd[0] == 'empty':
        print(queue.empty())
    elif cmd[0] == 'front':
        print(queue.front())
    elif cmd[0] == 'back':
        print(queue.back())