def rangechecker():
    up = int(input("upper range? "))
    low = int(input("lower range? "))
    num = int(input("num in range? "))
    z = True
    if up >= num >= low:
        z = True
    else:
        z = False 
    return z  

