# https://www.codewars.com/kata/5340298112fa30e786000688/train/python

def twos_difference(lst): 
    tuple_list=[]
    unique_numbers = set(lst)
    
    for e in lst:
        if e + 2 in unique_numbers:
            tuple_list.append((e, e + 2))
        tuple_list.sort()
    return tuple_list