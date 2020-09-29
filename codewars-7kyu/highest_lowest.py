def high_and_low(numbers):
    str_numbers=numbers.split() #separate the string
    real_numbers=[]
    # turn into a list to find the max/min
    [real_numbers.append(int(n)) for n in str_numbers] 
    
    # turn again to string (the solution requires it)
    final=str(max(real_numbers))+" "+str(min(real_numbers))
    return final