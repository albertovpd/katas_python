def solution(X, Y, D):
    # write your code in Python 3.6
    '''FrogJmp'''
    c=0
    while c*D+X < Y:
        c+=1
    return c