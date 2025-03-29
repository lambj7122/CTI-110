#Joshua Lamb
#3-29-2025
#P5LAB
#Program will simulate a customer using a self-checkout machine.

'''
Import random number function.
Define the disperse_change function.
    Determine if change is owed.
    Determine and display how many of each monetary unit is needed to make the change.
Define the main function.
    Generate a random amount of money owed (between 0 and 100 dollars).
    Get amount of cash being put in the self-checkout from user.
    Calculate and display the amount of change owed.
    Call the disperse_change function.
Call the main function.
'''



import random

def disperse_change(change):

    if change > 0:

        #Convert change value to whole number
        change = round(change * 100)

        #Determine how many coins are needed
        dollars = change // 100
        change = change - (dollars * 100)

        quarters = change // 25
        change = change - (quarters * 25)

        dimes = change // 10
        change = change - (dimes * 10)

        nickels = change // 5
        change = change - (nickels * 5)

        pennies = change
        

        if dollars > 0:
            if dollars == 1:
                print(f'{dollars} Dollar')
            else:
                print(f'{dollars} Dollars')

        if quarters > 0:
            if quarters == 1:
                print(f'{quarters} Quarter')
            else:
                print(f'{quarters} Quarters')

        if dimes > 0:
            if dimes == 1:
                print(f'{dimes} Dime')
            else:
                print(f'{dimes} Dimes')

        if nickels > 0:
            if nickels == 1:
                print(f'{nickels} Nickel')
            else:
                print(f'{nickels} Nickels')

        if pennies > 0:
            if pennies == 1:
                print(f'{pennies} Penny')
            else:
                print(f'{pennies} Pennies')

    else:
        print("No change")



def main():
    #Logic goes here

    #Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    #Create variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    #Calculate change owed to customer
    change = money_in - amount_owed
    print(f"Change is: ${change:.2f}")
    print()

    #Call the disperse_change function
    disperse_change(change)



#Call the main function
main()
