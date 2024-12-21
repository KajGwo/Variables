pal = str(input("word ")) 
def pally(pal): 
    for i in range(0, int(len(pal)/2)):
     if pal[i] != pal[len(pal)-i-1]:
        return False
    return True
print(pally(pal))
  
  
