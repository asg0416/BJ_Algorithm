# 정수 리스트
int_num = list(range(1, 10001))
self_list = []

# 셀프 넘버 구하는 함수
def repeat_num(n):
    self_num = n + n//1000 + (n%1000)//100 + ((n%1000)%100)//10 + n%10
    return self_num

# 셀프 넘버 리스트 만들기
for i in int_num:
    if repeat_num(i) <= 10000:
        self_list.append(repeat_num(i))
self_list = list(set(self_list))

# 중복값 딕셔너리 key 값으로 받아서 삭제 함수
exception_dict = {}
result = []

def exception(int_list, self_num_list):
    for key in int_list:
        exception_dict[key] = True

    for key in self_num_list:
        del exception_dict[key]

    for key in exception_dict.keys():
        result.append(key)

    for i in range(len(result)):
        print(result[i])


exception(int_num, self_list)