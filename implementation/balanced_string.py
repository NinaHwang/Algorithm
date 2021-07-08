def solution(n):
    string = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    cnt = 0
    a = n
    while n > 26:
        cnt += 1
        n -= 26

    for i in range(cnt):
        answer += string

    if n % 2 == 0:
        answer += string[:n//2]
        answer += string[(n//2) * -1:]
        return answer

    sum_of_digits = sum(list(map(lambda x: int(x), str(a))))
    if sum_of_digits % 2 == 0:
        answer += string[:(n+1)//2]
        if n != 1:
            answer += string[((n-1)//2)*-1:]
        return answer

    if n != 1:
        answer += string[:(n-1)//2]
    answer += string[((n+1)//2)*-1:]
    return answer   


print(solution(21), bool('abcdefghijpqrstuvwxyz' == solution(21)))
print(solution(28), bool('abcdefghijklmnopqrstuvwxyzaz' == solution(28)))
print(solution(53), bool('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza' == solution(53)))

# https://practice.geeksforgeeks.org/problems/balanced-string1627/1/?problemType=functional&difficulty[]=0&page=1&sortBy=submissions&category[]=implementation&query=problemTypefunctionaldifficulty[]0page1sortBysubmissionscategory[]implementation#
# Execution Time:0.05