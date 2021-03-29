# Disease Spread
# https://www.codewars.com/kata/566543703c72200f0b0000c9/train/scala

def epidemic(tm, n, s0, i0, b, a):
    # your code
    dt = tm / n
    susceptible = [s0, ]
    infected = [i0, ]

    for k in range(n):
        susceptible.append(susceptible[k] - dt * b * susceptible[k] * infected[k])
        infected.append(infected[k] + dt * (b * susceptible[k] * infected[k] - a * infected[k]))

    return int(max(infected))