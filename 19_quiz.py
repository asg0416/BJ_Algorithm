def count(n):
    print(2 ** n - 1)  # 하노이의 탑 횟수 구하는 식

def move(start, to):  # N개의 탑을 시작점에서 목적지로 옮기는 함수
    print(f'{start} {to}')

def hanoi(N, start, to, via):  # 하노이 함수는 N개의 탑을 시작점에서 경유지를 거쳐 목적지로 가게하는 함수
    if N == 1:  # 옮겨야하는 것이 하나일 때가 오면
        move(start, to)  # 시작점에서 목적지로
    else:
        hanoi(N-1, start, via, to)  # 1이 아니면 그 앞 전 탑을 시작을 시작으로 경유지를 목적지로 삼고 목적지를 경유해서 다시 하노이 함수를 돌림
        move(start,to)  # 목적으로하는 n 번째 탑이 경유지로 모두 옮겨 지고나면 해당 탑을 시작에서 목적지로 옮김
        hanoi(N-1, via, to, start)  # 경유지에 남은 탑을 목적지로 옮기기 위해 시작점을 경유지로 두고 하노이 함수를 실행 시킴

n = int(input())
count(n)
hanoi(n, '1', '3', '2')