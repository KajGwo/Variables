def sum_digits(a):
    
    #x = sum(int(a) for char in (str(abs(a)).split( -1)))
    x = str(abs(a))
    z = [char for char in x]
    for i in range(len(z)):
        z[i] = int(z[i])
    y = sum(z)   

        

    return y

a = int(input('Enter integer number: '))
result = sum_digits(a)
print("The sum of the digits in the number", a,  "is", result)

