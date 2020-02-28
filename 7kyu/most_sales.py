def top3(products, amounts, prices):
    
    revenue=[]
    [revenue.append(a*p) for a,p in zip(amounts,prices)]
    
    dictionary= dict(zip(products, revenue))
    dictionary = sorted(dictionary, key=dictionary.get, reverse=True)

    
    return dictionary[0:3]