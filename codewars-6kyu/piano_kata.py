# Piano Kata, Part 1

def black_or_white_key(key_press_count):
    
  keyColor = {1 : 'white',2 : 'black',3 : 'white',4 : 'white',
    5 : 'black',6 : 'white',7 : 'black',8 : 'white',9 : 'white',
    10 : 'black',11 : 'white',12 : 'black'}
  a = 0
  b = 0
  if (key_press_count % 88 == 0):
    a = 1
  else:
    a = key_press_count % 88
  
  if (a % 12 == 0):
    b = 12
  else:
    b = a % 12
  
  return keyColor[b]

# other way

def black_or_white_key(key_press_count):

    # david  es un máquina
    black=[2,  5,7,  10,12,14,  17,19,  22,24,26,  29,31,  34,36,38,  41,43,  46,48,50,  53,55,  58,60,62,  65,67,  70,72,74,  77,79,  82,84,86]
    
    if key_press_count%88 not in black:
        return "white"
    else:
        return "black"

