#  module operations 
def ope (pc_number , Name , Attempts) :
        res = 1e9 
        while True :
                # Entre your name player 
         Number_player =  int (input(f"Entre your number mr {Name} "))
         # if player number ==  pc number 
         if Number_player == pc_number :
                # message     Winning 
                 print(f"You Win mr {Name}" )
                 # many Attempts in once 
                 print (f"this is  a your Attempts : {Attempts} ")
                 # function min () ----> use to get best Attempts
                 res =  min(res , Attempts)
                 # best Attempts
                 print (f"Best Attempts  {res} ")
                 return  res
        # if Number_player bigger than  pc_number . 
         elif Number_player > pc_number : 
                # note to help player to achieve -----> goal value 
                 print ("Your guess is bigger than number game")
                 # counter  Attempts
                 Attempts +=1  
         # if Number_player lower than  pc_number .
         else :
                 # note to help player to achieve -----> goal value
                 print ("Your guess is lower than number game")
                 # counter  Attempts
                 Attempts +=1    