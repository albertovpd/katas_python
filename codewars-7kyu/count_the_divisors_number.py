def divisors(n):
    return sum( n%e == 0 for e in range(1,n+1))


# other way

def divisors(n):
    
    divisors=0
    
    for e in range(1,n+1):
    
        if n % e == 0:
            
            divisors += 1
            #print(n,divisors,e)
    return divisors
            