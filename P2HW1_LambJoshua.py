# Joshua Lamb
# 2-23-2025
# P1HW2
# Python program to calculate travel expenses and show a formatted display.



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
