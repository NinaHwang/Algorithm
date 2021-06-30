def solution(arr, n):
    a,b,diff = 0,0,0
    arr.sort()

    for i in range(n):
        if a != 0 and b != 0:
            break
        current_diff = i + 1 - arr[i]
        if current_diff != diff:
            if current_diff > diff and a == 0:
                a = arr[i]
            elif b == 0:
                b = i + 1 - diff
            diff = current_diff

    if b == 0:
        b = arr[-1] + 1

    return [a, b]


# Execution Time:0.42
# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1#