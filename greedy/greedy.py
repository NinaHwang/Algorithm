n = int(input())
if n % 5 == 0:
    print(n//5)
a = 0
while n > 0:
    if n <= 12 and n%3 == 0:
        print(a + n//3)
        break
    n -= 5
    a += 1
else:
    print(-1)