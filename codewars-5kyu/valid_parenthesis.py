# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    #your code here
    parenthesis = [s for s in string if s=="(" or s==")"]
    c=0
    result= []
    for p in parenthesis:
        if p=="(":
            c+=1         
        else:
            c-=1
        result.append(c)
    for e in result[::2]:
        if e<0:
            return False   
            
    return True if c==0 else False