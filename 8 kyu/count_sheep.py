# If you can't sleep, just count sheep!!

def count_sheep(n):
    sol=""
    for x in range(n):
        sol+=str(x+1)+" sheep..."
    return sol