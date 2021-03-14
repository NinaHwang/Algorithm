#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)

    h = []
    a = 0

    for i in citations:
        if i >= len(h):
            h.append(i)
        else:
            break

    return min(len(h), h[-1])



print(solution([ 4, 4, 4, 5, 0, 1, 2, 3])==4)
print(solution([ 3, 0, 6, 1, 5])==3)
print(solution([2, 7, 5])==2)
print(solution([0, 0 ,1 ,1])==1)
print(solution([10, 11, 12, 13])==4)
