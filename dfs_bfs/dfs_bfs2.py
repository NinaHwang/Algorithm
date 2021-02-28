answer = 0

def dfs(begin, target, words):
    global answer
    if begin == target:
        return

    for word in words:
        count_diffs = 0
        for a, b in zip(begin, word):
            print(begin)
            print(word)
            if a!=b:
                count_diffs += 1
        if count_diffs == 1:
            begin = word
            words.remove(word)
            answer += 1
            dfs(word, target, words)

def solution(begin, target, words):
    if target not in words:
        return 0
    global answer
    dfs(begin, target, words)
    return answer-1

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))

