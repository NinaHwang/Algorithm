import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

answer = [0] * n

for i in range(n):
    x = li[i]
    target = i+1

    zero_cnt = 0
    idx = 0
    while zero_cnt < x:
        if answer[idx] == 0:
            zero_cnt += 1
        idx += 1

    final_idx = idx
    while answer[final_idx] != 0:
        final_idx += 1
    answer[final_idx] = target

print(answer)