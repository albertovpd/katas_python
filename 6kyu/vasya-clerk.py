# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/solutions/python

def tickets(people):    
    change = {25: 0, 50: 0}
    for m in people:
        if m == 25:
            change[25] += 1
        elif m == 50:
            if change[25] == 0:
                return "NO"
            else:
                change[25] -= 1
                change[50] += 1
        elif m == 100:
            if change[50] > 0 and change[25] > 0:
                change[25] -= 1
                change[50] -= 1
            elif change[25] >= 3:
                change[25] -= 3
            else:
                return "NO"
    return "YES"