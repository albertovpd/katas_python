# https://www.codewars.com/kata/54d7660d2daf68c619000d95/solutions/python/me/best_practice

import math
def convertFracts(lst):

    denominators=[d[1] for d in lst ] # get all denominators
    lcm = 1 
    for d in denominators:
        lcm = lcm*d//math.gcd(lcm, d) # lower common denominator
    return [[lcm*e[0]//e[1],lcm] for e in lst]