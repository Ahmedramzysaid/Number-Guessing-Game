#     Start 
# this module operations using to playing 
# note :-
# 1e9 == 1000000000
# function min ()  to use get lewer number between two numbers 
from operations import ope
# module random  ------> to use function (randint)
import random
print ("Hello Mr ! ")
Name = str(input ("What's your name mr ? ")) 
# Ask  player ----> he want play or not 
answer = str(input("You want to play with me guessing number : ")).lower().capitalize()
# many ----> Attempts 
Attempts = 1
#  res using to best ----> Attempts  and 1e9 is value impossible player achieve 
res =  1e9
# pc choose value between  1 : 10  about shape random  .
pc_number = random.randint(1,10)

# condition if he want play or not 
if answer ==  "No" :
    # this first time ask he do not play .
    print (f"Thanks Mr  {Name} ") 
else :   # answer ----> Yes 
    print("It is very well ") 
     # function min () ----> use to get best Attempts
    res =  min(res  ,ope(pc_number , Name , Attempts) )
    while  True :
          # this loop using he want play again or not 
          answer =  str (input(f"You want play again {Name} :")).lower().capitalize()
          if answer == "Yes" : # he want play again 
              pc_number = random.randint(1,10)
              # function min () ----> use to get best Attempts
              res =  min(res  ,ope(pc_number , Name , Attempts) )
              continue 
          else : # he do not play again 
            # print the total player ---- > beat Attempts
              print(f"Thanks mr {Name} about Participate this is a best score {res}")
              # finction exit () ------> to end program .
              exit ()           
#               End   

        

    
        
    
