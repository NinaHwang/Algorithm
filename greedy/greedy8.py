import sys

n = int(input())
li = [int(x) for x in sys.stdin.readline().split()]
total = int(input())

for i in range(total):
    li.sort()
    li[0] += 1
    li[-1] -= 1

li.sort()
print(li[-1] - li[0])