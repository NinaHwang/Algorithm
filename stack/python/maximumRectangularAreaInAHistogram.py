from collections import deque


def solution(histogram):
    stack = deque()
    answer = 0
    for i in histogram:
        left = 1

        while stack and stack[-1 * left] >= i:
            left += 1
        right = 1
        for k in histogram[i+1:]:
            if k < i:
                break
            right += 1
        
        width = (right - left - 1)
        height = i
        tmp = width * height
        if tmp > answer:
            answer = tmp
        stack.append(i)

    return answer


print(solution([6,2,5,4,5,1,6]))
print(solution([1,2,3,4,5]))
print(solution([1]))

        # answer = 0
        # for i in range(len(histogram)):
        #     for j in range(i,-1,-1):
        #         tmp = histogram[j:i+1]
        #         if min(tmp) * (i-j+1) > answer:
        #             answer = min(tmp) * (i-j+1)
        # return answer

        # answer = 0
        # for i in range(0, len(histogram)):
        #     j = 0
        #     while j + i < len(histogram):
        #         shortest = min(histogram[j:j+i+1])
        #         area = shortest * (i+1)
        #         if area > answer:
        #             answer = area
        #         j += 1

        # return answer

        # indices = sorted(range(len(histogram)), key=lambda k: histogram[k])
        # answer = 0
        # for i in indices:
        #     left = next((idx+1 for idx in range(i-1, -1, -1) if histogram[idx] == None), 0)
        #     right = next((idx-1 for idx in range(i+1, len(histogram)) if histogram[idx] == None), len(histogram)-1)
        #     area = (right-left+1) * histogram[i]
        #     if area > answer:
        #         answer = area
        #     histogram[i] = None

        # return answer