def solution(n,q,s,q1,q2):
    answer = []

    rotate = 0
    idx = 0
    for i in range(len(q1)):
        if q1[i] == 1:
            idx = n-((q2[i]+rotate) % n)
            rotate = (q2[i]+rotate) % n
        else:
            if q2[i] + idx >= n:
                answer.append(s[q2[i]+idx-n])
            else:
                answer.append(s[q2[i]+idx])
    
    return answer

print(solution(7,5,'abcdefg',[1,2,2,1,2],[2,0,6,4,1]))

# https://practice.geeksforgeeks.org/problems/lazy-pasha1646/1/?category[]=implementation&category[]=implementation&problemType=functional&difficulty[]=1&page=1&sortBy=submissions&query=category[]implementationproblemTypefunctionaldifficulty[]1page1sortBysubmissionscategory[]implementation
# Execution Time:2.53