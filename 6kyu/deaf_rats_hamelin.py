# the deaf rats of hamelin

import re

def count_deaf_rats(town):
    # Your code here
    town = town.replace(' ','').split('P')
    #print(town)
    return re.findall('..',town[0]).count('O~')  + re.findall('..',town[1]).count('~O')

# other way

def count_deaf_rats(town):
    rat = []
    deaf = 0
    rat.append(town.split("P")[0].replace(" ",""))
    rat.append(town.split("P")[1].replace(" ",""))
    
    for i in range(0,len(rat[0]),2):
        if rat[0][i]=="O":
            deaf += 1
    for x in range(0,len(rat[1]),2):
        if rat[1][x]=="~":
            deaf += 1
    return deaf