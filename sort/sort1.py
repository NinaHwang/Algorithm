import math
import collections
# https://programmers.co.kr/learn/courses/30/lessons/42746
#
#def solution(numbers):
#    def sort_func(numbers):
#        if len(numbers) <= 1:
#            return numbers
#
#        numbers.sort(reverse=True)
#
#        pivot = numbers[0]
#        if pivot == 0:
#            return numbers
#
#        a = math.floor(math.log10(pivot))
#        
#        tail = numbers[1:]
#
#        left = []
#        right = []
#
#        for i in tail:
#            if i == 0:
#                right.append(i)
#                break
#
#            b = math.floor(math.log10(i))
#            j = i * 10**(a-b)
#            print('j',j)
#            print('p', pivot)
#            if j >= pivot:
#                left.append(i)
#            else:
#                right.append(i)
#
#            print('l', left)
#            print('r', right)
#
#        return sort_func(left) + [pivot] + sort_func(right)
#
#    arr = sort_func(numbers)
#    
#    answer = ''.join(list(map(str, arr)))
#    if int(answer) == 0:
#        return '0'
#
#
#    return answer
#
#
#def solution(numbers):
#    b = ''
#    if 0 in numbers:
#        a = sum(1 for x in numbers if x == 0)
#        for i in range(a):
#            b += '0'
#    if max(numbers) == 0:
#        return '0'
#    def sort(numbers):
#        if len(numbers) <= 1:
#            return numbers
#        
#        numbers.sort(reverse=True)
#        li = list(map(str, numbers))
#        pivot = li[0]
#
#        left = []
#        right = []
#
#        tail = [x for x in li[1:] if x != '0']
#
#        for i in tail:
#            print('i',i)
#            print('pivot',pivot)
#            if i+pivot >= pivot+i:
#                left.append(i)
#            else:
#                right.append(i)
#
#        return sort(left) + [pivot] + sort(right)
#
#    arr = sort(numbers)
#
#    return ''.join(arr)+b

def solution(numbers):
    li = list(map(str, numbers))
    li.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(li)))

print(solution([6,646]))
