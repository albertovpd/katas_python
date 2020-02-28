# see you next happy year

def next_happy_year(year):
    year += 1  
    # if set lenght <4 means the elements arent uniques
    while len(set(str(year))) != 4:
        year += 1
    return year