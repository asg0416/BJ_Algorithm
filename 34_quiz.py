import sys 
n = int(sys.stdin.readline()) 
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

one = 0
zero = 0

def cut(x, y, n):  # x, y는 좌표 시작점, n은 변의 길이 / x가 가로같지만 리스트 인덱스 특성상 가로임
    global one, zero
    check = matrix[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != matrix[i][j]:  # i가 세로, j가 가로
                cut(x, y, n//2)  # 1사분면
                cut(x, y + n//2, n//2)  # 2사분면
                cut(x + n//2, y, n//2)  # 3사분면
                cut(x + n//2, y + n//2, n//2)  # 4사분면
                return

    # 위 이중 반복문을 모두 돌았는데 사분면의 첫번째 좌표 check와 같다면 아래 사항 체크하게 됨
    if check == 0:
        zero += 1
        return
    else:
        one += 1
        return

cut(0, 0, n)
print(zero, one, sep='\n')

#[[1, 1, 0, 0, 0, 0, 1, 1], 
# [1, 1, 0, 0, 0, 0, 1, 1], 
# [0, 0, 0, 0, 1, 1, 0, 0], 
# [0, 0, 0, 0, 1, 1, 0, 0], 
# [1, 0, 0, 0, 1, 1, 1, 1], 
# [0, 1, 0, 0, 1, 1, 1, 1], 
# [0, 0, 1, 1, 1, 1, 1, 1], 
# [0, 0, 1, 1, 1, 1, 1, 1]]