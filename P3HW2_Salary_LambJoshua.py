# Joshua Lamb

# 3-28-2025

# P3HW2

# A program that gets an emplpoyee's name, hours worked, and pay rate;
# and calculates overtime pay, regular pay, and gross pay.



'''
Get employee name, hours worked, and pay rate.
Calculate overtime hours and pay, regular hours and pay, and gross pay.
Display employee name.
Display hours worked, pay rate, overtime, overtime pay, regular pay, and gross pay;
and display corresponding amounts.
'''



#Get employee name
name = input("Enter employee's name: ")

#Get hours worked
hours = float(input("Enter number of hours worked: "))

#Get pay rate
rate = float(input("Enter employee's pay rate: "))



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



print('-------------------------------------')
print(f'Employee name:   {name}')
print()
print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
print('--------------------------------------------------------------------------------------------------')
print(f'{hours:<15.1f}{rate:<12.1f}{OT:<12.1f}{OT_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:<17.2f}')
