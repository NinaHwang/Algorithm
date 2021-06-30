def minimumPlatform(n, arr, dep):
    li = [(arr[i],dep[i]) for i in range(n)]

    li.sort(key=lambda tup: tup[1])
    platform = []
    cnt = 0

    for train in li:
        platform = [x for x in platform if x[1] > train[0]]
        print(platform)
        platform.append(train)
        if len(platform) > cnt:
            cnt = len(platform)
        print(platform)



    return cnt


print(minimumPlatform(6, ['0900', '0940', '0950', '1100', '1500', '1800'], ['0910', '1200', '1120', '1130', '1900', '2000']))
