n = int(input("writ esmth: "))
nnn = []
nn = int(input("write smth: "))
for num in range(2,n):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        nnn.append(num)
print((nnn[nn]))
        
       
