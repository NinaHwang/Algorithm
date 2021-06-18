def solution(n, times):
    times.sort(reverse=True)
    fastest, longest = 1, min(times)*n
    answer = 0

    while fastest <= longest:
        middle = (fastest + longest)//2
        print('f', fastest, 'l', longest, 'm', middle)
        for i in times:
            n -= middle//i
            if n <= 0:
                longest = middle-1
                answer = middle
                break
        if n > 0:
            fastest = middle+1

    return answer

print(solution(6, [7,10]))
