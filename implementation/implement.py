import sys
t = int(sys.stdin.readline())
for i in range(t):
    a,b = map(int,input().split())
    a = a%10
    b = b%4 if b != 0 else 4
    print(a**b)
    print(a)
    print(b)
    
    print((a**b)%10 if ((a**b) %10) != 0 else 10)