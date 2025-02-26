##Joshua Lamb
##2-26-2025
##P2LAB2
##Code that uses a dictionary to store user input and displays output to the user.

cars = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = cars.keys()

print(keys)
print()
car = input("Enter a vehicle to see it's mpg: ")
print()
print(f"The {car} gets {cars[car]} mpg.")
print()
miles = float(input(f"How many miles will you drive the {car}? "))
print()
gas = miles / cars[car]
print(f"{gas:.2f} gallon(s) of gas are needed to drive the {car} {miles:.1f} miles.")
