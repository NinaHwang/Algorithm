from itertools import product

def solution(numbers, target):
    lst = [(n, -n) for n in numbers]
    sum_lst = list(map(sum, product(*lst)))

    return sum(1 for i in sum_lst if i == target)

print(solution([1,1,1,1,1],3))
