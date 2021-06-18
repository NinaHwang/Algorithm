import sys

first_line = sys.stdin.readline().split()

n = int(first_line[0])
load = int(first_line[1])

weights = list(map(int, sys.stdin.readline().split()))
weights.sort()

escaped = 0

lightest_idx = 0
heaviest_idx = n-1
boat = 0

while lightest_idx < heaviest_idx:
    if weights[heaviest_idx] + weights[lightest_idx] <= load:
        escaped += 2
        lightest_idx += 1
        heaviest_idx -= 1
    else:
        escaped += 1
        heaviest_idx -= 1

    boat += 1

if lightest_idx == heaviest_idx:
    boat += 1

print(boat)
