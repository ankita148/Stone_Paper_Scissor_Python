import random
# generating comp input

randomNo = random.randint(1, 3)
if randomNo == 1:
    comp = 's'
elif randomNo == 2 :
    comp = 'p'
else:
    comp = 'c'


# game win function 
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        else:
            return False

    elif comp == 'p':
        if you == 's':
            return False
        else:
            return True

    elif comp == 'c':
        if you == 'p':
            return False
        else:
            return True



# display statements
print("----------------------------------------")
print("\nLet's play a game! STONE-PAPER-SCISSOR")
print("-----------------------------------------")
print("\nComp turn - Choose from stone-'s' paper-'p' scissor-'c' ")
you = input("\nYour turn - Choose from stone-'s' paper-'p' scissor-'c' : ")
if ((you =='s') or (you == 'p') or (you == 'c')):


    result = gamewin(comp, you)

    print(f"The comp has chosen - {comp}")

    print(f"You have chosen - {you}")
    if result == True:
        print("Congratulations! You won.")
    elif result == False:
        print("Oh no! You lose.")
    elif result == None:
        print("There is a tie!")
else:
    print(f"'{you}' - this is a wrong input! Play again.\n")
    
