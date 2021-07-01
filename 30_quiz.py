from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

# result_list = []
count = 0

goal = list(map(int, stdin.readline().rstrip().split()))
q = list(range(1, n + 1))

for _ in range(len(goal)):
    while q[0] != goal[0]:
        if goal[0] in q[int(len(q)//2) + 1:]:
            q.insert(0, q[-1])
            q.pop()
            count += 1
        else:
            q.append(q[0])
            q.pop(0)
            count += 1

    if q[0] == goal[0]:
        # result_list.append(q[0])  # 문제 풀때 썼던 참고용 리스트
        q.pop(0)
        goal.pop(0)

print(count)