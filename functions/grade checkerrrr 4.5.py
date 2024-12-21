##
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif 18 > points >= 14:
        grade = 'Good'
    elif 14 > points >= 10:
        grade = 'Satisfactory'
    elif points > 10:
        grade = 'Fail'
    
    return grade

points = int(input('Enter points number: '))
final_grade = pts_to_grade(points)
print(f'You scored {points} points on the test. Your final grade is {final_grade}')