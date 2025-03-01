##Joshua Lamb
##
##3-1-25
##
##P2HW2
##
##Working with Lists



'''
Get grade 1 and add to list.
Get grade 2 and add to list.
Get grade 3 and add to list.
Get grade 4 and add to list.
Get grade 5 and add to list.
Get grade 6 and add to list.
Determine minimum grade, (lowest).
Determine maximum grade, (highest).
Determine sum of grades, (total).
Determine total count of grades in list, (count).
Determine average grade by dividing the sum by the count, (average).
Display "Results"
Display "Lowest grade:" and (lowest).
Display "Highest grade:" and (highest).
Display "Sum of Grades:" and (total).
Display "Average:" and (average).
'''



grades = []

mod1 = float(input('Enter grade for Module 1: '))
grades.append(mod1)

mod2 = float(input('Enter grade for Module 2: '))
grades.append(mod2)

mod3 = float(input('Enter grade for Module 3: '))
grades.append(mod3)

mod4 = float(input('Enter grade for Module 4: '))
grades.append(mod4)

mod5 = float(input('Enter grade for Module 5: '))
grades.append(mod5)

mod6 = float(input('Enter grade for Module 6: '))
grades.append(mod6)

lowest = min(grades)
highest = max(grades)
total = sum(grades)
count = len(grades)
average = total / count

print('\n------------Results------------')
print(f'{'Lowest Grade:':20}{lowest:.1f}')
print(f'{'Highest Grade:':20}{highest:.1f}')
print(f'{'Sum of Grades:':20}{total:.1f}')
print(f'{'Average:':20}{average:.2f}')
print('----------------------------------------')
