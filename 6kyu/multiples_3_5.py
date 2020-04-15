# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    list_multiples=[]
    for e in range(number):
        if e % 3==0 or e% 5==0:
            list_multiples.append(e)
    return sum(list_multiples)