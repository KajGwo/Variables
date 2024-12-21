
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'tuesday'
    elif day_number == 3:
        result = 'Thursday'
    elif day_number == 4:
        result = 'Wednesday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    
    return result

day_number = int(input("what is the daynumber: "))
dn = day_name(day_number)
#
print(f'The name of day {day_number} in the week is {dn}')
