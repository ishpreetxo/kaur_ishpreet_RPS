global playerlives 
playerlives = 2
global computerlives
computerlives = 2
global player

#whether player wants to play or not

def winlose(status):       

        #computer asking the player if he wants to play the game again or not

        print("?_?_?")
        print("You " + status + "! Would u like to play again?")
        print("?_?_?")

        Choice = input("Y / N")

        if Choice == "N":
            print("......")
            print ("Better luck next time")
            print("......")
            exit()
        else:
            #reset and restart game
            playerlives = 2
            computerlives = 2
            player = False
