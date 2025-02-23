# Joshua Lamb
# 2-23-2025
# P1HW1
# Code to collect info, process info, and display results.

print("-----Calculating Exponents----")
print()

print("Enter an integer as the base value:", end=' ')
base = int(input())
print("Enter an integer as the exponent:", end=' ')
exponent = int(input())
answer1 = base**exponent
print()

print(base, 'raised to the power of', exponent, 'is', answer1, '!!')
print()

print("-----Addition and Subtraction----")
print()

print("Enter a starting integer:", end=' ')
start=int(input())
print("Enter an integer to add:", end=' ')
add=int(input())
print("Enter an integer to subtract:", end=' ')
sub=int(input())
answer2=start+add-sub
print()

print(start, '+', add, '-', sub, 'is equal to', answer2)
