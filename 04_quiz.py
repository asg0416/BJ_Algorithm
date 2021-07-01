n = int(input())  # 반복문 들어가면서 숫자 변함
check = n  # 그래서 처음 n 을 체크하기 위해서 저장해둠
new_num = 0
temp = 0
count = 0

while True:
    temp = n // 10 + n % 10  # 새로운 수를 만들기 위한 중간 숫자이다.
    new_num = (n % 10)*10 + temp % 10  # 각각의 10의 나머지 (= 뒷자리)를 들고와서 합치는 방식이다.
    count += 1  # 새로운 숫자가 하나 나오면 사이클을 한번 돌고 있다는 뜻이므로 카운트 해준다.
    n = new_num  # 바뀐 수로 위 과정을 반복하기 위해서 n 에 새로 나온 숫자를 대입해준다.
    if check == new_num:  # 맨 처음 받은 값과 새로 만들어진 숫자를 비교해서 같으면 count 를 반환해준다.
        break
print(count)