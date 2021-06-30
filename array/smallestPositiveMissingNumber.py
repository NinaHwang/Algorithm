def solution(arr, n):
    li = [x for x in arr if x > 0]
    li = sorted(list(set(li)))

    for i in range(0, len(li)):
        if i+1 != li[i]:
            return i+1

    return (li[-1]+1 if len(li) > 0 else 1)

# Execution Time:0.96

# https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1/?category[]=Arrays&category[]=Arrays&difficulty[]=1&page=1&sortBy=submissions&query=category[]Arraysdifficulty[]1page1sortBysubmissionscategory[]Arrays