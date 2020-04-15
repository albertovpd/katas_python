# Pete, the baker

def cakes(recipe, available):
    # try again
    quantity = []
    for ingredients in recipe:
        if ingredients in available.keys():
            num = available[ingredients]/recipe[ingredients]
            quantity.append(num)
        else:
            return 0
    return min(quantity)