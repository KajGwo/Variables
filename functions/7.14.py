###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
num = float(input("first number: ")) 
numm = float(input("second number: "))
operator = input("operator: ")

if operator == "+":
    result = num + numm
elif operator == "-":
    result = num - numm
elif operator == "*":
    result = num * numm
elif operator == "%":
    result = num % numm
elif operator == "**":
    result = num ** numm

# print result
print(f'{num} {operator} {numm}= {result}')