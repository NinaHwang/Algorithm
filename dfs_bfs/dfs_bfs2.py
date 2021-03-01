# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    queue = deque([begin])
    while not target in queue:
        for w in list(queue):
            v = queue.popleft()
            for word in words:
                count_diffs = 0
                for a, b in zip(v, word):
                    if a != b:
                        count_diffs += 1
                if count_diffs == 1:
                    queue.append(word)
        answer += 1
    return answer

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))

