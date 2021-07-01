from sys import stdin


class Node():  # 데이터 저장, 포인트 지정 클래스
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():  # 데이터 입출력 방식 지정 클래스
    def __init__(self):  # 처음에 스택 불리면 헤드가 디폴트 none인 상태로 존재, 생성됨
        self.head = None
        self.len = 0

    def push(self, data):
        new_head = Node(data)  # 제일 마지막, 최신에 들어온 값을 새로운 헤드로 저장하기 전 임시저장해둔다
        new_head.next = self.head  # 최신 데이터의 다음 데이터는 지금의 헤드로 지정됨
        self.head = new_head  # 최신 데이터가 헤드가 됨
        self.len += 1  # 추가하면 길이 1증가
        return

    def pop(self):
        if self.is_empty():  
            return -1

        pop_data = self.head
        self.head = self.head.next
        self.len -= 1  # 데이터 출력돼서 빠지면 길이 -1 
        return pop_data.data

    def top(self):
        if self.is_empty():
            return -1
        return self.head.data

    def size(self):
        return self.len

    def empty(self):
        if self.is_empty():
            return 1
        return 0

    def is_empty(self):
        return self.head is None

n = int(input())
stack = Stack()

for _ in range(n):  # 여기서 언더바는 인덱스가 딱히 의미가없어서 생략하고 범위만큼 계속하라는 뜻
    cmd = stdin.readline().rstrip().split()  # readlines 아니고 readline 해야 정상적으로 실행됨
    order = cmd[0]
    if order == 'push':
        stack.push(cmd[1])
    elif order == 'pop':
        print(stack.pop())
    elif order == 'size':
        print(stack.size())
    elif order == 'empty':
        print(stack.empty())
    elif order == 'top':
        print(stack.top())