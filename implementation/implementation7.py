# 이것이 취업을 위한 코딩테스트다 chapter4 구현 실전 -- 게임 개발
import sys

map_range = list(map(int, sys.stdin.readline().split()))
position = list(map(int, sys.stdin.readline().split()))
li = []
for i in range(map_range[0]):
    li.append(list(map(int, sys.stdin.readline().split())))

li[position[0]][position[1]] = 1


def turn(current_position):
    global li

    h, v, direction = current_position[0], current_position[1], current_position[2]

    cnt = 0
    _v = v
    _h = h

    is_end = False

    while li[_h][_v] == 1:
        if cnt > 3:
            is_end = True
            break

        if direction % 4 == 0:
            _v = v - 1
            _h = h
        elif direction %4 == 1:
            _v = v
            _h = h - 1
        elif direction %4 == 2:
            _v = v + 1
            _h = h
        else:
            _v = v
            _h = h + 1

        direction += 3        
        cnt += 1

    if is_end:
        return False

    return [_h, _v, direction]

answer = 1
while position:
    position = turn(position)
    if not position:
        break
    li[position[0]][position[1]] = 1
    answer += 1
    
print('answer: ', answer)
