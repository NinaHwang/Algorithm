import sys

n = int(input())
li = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]

li.sort(reverse=True)

heaviest = 0
answer = 0
for h, w in li:
    if w > heaviest:
        heaviest = w
        answer += 1

print(answer)


