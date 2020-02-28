# Deodorant Evaporator

def evaporator(content, evap_per_day, threshold):
    day=0
    x=content
    while (x>=content*threshold/100):
    # lo que no se me había ocurrido era evaluar el while con un elemento interior de él
    # nombrar con sentido las variables
    
        x=x*(1-evap_per_day/100)
        day+=1
    
    return day

    