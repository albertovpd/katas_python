# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/solutions/python

import re
def first_non_repeating_letter(string):
    for s in string:
        if len(re.findall(s.lower(), string.casefold())) == 1:
            return s
    return ""