# Joshua Lamb
# 2-23-2025
# P1HW2
# Python program to calculate and display travel expenses.



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

print('Enter Budget:', end=' ')
budget=int(input())

print()

print('Enter your travel destination:', end=' ')
dest=input()

print()

print('How much do you think you will spend on gas?', end=' ')
gas=int(input())

print()

print('Approximately, how much will you need for accomodation/hotel?', end=' ')
hotel=int(input())

print()

print('Last, how much do you need for food?', end=' ')
food=int(input())

print()

print('------------Travel Expenses------------')

print('Location:', dest)

print('Initial Budget:', budget)

print()

print('Fuel:', gas)

print('Accomodation:', hotel)

print('Food:', food)

print()

expenses=gas+hotel+food

balance=budget-expenses

print('Remaining Balance:', balance)


