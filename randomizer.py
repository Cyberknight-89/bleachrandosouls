##################### note to future self ###########
# the output prints an empty list idk why i think it might be because 
def randomizer():
     import random
    #this code just take input from user and ask if he have a character keep going until 3/3

     while len(my_team) < 3 :
      candidate=random.choice(characters)
      
      comfirmation_user=input(f"randomly picked:\n {candidate}. Do you have this character(yes or no): ")
      if comfirmation_user.lower() == "yes":
             my_team.append(candidate)
             print(f"great {candidate} added to you team. {len(my_team)}/3")
      else:
            print("no problem, picking a different character...")    
randomizer()
print(f"your comfirmed team is:\n{my_team}") 
