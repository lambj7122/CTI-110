##Joshua Lamb

##3-8-2025.  Resubmitted 3-23-25:  added "No change" output

##P3LAB

##Program that gets a money value from the user,
##and calculates the most efficient number of
##dollars, quarters, dimes, nickels, and pennies
##needed to make the given amount of money.



#Get money value from user
money = float(input('Enter an amount of money: $'))

if money > 0:

    #Convert money value to whole number
    money = round(money * 100)

    #Determine how many coins are needed
    dollars = money // 100
    money = money - (dollars * 100)

    quarters = money // 25
    money = money - (quarters * 25)

    dimes = money // 10
    money = money - (dimes * 10)

    nickels = money // 5
    money = money - (nickels * 5)

    pennies = money

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
    
