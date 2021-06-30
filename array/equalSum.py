def solution(arr, n):
    answer = False
    left_sum = 0
    right_sum = sum(arr[1:])
    for i in range(1, n):
        left_sum += arr[i-1]
        right_sum -= arr[i]
        if left_sum == right_sum:
            return 'YES'
        if left_sum > right_sum:
            return 'NO'

# Execution Time:0.23
# https://practice.geeksforgeeks.org/problems/equal-sum0810/1/?category[]=Arrays&category[]=Arrays&difficulty[]=1&page=2&sortBy=submissions&query=category[]Arraysdifficulty[]1page2sortBysubmissionscategory[]Arrays
