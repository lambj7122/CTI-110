#Joshua Lamb

#3-28-2025

#P4HW1

#Working with Lists and Loops



'''
Create a list of scores called "scores".
Ask user to enter the number of scores they would like to enter.
Create a loop to collect the number of scores the user wants to enter.
For each score entered:
    Evaluate if the score is valid (between 0 and 100),
    If not valid, notify user and ask for valid score to be entered,
    If valid, add the score to the list.
Display lowest score.
Remove lowest score from list and display modified list.
Display average of scores in modified list.
Determine the letter grade for the average score and display it to user.
'''



scores = []

entries = int(input("How many scores do you want to enter? "))

print()

for item in range(entries):
    entry = float(input(f'Enter score #{item + 1}: '))

    while entry < 0 or entry > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        entry = float(input(f'Enter score #{item + 1} again: '))

    scores.append(entry)



print()
print()
print('--------------Results-----------')

print(f'Lowest Score  : {min(scores):.1f}')

scores.remove(min(scores))
print(f'Modified List : {scores}')

average = sum(scores)/len(scores)
print(f'Scores Average: {average:.2f}')

if average >= 90:
    grade = "A"

elif average >= 80:
    grade = "B"

elif average >= 70:
    grade = "C"

elif average >= 60:
    grade = "D"

else:
    grade = "F"

print(f'Grade         : {grade}')
print('----------------------------------')
