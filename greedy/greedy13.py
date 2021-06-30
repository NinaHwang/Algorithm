def solution(number, k):
    answer = [number[0]]
    i = 1
    while i < k + 1 and len(answer) < len(number) - k + 1:
        print(i,number[i])
        if number[i] > answer[-1]:
            for j in sorted(answer, reverse=True):
                if j < number[i]:
                    answer.pop()
                else:
                    break
            answer.append(number[i])
        elif number[i] == answer[-1]:
            answer.append(number[i])
        print('see!', answer)
        i+=1
    print('??', answer[i+1:])
    return answer + [x for x in number[i+1:]]

print(solution("1231234", 3))
print('-------------------------------------------')
print(solution('1924', 2))
print('-------------------------------------------')
print(solution("4177252841", 4))


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.13ms, 10.1MB)
# 테스트 5 〉	통과 (0.85ms, 10.2MB)
# 테스트 6 〉	통과 (4.74ms, 10.3MB)
# 테스트 7 〉	통과 (9.19ms, 10.3MB)
# 테스트 8 〉	통과 (24.11ms, 10.3MB)
# 테스트 9 〉	통과 (21.03ms, 11.8MB)
# 테스트 10 〉	통과 (210.96ms, 11.6MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)