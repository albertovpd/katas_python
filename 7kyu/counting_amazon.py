# Counting in the Amazon

def count_arara(n):
    # ...
    
    par="adak"
    impar="anane"
    numero=""
    m=int((n-1)/2)
    
    if n%2==0:
        numero+=(par+" ")*m+par
    else:
        numero+=(par+" ")*m+impar
    
    
    return numero