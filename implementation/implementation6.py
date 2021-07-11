# 이것이 취업을 위한 코딩테스트다 chapter4 구현 실전 -- 왕실의 나이트
import sys

position = sys.stdin.readline()

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
cases = [(2,1), (2,-1), (1,2), (1,-2), (-2,1), (-2,-1), (-1,2), (-1,-2)]

criteria = range(1,9)

c, r = horizontal.index(position[0]) + 1, int(position[1])


answer = 0
for case in cases:
    _c = c + case[0]
    _r = r + case[1]

    if _c in criteria and _r in criteria:
        answer += 1

print(answer)