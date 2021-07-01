n = int(input())  # 처음 케이스가 몇개인지 받는 변수

def check_word():
    word = list(input())  # 함수가 불리면 단어로 값을 받음
    for i in range(len(word)-1):
        if word[i] == word[i+1]:  # 단어 앞 뒤로 비교하면서 같은 단어면
            word[i] = ''  # 해당 자리를 공백 처리  >>  이거할때 그냥 문자열 상태면 에러(자료형 안 맞다는 것, 참조 범위 벗어난다는 것)나서 리스트로 만들어서 공백으로 바꾸고

    new_word = ''.join(word)  # 문자열인 리스트 인자들을 모아서 문자열로 합쳐달라는 뜻

    alpha_count = 0  # 새로 만들어진 앞 뒤 중복이 제외된 단어 상태에서 또 중복 글자가 있는 지 확인
    for alpha in new_word:
        alpha_count += new_word.count(alpha)  # 해당 알파벳이 문자 안에 있는 만큼 계수하라는 뜻
    
    if alpha_count == len(new_word):  # 그 값이 문자열의 길이보다 크다는 것은 중복된 글자가 있다는 뜻이므로 같을 때만 true로 반환
        return True


count = 0
for i in range(n):  # 받는 n 만큼 반복문을 돌려서 
    if check_word() is True:  # 조건에 맞는 단어면 count 해라.
        count += 1

print(count)
