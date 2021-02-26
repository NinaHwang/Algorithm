def solution(people, limit):
    people.sort()
    light = []
    heavy = []
    half = limit//2
    answer = 0

    for x in people:
        if x <= half:
            light.append(x)
        else:
            heavy.append(x)

    while len(light) > 0 and len(heavy) > 0:
        if light[0] + heavy[-1] <= limit:
            answer += 1
            light.pop(0)
            heavy.pop()
        else:
            answer += 1
            heavy.pop()

    if len(light) > 0:
        if len(light) % 2 == 0:
            answer += len(light) // 2
        else:
            answer += len(light) // 2 + 1
    else:
        answer += len(heavy)

    return answer



print(solution([70, 50, 80],100))
