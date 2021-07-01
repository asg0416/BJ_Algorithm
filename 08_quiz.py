# replace 함수 사용 법 익히기

cro_alpha_sample = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cro_alpha = input()

for alpha in cro_alpha_sample:
    if alpha in cro_alpha:
        cro_alpha = cro_alpha.replace(alpha, '*')  # 샘플 문자가 입력값 안에 있으면 * 로 치환해서 남은 글자의 갯수를 셈

print(len(cro_alpha))