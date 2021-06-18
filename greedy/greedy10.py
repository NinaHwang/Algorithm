import sys
from collections import deque

n = int(input())
li = deque(list(map(int, sys.stdin.readline().split())))

last = 0
answer = ''
i = 0

for i in range(n):
    x, y = li[0], li[-1]
    if x < last and y < last:
        break

    if x < y:
        small, big, is_left = x, y, True
    else:
        small, big, is_left = y, x, False

    if small > last:
        last = small
    elif big > last:
        last = big
        is_left = not is_left
    else:
        continue

    i += 1
    if is_left:
        answer += 'L'
        li.popleft()
    else:
        answer += 'R'
        li.pop()
        

print(i)
print(answer)


