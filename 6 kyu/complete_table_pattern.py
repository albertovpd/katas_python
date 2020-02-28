# Complete the table pattern

def pattern(rows, columns, s):
    f="+"
    file="---+"
    c="|"
    fil=f+file*columns
    v=rows*columns-len(s)
    s=s+" "*v
    sf=list(map(lambda x: c+" "+x+" ",s))
    result=""
    for col in range(0,len(sf),columns):
        result+=fil+"\n"+"".join(sf[col:col+columns])+c+"\n"
    result+=fil
    return result