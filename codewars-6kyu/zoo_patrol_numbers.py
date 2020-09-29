# https://www.codewars.com/kata/5276c18121e20900c0000235/train/python

def find_missing_number(numbers):
    
    # i hated this trick
    if not numbers:
        return 1

    n = max(numbers)+1 
    num_set = set(numbers)
    #print (num_set)
    
    
    for e in list(range(1, n+1)):
        # timeout while iterating by numbers, it looks like sets are faster than lists
        if e not in num_set:
            return e