N = int(input())
first = 666
while 1:
    if '666' in str(first):  # first 안에 666 들어있는지 확인
        N = N - 1  # 666이 있다면 N 을 하나씩 뺌
        if N == 0:  # 0 이되면 N 번째로 작은 종말 숫자라는 의미로 반복문 종료시킴
            break
    first = first + 1  # 근데 그 숫자에 666이 없으면 1을 더해가면서 first를 바꾸고 666 나올때까지 돌림 = 이렇게 모든 경우를 다따지는게 브루트 포스 개념
print(first)


# 중요한 것은 작은 숫자부터 차례대로 검사해서 666 여부를 판단하기 때문에 7번째 종말 숫자는 단순히 7666이 아니라 6660 이된다. 13번 숫자처럼 6666으로 나오는것은 문제가 되지 않는다.