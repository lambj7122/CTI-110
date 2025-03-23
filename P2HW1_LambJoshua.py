# Joshua Lamb
# 3-1-2025 resubmitted 3-20-2025. Resubmitted 3-23-2025.
# P2HW1
# Python program to calculate travel expenses and show a formatted display.

# 3-23-25: changed quotes in strings.
# It runs in pythontutor.com visual debugger
# I'm writing and running the code in IDLE 3.13.2

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
print()
budget = float(input('Enter Budget: '))
print()
dest = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think you will spend on gas? '))
print()
hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '))
print()

print('------------Travel Expenses------------')
print(f"{'Location:':20}{dest}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accomodation:':20}${hotel:.2f}")
print(f"{'Food:':20}${food:.2f}")
print('---------------------------------------')

print()

expenses = gas + hotel + food

balance = budget - expenses

print(f"{'Remaining Balance:':20}${balance:.2f}")
