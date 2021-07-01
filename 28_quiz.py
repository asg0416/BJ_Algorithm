from sys import stdin

while True:

    str_list = stdin.readline()
    if str_list[0] == '.':  # . 입력받으면 종료
        break

    stack = []
    answer = True  # no 조건에 걸리면 반환해줄 변수

    for i in str_list:  # 여는 괄호 시작되면 
        if i == '(' or i == '[':
            stack.append(i)  # 스택에 저장

        elif i == ')':  # 닫는 괄호 나오면
            if len(stack) == 0:  # 스택 비어있으면 여는 괄호 없었다는 거니까
                answer = False  # no 조건
                break
            if stack[-1] == '(':  # 스택 마지막에 저장된 값이 여는 괄호면
                stack.pop()  # 마지막 저장된 값 빼냄
            else:
                answer = False  # 위 조건 이외는 모두 no조건 오답처리
                break
        
        elif i == ']':  # 같은 내용
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                answer = False
                break

    if answer and not stack:  # answer가 True 이면서 stack 이 비었을 때. (true 가 아닌게( = false)일때 true 인 상태)
        print('yes')  
    else:
        print('no')