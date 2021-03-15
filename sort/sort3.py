# https://www.acmicpc.net/problem/1181

import sys

#n = int(input())
#li = []
#for i in range(n):
#    a = sys.stdin.readline().rstrip()
#    if a not in li:
#        li.append(a)
#
#def sort_li(words):
#    if len(words) <= 1:
#        return words
#
#    pivot = words[0]
#    left = []
#    right = []
#    tail = words[1:]
#
#    for i in tail:
#        if len(i) < len(pivot):
#            left.append(i)
#        elif len(i) == len(pivot):
#            if i < pivot:
#                left.append(i)
#            else:
#                right.append(i)
#        else:
#            right.append(i)
#
#    return sort_li(left) + [pivot] + sort_li(right)
#
#for word in sort_li(li):
#    print(word)
#

n = int(input())
li = list(set([sys.stdin.readline().rstrip() for x in range(n)]))
li.sort()
li.sort(key=lambda x:len(x))
for word in li:
    print(word)
