# Count the smiley faces!

def count_smileys(arr):
    lista=[]
    for e in arr:
        if e[0] in ':;':
            if e[1] in ')D':
                lista.append(e)
                
            
            elif e[1] in '-~ ':
                if e[2] in ')D':
                    lista.append(e)
            
    return len(lista)

    