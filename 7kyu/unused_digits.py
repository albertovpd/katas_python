# Filter unused digits

def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))

# other way

def unused_digits(*args):
    all_numbers=set('0123456789') # this takes the numbers 1 by 1

    r= ''.join(sorted(all_numbers.difference(''.join(str(a) for a in args))))
    
    # difference = substract from each string, but performing the math operation "-" is not allowed

    return r