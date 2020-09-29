# alphabet war

def alphabet_war(fight):
    dicc = {'w':4, 'p':3, 'b':2, 's':1, 'm':-4, 'q':-3, 'd':-2, 'z':-1}
    count=0
    for f in fight:
        for k, v in dicc.items():
            if f == k:
                count+= v
    
    if count > 0:
        return "Left side wins!"
    elif count < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"