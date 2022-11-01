'''
CTI 110
Larry Dowd
P4HW1
Ask user for six grades, and store them in the list called 'grades'
'''
grades = []

for i in range(6):
    num = str(i + 1)
    grade = float(input('Please enter grade for Module #' + num + ': '))
    grades.append(grade)

average = sum(grades) / len(grades)
print('The lowest grade is:', min(grades))
print('The highest grade is:', max(grades))
print('The sum of grades is:', sum(grades))
print('The average grade is:', average)