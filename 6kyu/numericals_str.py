# numericals of a string

def numericals(s):
    string=""
    dictionary={}
    for e in s:
        dictionary[e]=dictionary.get(e,0)+1
        string+=str(dictionary[e])
    return string
