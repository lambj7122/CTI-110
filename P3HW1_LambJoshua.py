# Joshua Lamb

# 3-28-2025

# P3HW1

# This program takes a number grade,
# determines average and displays letter grade for the average.



'''
Get user entered grades for Modules 1-6.
Create a list containing the entered grades.
Determine and display lowest, highest, sum, and average of grades.
Use if/else statements to determine and display a letter grade
based on the numerical average.
'''



# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
count = len(grades)
avg = total / count

print()
print('------------Results------------')
print(f'Lowest Grade:       {low:.1f}')
print(f'Highest Grade:      {high:.1f}')
print(f'Sum of Grades:      {total:.1f}')
print(f'Average:            {avg:.2f}')
print('----------------------------------------')


# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')
    
else:
    print('Your grade is: F')
