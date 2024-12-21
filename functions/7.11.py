def f(n1, n2, n3):
    if n1 < 0:
       a = False
    elif n2 < 0:
        a = False 
    elif n3 < 0:
        a = False 
    else:
        a = True
    return a 
n1 = int(input("input nr"))
n2 = int(input("input nr"))
n3 = int(input("input nr"))
print(f(n1, n2, n3))





