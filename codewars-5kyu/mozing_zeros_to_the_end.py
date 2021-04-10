# https://www.codewars.com/kata/52597aa56021e91c93000cb0/solutions/python

def move_zeros(array):
    result = [n for n in array if n!=0]    
    for z in range(array.count(0)):
        result.append(0)
        
    return result