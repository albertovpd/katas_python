# Test's results

def test(r):
    # your code
    media=sum(r)/len(r)
    class_average=round(media,3)
    diccionario={'h':0,'a':0,'l':0}
    h=0
    a=0
    l=0
    
    for e in r:
        if e>=9:
            h+=1
            diccionario['h']=h
            
        elif e>=7:
            a+=1
            diccionario['a']=a
        else:
            l+=1
            diccionario['l']=l
    mayores=[]        
    for e in r:
        if e>=9:
            mayores.append(e)
            if len(mayores)==len(r):
                return [class_average, diccionario, 'They did well'] 
        else:
            return [class_average, diccionario] 
            