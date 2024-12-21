a = int(input('Enter lower end: '))
b = int(input('Enter higher end: '))
lis = []
while (a <= b):
    lis.append(a)
    a+=1
zz = [i for i in lis if i % 2 == 0 and i < 0]
print(zz)





