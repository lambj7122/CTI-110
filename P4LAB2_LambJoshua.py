# Joshua Lamb
# 3-22-2025
# P4LAB2
# Use a while loop and a for loop together



'''
Get integer from user
Determine if interger is positive or negative
If number is positive, display multiplication table
If number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program
If no, end program
'''



run_again = 'yes'

while run_again != 'no':

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range(1, 12+1):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")

#Loop has broken.  User entered 'no'
print("Program is ending...")
