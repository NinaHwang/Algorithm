n, k = map(int, input().split())
integers = list(range(2, n+1))

i = 0
while k > 0:
    smallest = integers.pop(0)
    answer = smallest
    k -= 1
    for n in integers[1:]:
        if n % smallest == 0:
            answer = n
            integers.remove(n)
            k -= 1
            if k == 0:
                break

print(answer)
