# https://www.codewars.com/kata/605ae9e1d2be8a0023b494ed/train/python
def count_salutes(hallway):
    right = 0
    salutes = 0
    for p in hallway:
        if p == '>':
            right += 1
        if p == '<':
            salutes += right
    return 2* salutes
