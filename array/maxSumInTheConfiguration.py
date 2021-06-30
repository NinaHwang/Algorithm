def solution(a, n):
    answer = 0
    for i in range(n):
        answer += a[i] * i
    prev_result, total_sum = answer, sum(a)

    for i in range(n-1):
        result = prev_result - total_sum + a[i] * n
        if result > answer:
            answer = result

        prev_result = result
    
    return answer


# Execution Time:0.71
# https://practice.geeksforgeeks.org/problems/max-sum-in-the-configuration/1/?category[]=Arrays&category[]=Arrays&difficulty[]=1&page=1&sortBy=submissions&query=category[]Arraysdifficulty[]1page1sortBysubmissionscategory[]Arrays