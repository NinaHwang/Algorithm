def biggest(n, m):
    li = []

    for i in str(n):
        if len(li) == 0:
            li.append(i)
            continue
        if len(li) < len(str(n)) - m:
            li.append(i)
        else:
            while len(li) > len(str(n)) - m -2:
                if li[0] > i:
                    break
                li.pop(0)
            li.append(i)
        print(li)

    return li


print(biggest(5276823, 3))
            
        