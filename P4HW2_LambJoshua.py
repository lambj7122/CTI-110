# Joshua Lamb

# 3-28-2025

# P4HW2

# A program that gets one or more employees' names, hours worked, and pay rate;
# and calculates overtime, overtime pay, regular pay, and gross pay for each employee;
# along with the total number of employees entered,
# and total overtime pay, regular pay, and gross pay for ALL employees entered.



'''
Establish variables for total number of employees, total overtime pay, total regular pay, and total gross pay.
Set variable 'name' to "run program".
Use while loop to ask user to enter either an employee name or "Done" to terminate the program.
Use if/else statement to run or terminate the program.
Get hours worked and pay rate for employee from user.
Calculate overtime hours and pay, regular hours and pay, and gross pay.
Display employee name.
Display hours worked, pay rate, overtime, overtime pay, regular pay, and gross pay;
    and display corresponding amounts.
Calculate total number of employees entered so far,
    and calculate total overtime pay, regular pay, and gross pay for ALL employees entered so far.
When user terminates program,
    display total number of employees entered,
    display total amount paid for overtime, regular hours, and gross, for ALL employees entered.
'''



#Establish variables
tot_num_employees = 0
tot_OT_pay = 0
tot_reg_pay = 0
tot_gross_pay = 0

name = "run program"

#begin while loop
while name != "Done":

    sentinel = '"Done"'

    #Get employee name or terminate program
    name = input(f"Enter employee's name or {sentinel} to terminate: ")

    

    #if/else to run or terminate
    if name != "Done":

        #Get hours worked
        hours = float(input(f"How many hours did {name} work? "))

        #Get pay rate
        rate = float(input(f"What is {name}'s pay rate? "))



        #Determine overtime hours and pay

        if hours > 40:
            OT = hours - 40
        else:
            OT = 0

        OT_rate = rate * 1.5

        OT_pay = OT * OT_rate



        #Calculate regular hours and pay

        reg_hours = hours - OT

        reg_pay = reg_hours * rate



        #Calculate gross pay

        gross_pay = OT_pay + reg_pay



        #Display results
        print()
        print(f'Employee name:   {name}')
        print()
        print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
        print('----------------------------------------------------------------------------------------')
        print(f'{hours:<15.1f}{rate:<12.2f}{OT:<12.1f}{OT_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:<17.2f}')
        print()
        print()



        #Add to totals
        tot_num_employees = tot_num_employees + 1

        tot_OT_pay = tot_OT_pay + OT_pay

        tot_reg_pay = tot_reg_pay + reg_pay

        tot_gross_pay = tot_gross_pay + gross_pay



    else:
        #Terminate program and display totals
        print()
        print(f'Total number of employees entered: {tot_num_employees}')
        print(f'Total amount paid for overtime: ${tot_OT_pay:.2f}')
        print(f'Total amount paid for regular hours: ${tot_reg_pay:.2f}')
        print(f'Total amount paid in gross: ${tot_gross_pay:.2f}')

    
