def solution(A, K):
    if len(A) == 0:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]
    # take the element from K position and put it in 1st place, then the rest. It's nice