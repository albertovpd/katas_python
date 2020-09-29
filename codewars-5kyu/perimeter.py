# Perimeter of squares in a rectangle

def perimeter(n):
    # your code
    fibo=[0,1]
    for i in range(n):
        fibo.append(fibo[-2]+fibo[-1])
    return (sum(fibo)*4)