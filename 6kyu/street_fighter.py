# Street Fighter 2 - Character Selection

def street_fighter_selection(fighters, initial_position, moves):
    figthers = [['Ryu','E.Honda','Blanka','Guile','Balrog','Vega'],['Ken','Chun Li','Zangief','Dhalsim','Sagat','M. Bison']]
    final = []
    f = initial_position[0]
    c = initial_position[1]
    
    for move in moves:
        
        if move == 'up':
            f -= 1
            if f < 0:
                f = 0
                a = fighters[f][c]
                final.append(a)
            else:
                a = fighters[f][c]
                final.append(a)
                
        elif move == 'down':
            f += 1
            if f > 1:
                f = 1
                a = fighters[f][c]
                final.append(a)
            else:
                a = fighters[f][c]
                final.append(a)
            
        elif move == 'right':
            c += 1
            
            if c > 5:
                c = 0
                a = fighters[f][c]
                final.append(a)
            else:
                a = fighters[f][c]
                final.append(a)  
        
        elif move == 'left':
            c -= 1
            
            if c < 0:
                c = 5
                a = fighters[f][c]
                final.append(a)
            else:
                a = fighters[f][c]
                final.append(a) 
            
            
            
    return final