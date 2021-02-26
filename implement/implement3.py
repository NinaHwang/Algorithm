import itertools

def solution(numbers):
    lst =sorted(list(map(int,numbers)))
    number = ''
    numbers = []
    answer = 0
    for n in range(0, len(lst)+1):
        for subset in itertools.permutations(lst, n):
            subset = list(map(str, subset))
            number = ''.join(subset)
            if number != '' and int(number) >= 2 and int(number) not in numbers :
                numbers.append(int(number))

    for number in numbers:
        is_prime = 1
        for i in range(2, number):
            if number % i == 0:
                is_prime = 0
                break
        if is_prime == 1:
            answer += 1
    return answer


print(solution('011'))
