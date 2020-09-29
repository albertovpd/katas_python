# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/solutions/python

def find_outlier(integers):
    even=[]
    odd=[]
    for e in integers:
        if e%2 == 0:
            even.append(e)
        else:
            odd.append(e)
    if len(even)<len(odd):
        return even[0]
    else:
        return odd[0]