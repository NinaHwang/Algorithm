
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    lst = [i for i in s]
    for i in range(len(lst)):
        if (i == 0 and lst[i].isalpha()) or lst[i-1] == ' ':
            lst[i] = lst[i].upper()
        elif lst[i].isalpha() and lst[i].isupper():
            lst[i] = lst[i].lower()

    return ''.join(lst)


print(solution("3people unFollowed me"))
print(solution("for the last week"))
