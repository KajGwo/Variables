a = int(input('Enter integer number: '))




def sum_digits(a):
    
    #x = sum(int(a) for char in (str(abs(a)).split( -1)))
    x = str(abs(a))
    z = [char for char in x]
    for i in range(len(z)):
        z[i] = int(z[i])
    zz = [i for i in z if i % 2 == 0]
    zzz = [i for i in z if i % 2 == 1]
    if a % 2 == 0:
        print(sum(zz))
    elif a % 2 == 1:
        print(sum(zzz))
     

result = sum_digits(a)
print(result)
