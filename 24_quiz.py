from sys import stdin

n = int(stdin.readline())

def check(string):
    stack = []

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    if len(stack) != 0:
        return False
    else:
        return True


for _ in range(n):
    string = str(stdin.readline())
    
    if check(string):
        print('YES')
    else:
        print('NO')