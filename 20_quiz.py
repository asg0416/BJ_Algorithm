n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

a.sort(key=lambda x: (x[1],x[0]))  # 람다는 익명함수 정도의 느낌. 이름을 정해주지 않고 사고의 흐름대로 함수(특정 조건)을 걸어서 사용할 수 있다

for x, y in a:  # for를 한번만 써도 리스트 안에 있는 리스트의 요소를 풀어서 나타낼 수 있다.
    print(x, y)