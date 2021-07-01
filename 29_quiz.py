from sys import stdin

n = int(stdin.readline())
num_list = [int(stdin.readline().rstrip()) for _ in range(n)]  # [4, 3, 6, 8, 7, 5, 2, 1]
sample = list(range(1,n + 1))  # [1, 2, 3, 4, 5, 6, 7, 8]
                                # 0  1  2  3  4  5  6  7

stack = []
new_list = []
result = []
while len(new_list) != n:
    num_i = 0
    sample_i = 0
    for _ in range(2 * n):
        if sample_i == n:
            new_list.append(stack[-1])
            stack.pop()
            result.append('-')
            num_i += 1

        if sample_i < n:
            if sample[sample_i] <= num_list[num_i]:  # 8 < 8
                stack.append(sample[sample_i])
                sample_i += 1  # 7
                result.append('+')

            else:
                new_list.append(stack[-1])
                stack.pop()
                result.append('-')
                num_i += 1  # 3 >> 8

if new_list == num_list:
    for sign in result:
        print(sign)
else:
    print('NO')