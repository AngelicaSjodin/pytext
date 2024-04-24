
        
def start():
    while True:
        print("whats your player name?")
        name=input(": ")
        print("weird name but ok "+name+". \n")
        intro()

def intro():
    print("\nyou wake up on a large golden throne surrounded by a buffet full of exotic cheeses and spread \n " 
          "across the stone floor were shiny golden coins. \n")
    
    options=[1,2,3]
    playerChoice=""

    while playerChoice not in options:
        print("Options: 1.feast, 2.fill your pockets w gold, 3.jump out the window ")
        playerChoice=int(input(": "))

        if playerChoice == 1:
            mice()
        elif playerChoice == 2:
            coins()
        elif playerChoice == 3:
            window()
        else:
            print("choose one of the available options.")
                
#------------------------------------------------------------------------------------------------------------------------

def mice():
    print("\nYou chose to enjoy a nice meal of cheese, \n "
          "after eating your 511th slice of cheese u began to notice a squeaking sound coming from the walls..."
          "\n hundreds of mice starts pouring out from a hole in the wall! \n")

    options=[1,2]
    playerChoice=""

    while playerChoice not in options:
        print("Options: 1. Punch mice, 2. Give them cheese as peace a offering ")
        playerChoice=int(input(": "))

        if playerChoice == 1:
            print("\nthe mice became aggressive and ate your left foot :,(\n"
                  "one of them waves their paw at you and challenges you to a 1v1\n")
            global brokenFoot
            brokenFoot=+1
            mice2()

        if playerChoice == 2:
            print("\nthe mice now sees you as their leader, you have gained +1 mouse army\n")
            global mouseArmy
            mouseArmy =+ 1
            castleRoute()

        

def mice2():
    print("\nQuick! Make a move before he does!\n")

    options=[1,2]
    playerChoice=""

    while playerChoice not in options:
        print("Options: 1. Jab punch 2. Jumping back kick")
        playerChoice=int(input(": "))
    
        if playerChoice == 1:
            print("\nSuccess! You knocked out a tooth from that small rodent. \n"
                    "The other mice fled in horror.\n")
            castleRoute()

        if playerChoice == 2:
            print("\nYou tried to do a jumping back kick but faild because your opponent is barely 10cm tall. \n"
                "The mouse ate your other foot and you died an awful death surrounded by cheese and stinky mice...\n"
                "DEATH ENDING 9/9")
            break

        


def coins():
    print("\nYou ignored the cheese and started picking up coin after coin.\n"
          "You gained a total of 3 gold coins.\n")
    global goldCoins
    goldCoins = 1
    castleRoute()

def window():
    print("\nu thought it would be a good idea to jump out the window...?\n"
          "As your body falls thru the sky you see two possible landing spots.\n")    

    options=[1,2]
    playerChoice=""

    while playerChoice not in options:
        print("Options: 1. The castles crocodile infested moat (vallgrav) 2. The castles courtyard")
        playerChoice=int(input(": "))
    
        if playerChoice == 1:
            print("\n A big splash into the cold water. \n")
            crocodile()

        if playerChoice == 2:
            print("\n ... \n"
                "You hit the stone hard ground and turned into a mushy lump of meat\n"
                "why did you pick the courtyard?\n"
                "DEATH ENDING 9/9\n")
            break

        

#------------------------------------------------------------------------------------------------------------------------------------

def crocodile():
    print("\nYou're also starting to feel a large pain coming from your left leg, it's probably boken ops...\n"
        "And now you also see a large crocodile swimming towards you, life could not get any better.\n"
        "What do you do?\n")
    global brokenFoot
    brokenFoot=+1
    options=[1,2]
    playerChoice=""

    while playerChoice not in options:
        print("Options: 1. Let the crocodile come closer 2. swim away from the crocodile")
        playerChoice=int(input(": "))

        if playerChoice == 1:
            print("\nAs the crocodile comes closer he gives you puppy eyes.\n"
                  "Such a cute corcodile can't be evil, so you deicide to let him take you away.\n")
            witch()

        if playerChoice == 2:
            print("\nYou start to scream in horror and try uour best to swim away in the other direction.\n"
                  "Some guards seem to have heard your screams and approach you.\n"
                  "helping you out of the cold waters.")
            guards()

        

def castleRoute():
    print("\nafter you are done with the room you make your way down the castles large stairway.\n"
          "Finally arriving at the castles courtyard you notice two groups of people.\n"
          "a young beautiful lady and some guards patrolling the grounds, which one do you approach?\n")

    options=[1,2]
    playerChoice=""

    while playerChoice not in options:
        print("Options: 1. Lady 2. Guards")
        playerChoice=int(input(": "))

        if playerChoice == 1:
            print("\nYou quickly fix your hair before going up to her\n")
            lady()
        if playerChoice == 2:
            print("\nyou let out a weak 'hElO' to the guards\n")
            guards()

        
