def fact(x):
    y=1
    while x>0:
        y=y*(x)
        x=x-1
        if x==0:
            break
    return y;
print(fact(6))

