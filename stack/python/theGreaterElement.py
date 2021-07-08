from collections import deque

def solution(arr, n):
    answer = [-1] * n
    stack = deque()
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)

    return answer


print(solution([1,3,2,4], 4))
print(solution([7,8,1,4], 4))

# Execution Time:1.09
# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/?category[]=Stack&category[]=Stack&difficulty[]=1&page=1&query=category[]Stackdifficulty[]1page1category[]Stack