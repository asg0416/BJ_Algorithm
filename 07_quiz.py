def alpha_count():
    alpha_input = input()
    alpha_sample = alpha_input.lower()

    alpha_check_list = [0] * 26

    for alpha in alpha_sample:
        if not alpha.isalpha():  # False 가 아니라면 계속해라.
            continue
        
        char_index = ord(alpha) - ord('a')
        alpha_check_list[char_index] += 1

    max_count_alpha = alpha_check_list[0]  # 가장 자주 나온 알파벳 갯수
    for num in alpha_check_list:
        if num > max_count_alpha:
            max_count_alpha = num

    index_num = []
    for i in range(len(alpha_check_list)):
        if alpha_check_list[i] == max_count_alpha:  # 가장 자주 나온 알파벳 갯수가 들어 있는 ind 값 저장
            index_num.append(i)

    if len(index_num) == 1:
        char = chr(index_num[0] + ord('a'))
        return char.upper()
    else:
        return '?'

print(alpha_count())