#-------------------------------------------------------------------------------------------------------------------------------------
def lady():
    print("\nShe looks you up and down with a worring face.\n"
          "How will you sweep her off her feet?\n")
    
    if goldCoins == 1:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. Wink and offer a gold coin 2. thy bottom is rounder than thy apple ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nShe eagerly takes the coin out of your hand and whips out a marriage contract.\n")
                marriage()
                
            if playerChoice == 2:
                print("\n...\n"
                      "she calls the guards on your ass.\n")
                guards()
                
    
    elif mouseArmy == 1: 
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. flex your mouse army 2. Whats up? ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nShe was appalled by mice coming out of your pantaloons.\n"
                      "She runs to the guards with tears in her eyes.\n")
                guards()
                
            if playerChoice == 2:
                print("\n...\n"
                      "The sky.\n"
                      "She then walks off leaving you with the guards...\n")
                guards()
    
    else:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. Chicken out")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nYou decide you have no balls and goes to the guards instead.\n")
                guards()

            else: print("pick a choice bro")
    
def guards():
    print("\n The guards looks at you with sus.\n"
          "They might think you are a russian spy, rasputini.\n"
          "How do you get out of the tricky situation?\n")
    
    if goldCoins == 1:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. convince them you are also a guard 2. try to bribe with gold. ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nNo way is that you Garry?!\n"
                     "Where have you been broski we thought \n"
                     "we lost you in the great vietnam war!\n" )
                garry()
                
            if playerChoice == 2:
                print("\nThey look at you with most utter chock.\n"
                      "How dare you think the kings men are so easily bribed with?!\n")
                prison()
    
    if brokenFoot == 1:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. Ask them if they could heal your foot. 2. Convince them you are also a guard. ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nThey look at eachother and laugh out loud.\n")
                beggar()
                
            if playerChoice == 2:
                print("\nGarry is that you? :DD\n")
                garry()
    
    if mouseArmy == 1:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. You attack them using your cool mouse army! 2. Convince them you are also a guard. ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nThousands of mice rush out to fight the guards in your honor!\n")
                freedom()
                
            if playerChoice == 2:
                print("\nWhat are you Garry the guard? Why didn't you say so from the beginning?\n")
                garry()
def witch():
    print("\nAfter a while the croc leave you outside a hut made out of mud adn twigs.\n"
          "The door to the hut automatically opens upon your arrival and \n"
          "before you stands a witch!\n")
    if goldCoins == 1:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. She looks so hideous you to to pay her to go away. 2.Ask to be her apprentice. ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nShe truns red of anger and curses you for all eternity! D:\n")
                cursed()
                
            if playerChoice == 2:
                print("\nShe looks at you for 30 mins and then agrees! Yippie!\n")
                youAreAWizardHarry()
    
    if brokenFoot == 1:
        options=[1,2]
        playerChoice=""

        while playerChoice not in options:
            print("Options: 1. Ask to be her apprentice. 2. Show her your mangeled foot. ")
            playerChoice=int(input(": "))

            if playerChoice == 1:
                print("\nShe tickles you and says yes.\n")
                youAreAWizardHarry()
                
            if playerChoice == 2:
                print("\nShe looks at you and says,ewwwwww\n")
                blessed()
#-------------------------------------------------------------------------------------------------------------------------------------
# ends

def marriage():
    print("\nShe signs the contract thinking she married rich. \n"
    "tho little did she know you only hade two gold coins left to your name...\n"
    "MARRIAGE ENDING 1/9\n")


def beggar():
    print("\n They think you are a beggar who has wandered into the castle by mistake.\n"
          "They pick you up and throw you into the street below the castle.\n"
          "You think to yourself, damn\n "
          "BEGGAR ENDING 2/9\n")
    
def prison():
    print("\nThey knock you out cold and when you wake up you are in a prison cell...\n"
          "PRISON ENDING 3/9\n")

def freedom():
    print("\nThe guards runs away screaming in fear.\n"
          "You are now free to leave the castle! yippie!\n"
          "FREEDOM ENDING 4/9\n")
    
def blessed():
    print("\nDisgusted by your wounds she heals you and also give you a wonderful huge mustach!!\n"
          "You can feel yourself getting stonger by the mustach."
          "BLESSED ENDING 5/9\n")
    
def cursed():
    print("\nThe curse turned you into a bald walking stick...\n"
          "CURSED ENDING 6/9\n")

def garry():
    print("\nYou continue to pretend being their great friend Garry for all eternity...\n"
          "GARRY ENDING 7/9\n")
    
def youAreAWizardHarry():
    print("\nYour first mission as a powerful witch apprentice is to sweep the floor.\n"
          "YOU ARE A WIZARD HARRY ENDING 8/9\n")

def pandan():
    print("ok")
#c = coins
#m = mouse army 
#b = brokn leg or missing foot 
goldCoins=0
mouseArmy=0
brokenFoot=0


start()  