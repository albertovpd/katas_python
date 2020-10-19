def solution(A):
    # write your code in Python 3.6
    for e in A:
        if A.count(e)==1:
            return e
        