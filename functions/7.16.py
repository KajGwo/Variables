
length = int(input("write smth "))
n = int(input("desired pos "))
def Fibonacci(length):
    f = 0
    s = 1
    z = []
    for i in range(length):     
        z.append(f + s)   
        temp = s
        s = f + s
        f = temp   
        length -= 1
    return(z)


   
if __name__ == "__main__":
    
    print(Fibonacci(length)[n])
  
  
