# 80's Kids #2: Help ALF Find His Spaceship

import re

def find_spaceship(astromap):
    x = astromap.split('\n')[::-1]
    for i in x:
        if re.search(r'.?X.?',i):
            return [i.index('X'),x.index(i)]
    else: 
        return "Spaceship lost forever."