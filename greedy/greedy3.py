def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        while len(answer) > 0 and answer[-1] < num and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)
#def solution(number, k):
#    answer ='' 
#    a = 0
#    b = k+1
#    while b <= len(number):
#        test_range = range(a,b)
#        num = '0'
#        for n in test_range:
#            if number[n] > num:
#                num = number[n]
#                a = n+1
#            if num == '9':
#                break
#        answer += num 
#        number = 'x'*a + number[a:]
#       b += 1
#
#    return answer

def solution(number,k):
    answer = number[0]
    for i in number[1:]:
        while k > 0 and len(answer) > 0 and i > answer[-1]:
            k -= 1
            answer = answer[:-1]
            print('k',k)
            print(answer)
        answer += i
    if k != 0:
        answer = number[:-k]

    return answer

print(solution('999',2))
