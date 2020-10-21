# poor performance

def solution(A):
    # write your code in Python 3.6
    for e in list(range(1,max(A)+1)):
        if e not in A:
            return e