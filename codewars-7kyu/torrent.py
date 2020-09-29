# Computer problem series #2: Torrent download

def torrent(files): 
    # your code here
    '''multi=[]
    names=[]
    for x in files:
        names.append(x["name"])
        multi.append(x["size_GB"]*1000*8/x["speed_Mbps"])
        
        #names.sort(key=lambda multi: (multi[1], multi[0])) 
        
        #result=(names,max(multi))
        

    return result
    #None, None'''
    
    names = []
    time = []
    for k in files:
        names.append(k['name'])
        time.append((k['size_GB']*8000)/(k['speed_Mbps']))    
        
    dicc = {}
    for n, t in zip(names, time):
        dicc[n]=t
    
    sort = sorted(dicc.items(), key=lambda x: (x[1],x[0])) #Te ordena por el primer elemento y si son iguales por el segundo
    
    result = []
    time_t = []
    for r, t in sort:
        result.append(r)
        time_t.append(t)
      
    return result, time_t[-1]