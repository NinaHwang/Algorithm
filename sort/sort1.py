import math

# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    def sort_func(numbers):
        if len(numbers) <= 1:
            return numbers

        pivot = numbers[0]
        a = math.floor(math.log10(pivot))

        tail = numbers[1:]

        left = []
        right = []

        for i in tail:
            b = math.floor(math.log10(i))

            print('pivot', pivot)
            print('i', i)
            print('a', a)
            print('b', b)
            if a != b:
                if a > b:
                    j = i * 10**(a-b)
                    pivot_2 = pivot

                else:

                    pivot_2 = pivot * 10**(b-a)
                    j = i
            else:
                j = i
                pivot_2 = pivot

            if j > pivot_2:
                left.append(i)
            else:
                right.append(i)


        return sort_func(left) + [pivot] + sort_func(right)
    arr = sort_func(numbers)
    return ''.join(list(map(str, arr)))


print(solution([3, 30, 34, 5, 9]))

            


