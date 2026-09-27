#this code just take input from user and ask if he have a character keep going until 3/3

import random
from character.py import characters
my_team=[]
while len(my_team) < 3 :
    candidate=random.choice(characters)
    if candidate in my_team:
           continue
    comfirmation_user=input(f"randomly picked:\n {candidate}. Do you have this character(yes or no): ")
    if comfirmation_user.lower() == "yes":
        my_team.append(candidate)
        print(f"great {candidate} added to you team. {len(my_team)}/3")
    else:
        print("no problem, picking a different character...")    
print(f"your comfirmed team is:\n{my_team}") 
