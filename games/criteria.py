from games import winlose , gameVARS 

def check(player, computer):


    if computer == player:
        # tie - nothing else to compare, so it'll exit
        print("_______")
        print("tie! try again")
        print("_______")

    #the player chooses rock here

    elif player == "rock":
        if computer == "paper":
            print("<<<<<")
            print("you lose! sad!")
            winlose.playerlives = winlose.playerlives - 1
            print(">>>>>")
        else:
            print("<<<<<")
            print("you win! hurray!")
            print(">>>>>")
            winlose.computerlives = winlose.computerlives - 1

    #player now chooses paper 

    elif player == "paper":
        if computer == "scissors":
            print("^__^")
            print("you lose! sad!")
            print("^__^")
            winlose.playerlives = winlose.playerlives - 1
        else:
            print("----")
            print("you win! hurray!")
            print("----")
            winlose.computerlives = winlose.computerlives - 1

    #player chooses scissors for the last time

    elif player == "scissors":
        if computer == "rock":
            print(",,,")
            print("you lose! sad!")
            print(",,,")
            winlose.playerlives = winlose.playerlives - 1
        else:
            print("++++++")
            print("you win! hurray!")
            print("++++++")
            winlose.computerlives = winlose.computerlives - 1

    return (winlose.playerlives, winlose.computerlives)

def new_func():
    playerlives = 2
    computerlives = 2
    return playerlives,computerlives
