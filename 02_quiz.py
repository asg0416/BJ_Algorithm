a = int(input())
b = input()

# 순서 별 곱셈
a_b1 = a * int(b[2])
a_b2 = a * int(b[1])
a_b3 = a * int(b[0])
a_b = a * int(b)

# 답
print(a_b1, a_b2, a_b3, a_b, sep='\n')