N = int(input())

M = list(map(int, input().split()))

m_max = 0
m_min = 10**6

M.sort()
print(f"{M[0]} {M[-1]}")
''' 시간 초과
for m in M:
    m_max = m if m_max < m else m_max
    m_min = m if m_min > m else m_min

print(f"{m_min} {m_max}")
'''