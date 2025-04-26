#Joshua Lamb
#4-11-2025
#P5HW
#Character Creation Game

'''
The game allows you to create a character,
battle a monster,
and heal with a doctor.
'''

import random

#Create a character
def create_character():
    
    print()
    name = input("What is your character's Name? ")
    health = int(input("What is your character's beginning Health(50-100)? "))
    attack_power = int(input("What is your character's Maximum Attack Power(1-25)? "))
    
    character = {
        "Name": name,
        "Health": health,
        "Maximum Attack Power": attack_power
        }
    
    return character



#Display all characters
def display_character(character):    
    print()    
    for key, value in character.items():       
        print(f"{key:25}: {value}")
        


#Display intro
def display_intro():
    print()
    print("Welcome to Monster Battle!")
    print()
    print("Create a character and battle the Monster!")



#Create Monster
def create_monster():
    monster = {
        "Name": "Monster",
        "Health": random.randint(50, 100),
        "Maximum Attack Power": random.randint(1, 25)
        }
    return monster



#Create Doctor
def create_doctor():
    doctor = {
        "Name": "Doctor",
        "Health": random.randint(50, 100),
        "Maximum Healing Power": random.randint(1, 25)
        }
    return doctor



#Attack the Monster
def attack(attacker, defender):
    power = random.randint(1, attacker["Maximum Attack Power"])
    defender["Health"] = defender["Health"] - power
    print()
    print(f"You attack the Monster with {power} power!")
    print(f"Monster's health = {defender["Health"]}")



#Defend an attack
def defend(attacker, defender):
    damage = random.randint(1, attacker["Maximum Attack Power"])
    defender["Health"] = defender["Health"] - damage
    print()
    print(f"You take {damage} damage during the attack!")
    print(f"{defender["Name"]}'s health = {defender["Health"]}")



#Heal with the Doctor
def heal(healer, player):
    healing = random.randint(1, healer["Maximum Healing Power"])
    player["Health"] = player["Health"] + healing
    healer["Health"] = healer["Health"] - healing
    print()
    print(f"You have gained {healing} Health from the Doctor.")
    print(f"The Doctor has {healer["Health"]} Health remaining.")
    print(f"{player["Name"]}'s health = {player["Health"]}")



#Main function
def main():

    character_list = []

    display_intro()

    monster = create_monster()
    character_list.append(monster)

    doctor = create_doctor()
    character_list.append(doctor)

    #Main game play
    while True:
        print()
        print("1.  Create a character")
        print("2.  Display all characters")
        print("3.  Battle the Monster")
        print("4.  Heal with the Doctor")
        print("5.  Display intro")
        print("6.  Reset characters")
        print("7.  Exit the game")
        print()
        choice = (input("Choose an option (1-7): "))

        #Create a character
        if choice == "1":
            if len(character_list) >= 3:
                print()
                print("Character already created!")
                answer = input("Would you like to erase the current character and start over? (y/n): ")
                if answer == "y":
                    character_list.remove(new_character)
                    print()
                    print("Character erased...")
                    display_intro()
                else:
                    print()
                    print("The game continues...")
            else:       
                new_character = create_character()
                character_list.append(new_character)
                print()
                print("New character created:")
                display_character(new_character)

        #Display all characters        
        elif choice == "2":
            print()
            print("Current characters:")
            for item in character_list:
                display_character(item)

        #Battle the Monster
        elif choice == "3":
            if len(character_list) < 3:
                print()
                print("Please create a new character...")
            else:
                attacker = new_character
                defender = monster
                attack(attacker, defender)

                if monster["Health"] > 0:
                    attacker = monster
                    defender = new_character
                    defend(attacker, defender)
                    
                    if new_character["Health"] > 0:
                        print()
                        print("The game continues...")
                    else:
                        print()
                        print("You have been defeated by the Monster!")
                        print()
                        answer = input("Would you like to play again? (y/n): ")
                        if answer == "n":
                            print()
                            print("Thank you for playing Monster Battle!")
                            break
                        
                        else:
                            character_list.remove(new_character)
                            character_list.remove(monster)
                            character_list.remove(doctor)
                            monster = create_monster()
                            character_list.append(monster)
                            doctor = create_doctor()
                            character_list.append(doctor)
                            display_intro()
                else:
                    print()
                    print("You have defeated the Monster!")
                    print()
                    answer = input("Would you like to play again? (y/n): ")
                    if answer == "n":
                        print()
                        print("Thank you for playing Monster Battle!")
                        break
                        
                    else:
                        character_list.remove(new_character)
                        character_list.remove(monster)
                        character_list.remove(doctor)
                        monster = create_monster()
                        character_list.append(monster)
                        doctor = create_doctor()
                        character_list.append(doctor)
                        display_intro()

        #Heal with the Doctor        
        elif choice == "4":
            if len(character_list) < 3:
                print()
                print("Please create a new character...")
            else:
                if doctor["Health"] <= 0:
                    print()
                    print("The Doctor has no more Health to provide!")
                else:
                    healer = doctor
                    player = new_character
                    heal(healer, player)

        #Display intro
        elif choice == "5":
            display_intro()

        #Reset characters
        elif choice == "6":
            print()
            answer = input("Are you sure you want to reset the characters? (y/n): ")
            if answer == "y":
                print()
                print("Characters reset...")
                if len(character_list) > 2:
                    character_list.remove(new_character)
                    character_list.remove(monster)
                    character_list.remove(doctor)
                    monster = create_monster()
                    character_list.append(monster)
                    doctor = create_doctor()
                    character_list.append(doctor)
                    display_intro()
                else:
                    character_list.remove(monster)
                    character_list.remove(doctor)
                    monster = create_monster()
                    character_list.append(monster)
                    doctor = create_doctor()
                    character_list.append(doctor)
                    display_intro()
            else:
                print()
                print("The game continues...")

        #Exit the game
        elif choice == "7":
            print()
            answer = input("Are you sure you want to quit? (y/n): ")
            if answer == "y":
                print()
                print("Thank you for playing Monster Battle!")
                break
                
            else:
                print()
                print("The game continues...")
                

        #Invalid entry.  Try again.
        else:
            print()
            print("Please enter a number 1-7... ")
            
                
main()
