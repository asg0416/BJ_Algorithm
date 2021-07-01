ea, m = map(int,input().split())
m_list = list(map(int,input().split()))

def m_search(m):
    start = 1  # 이건 1이든 0이든 상관없음 둘다 정답처리됨
    end = max(m_list)

    while start <= end:
        mid = (start + end) // 2
        m_sum = 0

        for tree in m_list:
            if tree > mid:
                m_sum += tree - mid
            else:
                m_sum += 0

        if m_sum >= m:  # 같아 졌을 때가 여기 붙어야 그때 start가 end를 넘어서면서 for문 탈출하고 값 반환 가능 
            start = mid + 1  # + 나무가 다 짝수인데 홀수 목표값이 있으면 정확히 안 나눠떨어지므로 같다는 조건이 아니라 end값 반환하는 방법으로 해야함
        else:
            end = mid - 1
    
    return end

print(m_search(m))        