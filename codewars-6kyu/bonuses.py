# https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6/train/python

def bonus(arr, s):

    arr=[1/x for x in arr]
    sums=sum(arr)
    #print(arr)
    solution=[round(a*s/sums) for a in arr]
    #print(solution)
    return solution