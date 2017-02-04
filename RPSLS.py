"""
This program takes an input and plays RPSLS with that input
"""
import random
REPRESENTATIONS = ("rock","Spock","paper","lizard","scissors")
def name_to_number(choice):
    """
    returns the number associated with a choice
    """
    try:
        return (REPRESENTATIONS.index(choice))
    except ValueError:
        return -1

#def choice_to_number(choice):
#    if(choice=="rock"):
#        return(0)
#    elif(choice=="Spock"):
#        return(1)
#    elif(choice=="paper"):
#        return(2)
#    elif(choice=="lizard"):
#        return(3)
#    elif(choice=="scissors"):
#        return(4)
#    elif:
#        return(-1)

def number_to_name(num):
    """
    Returns the name assosciated with a number
    """
    return REPRESENTATIONS[num]

def winner(player,computer):
    """
    Determines the winner between two inputs, inputs are number
    """
    raw_score=computer-player
    changed_score=raw_score%5
    if(changed_score==1 or changed_score==2):
        return("Bazinga!")
    elif(changed_score==0):
        return("It's a tie.")
    else:
        return("Darn, you win!")

def rpsls(choice):
    """
    Takes an input, creates a random computer input, determines a winner, and
    displays appropriately
    """
    comp_choice=random.randrange(0,5)
    player_choice_num=name_to_number(choice)
    if(player_choice_num<0):
        return "You choose "+choice+".  That's not how you pla\
y the game!"
    win_string=winner(player_choice_num,comp_choice)
    return "You choose "+choice+".  I choose "\
+number_to_name(comp_choice)+".  "+win_string
print(rpsls("Scissors"))
