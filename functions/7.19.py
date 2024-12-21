
b = str(input(" write smth: "))
a = []
for char in b:
  count = b.count(char) 
  if count > 1:
    a.append(char)
print(a)
    
  
