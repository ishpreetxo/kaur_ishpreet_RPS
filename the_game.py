from random import randint
from games import winlose, gameVARS, criteria
gameVARS.computerlives=5
gameVARS.playerlives=5

#loop created to run the game
while gameVARS.player is False:

    #choose any of the 3 to start the game

    gameVARS.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVARS.computer = gameVARS.choices[randint(0, 2)]
    print("#-#-#-#-#-#-#-#-#-#-")
    print("player chose: " + gameVARS.player)
    print("computer chose: " + gameVARS.computer)

    #have to call function check from criteria 

    gameVARS.playerlives, gameVARS.computerlives =  criteria.check(gameVARS.player, gameVARS.computer)      #returning value

    print("=/=/=/=/=")
    print("player life count: " + str(gameVARS.playerlives))
    print("computer life count: " + str(gameVARS.computerlives))
    print("=/=/=/=/=")


    if gameVARS.playerlives == 0:
        #call winorlose here
        winlose.winlose("lose")

    elif gameVARS.computerlives == 0:
        #call winorlose function here
        winlose.winlose("won")  

    gameVARS.player = False

