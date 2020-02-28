# Directions Reduction

def dirReduc(arr):
    opposite = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    new_path = []
    for direction in arr:
        if new_path and new_path[-1] == opposite[direction]:
            new_path.pop()
        else:
            new_path.append(direction)
    return new_path

# other way

def dirReduc(arr):
    #new approach
    dire = arr
    should_restart=True
    while should_restart:
        should_restart=False
        for index,val in enumerate(dire):
            try:
                if (dire[index+1] == "NORTH" and dire[index] == "SOUTH") or (dire[index] == "NORTH" and dire[index+1] == "SOUTH"):
                    dire.pop(index+1)
                    dire.pop(index)
                    should_restart=True
                elif (dire[index+1] == "EAST" and dire[index] == "WEST") or (dire[index] == "EAST" and dire[index+1] == "WEST"):
                    dire.pop(index+1)
                    dire.pop(index)
                    should_restart=True
            except:
                continue
    return dire