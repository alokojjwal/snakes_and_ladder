import random
    
def check_ladder(pnt):
    if pnt==2:
        print("ladder and the points is now 23")
        return 23
    elif pnt==6:
        print("ladder and the points is now 45")
        return 45
    elif pnt==20:
        print("ladder and the points is now 59")
        return 59
    elif pnt==57:
        print("ladder and the points is now 96")
        return 96
    elif pnt==22:
        print("ladder and the points is now 72")
        return 72
    elif pnt==77:
        print("ladder and the points is now 92")
        return 92
    else:
        return pnt
           
def check_snakes(pnt):
    if pnt==98:
        print("snake and the points is now 40")
        return 40
    elif pnt==87:
        print("snake and the points is now 49")
        return 49
    elif pnt==84:
        print("snake and the points is now 58")
        return 58
    elif pnt==73:
        print("snake and the points is now 15")
        return 15
    elif pnt==56:
        print("snake and the points is now 8")
        return 8
    elif pnt==50:
        print("snake and the points is now 5")
        return 5
    elif pnt==43:
        print("snake and the points is now 17")
        return 17
    else:
        return pnt
    
    
def won(pnt):
    if pnt==100:
        return True
    else:
        return False
    
    
def snakes():
    player1=input("Enter the name of player 1: ")
    player2=input("Enter the name of player 2: ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(" ")
            print("Hey",player1,"it's your turn")
            x=int(input("Roll the dice: (Enter 1 to roll): "))
            while(1):
                if x!=1:
                    print("Invalid input, try again")
                    x=int(input("Roll the dice: (Enter 1 to roll): "))
                else:
                    break
            dice=random.randint(1,6)
            print("Hey",player1,"your dice shows:",dice)
            pp1=pp1+dice
            print(" ")
            print("Hey",player1,"your score is: ",pp1)
            if pp1>100:
                pp1=pp1-dice
                print("Your points returns to ",pp1)
            else:
                pp1=check_ladder(pp1)
                pp1=check_snakes(pp1)
                if won(pp1):
                    print("Hey",player1,"you won")
                    break
        else:
            print(" ")
            print("Hey",player2,"it's your turn")
            x=int(input("Roll the dice: (Enter 1 to roll): "))
            while(1):
                if x!=1:
                    print("Invalid input, try again")
                    x=int(input("Roll the dice: (Enter 1 to roll): "))
                else:
                    break
            dice=random.randint(1,6)
            print("Hey",player2,"your dice shows:",dice)
            pp2=pp2+dice
            print(" ")
            print("Hey",player2,"your score is: ",pp2)
            if pp2>100:
                pp2=pp2-dice
                print("Your points returns to ",pp2)
            else:
                pp2=check_ladder(pp2)
                pp2=check_snakes(pp2)
                if won(pp2):
                    print("Hey",player2,"you won")
                    break
        turn+=1
    
snakes()