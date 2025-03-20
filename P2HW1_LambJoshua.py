# Joshua Lamb
# 3-1-2025 resubmitted 3-20-2025
# P2HW1
# Python program to calculate travel expenses and show a formatted display.

# I'm not sure why my original submission wouldn't run.  My saved file worked
# for me when I opened it and ran it.  But I may have changed something in the
# file when I was referencing it while working on something else.  The only
# thing I changed for resubmitting was updating the date and assignment name,
# that I had forgotten to do when I first copied the program from P1HW2.


'''
Display explanation of program.
Get budget (budget) from user.
Get destination (dest) from user.
Get estimated cost of gas (gas) from user.
Get estimated cost of accomodations (hotel) from user.
Get estimated cost of food (food) from user.
Display "Travel Expenses"
Display "Location: (dest)"
Display "Initial Budget: (budget)"
Display "Fuel: (gas)"
Display "Accomodation: (hotel)"
Display "Food: (food)"
Calculate expenses (expenses) to equal gas plus hotel plus food.
Calculate remaining balance (balance) to equal budget minus expenses.
Display "Remaining Balance: (balance)"
'''



print('This program calculates and displays travel expenses')

budget = float(input('\nEnter Budget: '))

dest = input('\nEnter your travel destination: ')

gas = float(input('\nHow much do you think you will spend on gas? '))

hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))

food = float(input('\nLast, how much do you need for food? '))

print()

print('------------Travel Expenses------------')
print(f'{'Location:':20}{dest}')
print(f'{'Initial Budget:':20}${budget:.2f}')
print(f'{'Fuel:':20}${gas:.2f}')
print(f'{'Accomodation:':20}${hotel:.2f}')
print(f'{'Food:':20}${food:.2f}')
print('---------------------------------------')

print()

expenses = gas + hotel + food

balance = budget - expenses

print(f'{'Remaining Balance:':20}${balance:.2f}')
