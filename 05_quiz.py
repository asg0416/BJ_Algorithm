def avg(list):
    list_sum = 0
    for num in range(1,len(list)):
        list_sum += list[num]
    avg = list_sum / list[0]
    return avg

def find(list):
    count = 0
    for ind in range(1, len(list)):
        if list[ind] > avg(list):
            count += 1
        
    result = round(count / list[0] * 100, 3)
    x = '{result:.3f}%'
    return x

n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    print(find(a))