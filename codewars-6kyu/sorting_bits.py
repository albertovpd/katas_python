# Sorting by bits

def sort_by_bit(arr): 
    # your code
    return sorted(arr, key=lambda e: (bin(e).count("1"),e))