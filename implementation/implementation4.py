# 이것이 취업을 위한 코딩테스트다 chapter4 구현 예제 4-1
import sys

n = int(sys.stdin.readline())
directions = list(map(str,sys.stdin.readline().split()))

def move(current, n, direction):
    x, y = current[1], current[0]
    if direction == 'R':
        _x = x + 1
        if _x <= n:
            x = _x
    elif direction == 'L':
        _x = x - 1
        if _x > 0:
            x = _x
    elif direction == 'U':
        _y = y - 1
        if _y > 0:
            y = _y
    elif direction == 'D':
        _y = y + 1
        if _y <= n:
            y = _y
    
    return (y, x)

current = (1,1)
for direction in directions:
    current = move(current, n, direction)

print('final: ', current)
