


import random as R
from PIL import Image

def check_ladder(no):
    #11 3 5  20
    #22 8 26 29
    if no==11:
        return 26
    elif no==3:
        return 22
    elif no==5:
        return 8
    elif no==20:
        return 29
    else:
        return no

def check_snake(no):
    #17 19 21 27
    #4  7  9  1
    if no==17:
        return 4
    elif no==19:
        return 7
    elif no==21:
        return 9
    elif no==27:
        return 1
    else:
        return no


def reached_end(ps):
    return ps==30
        

def roll_dice():
    dice_no=R.randint(1,6)
    return dice_no



def show_img():
    img=Image.open("snakes.jpg")
    img.show()
    
def play():
    end=30
    p1=input("Player 1 Name : ")
    
    p2=input("Player 2 Name : ")
    
    ps1=0
    ps2=0
    turn=0
    while(1):
        
        if turn%2==0:
            print(p1," Your turn",end="")
            c=input("Roll Dice ? y/n")
            if c=="n":
                if ps1>ps2:
                    print(p1," Wins")
                    print(p1 ," Score : ",ps1 )
                    print(p2," Score : ",ps2)
                elif ps1<ps2:
                    print(p2," Wins")
                    print(p1 ," Score : ",ps1 )
                    print(p2," Score : ",ps2)
                else:
                    print("Its a Draw")
                    print(p1 ," Score : ",ps1 )
                    print(p2," Score : ",ps2)
                break
            
                    
            print("Rolling Dice... ")
            dice=roll_dice()
            print("You've Got ",dice)
            ps1+=dice
            #look in map whether a fall or rise
            ps1=check_ladder(ps1)
            ps1=check_snake(ps1)
            
            #check if the player goes beyond the board
            if ps1>end:
                ps1=end
            
            print(p1," Your Score ",ps1,end="\n\n")
            
            if  reached_end(ps1):
                print(p1 ," Won")
                break
        else:
            print(p2," Your turn",end="")
            c=input("Roll Dice ? y/n")
            if c=="n":
                if ps1>ps2:
                    print(p1," Wins")
                    print(p1 ," Score : ",ps1 )
                    print(p2," Score : ",ps2)
                elif ps1==ps2:
                    print(p2," Wins")
                    print(p1 ," Score : ",ps1 )
                    print(p2," Score : ",ps2)
                else:
                    print("Its a Draw")
                    print(p1 ," Score : ",ps1 )
                    print(p2," Score : ",ps2)
                break
            print("Rolling Dice... ")
            dice=roll_dice()
            print("You've Got ",dice)
            ps2+=dice
            #look in map whether a fall or rise
            ps2=check_ladder(ps2)
            ps2=check_snake(ps2)
            
            #check if the player goes beyond the board
            if ps2>end:
                ps2=end
            
            print(p2," Your Score ",ps2,end="\n\n")
            
            if  reached_end(ps2):
                print(p2 ," Won")
                break
    
        turn+=1
    
    
play()    
