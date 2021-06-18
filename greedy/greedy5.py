def getMinDiff(A, N):
    half = N / 2
    total = 0

    obj = {}

    for i in A:
        if i in obj.keys():
            obj[i] += 1
        else:
            obj[i] = 1

        if obj[i] > half:
                return i

    return -1

print(getMinDiff([15], 1))