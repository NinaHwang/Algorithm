# 이것이 취업을 위한 코딩테스트다 chapter4 구현 예제 4-2
import sys

n = int(sys.stdin.readline())

answer = 0

for i in range(60):
    for j in range(60):
        for k in range(n+1):
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)