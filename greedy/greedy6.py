import sys

n = int(input())
li = []
li = [tuple(map(int, sys.stdin.readline().split())) for x in range(n)]

li.sort(key=lambda x: (x[1], x[0]))

answer = 1
end = li[0][1]
for start_time, end_time in li[1:]:
    if start_time >= end:
        end = end_time
        answer += 1

print(answer)