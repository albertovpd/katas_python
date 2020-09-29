# Unknown amount of duplicates. One missing number.

def find_dups_miss(arr):
    dict_dup = {}
    sorted_list = list(range(min(arr),max(arr)))
    missing = list(set(sorted_list) - set(arr))
    missing= missing[0]
    for i in arr:
        dict_dup[i] = dict_dup.get(i, 0) +1
    
    lst_out = [k for k, v in dict_dup.items() if v > 1]
    return [missing, sorted(lst_out)]

# other way

from collections import Counter

def find_dups_miss(arr):
    sorted_list = list(range(min(arr),max(arr)))
    missing = list(set(sorted_list) - set(arr))
    d = sorted([item for item, count in Counter(arr).items() if count > 1])
    return [missing[0],d]

