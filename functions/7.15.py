
pinroom = str(input("write smth"))
z = [char for char in pinroom]
count = 0 
for char in z:
    if count >= 3:
        break
    elif char == "+":
        count += 1
    elif char == "-":
        count -= 1
if count >= 3:
    x = True
else:
    x = False
   



    
    
print (x)

