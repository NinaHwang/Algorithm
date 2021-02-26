n = int(input())
minutes = list(map(int, input().split()))

minutes.sort()
print(minutes)
result = 0
for i in range(1,n+1):
    print(minutes[0:i])
    result += sum(minutes[0:i])

print(result)