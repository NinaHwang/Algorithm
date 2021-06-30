def solution(arr, n):
    for i in range(n-1,-1,-1):
        for j in range(n-i):
            if arr[j] <= arr[j+i]:
                return i

# Execution Time:0.51
# https://practice.geeksforgeeks.org/problems/maximum-index-1587115620/1/?category[]=Arrays&category[]=Arrays&difficulty[]=1&page=1&sortBy=submissions&query=category[]Arraysdifficulty[]1page1sortBysubmissionscategory[]Arrays