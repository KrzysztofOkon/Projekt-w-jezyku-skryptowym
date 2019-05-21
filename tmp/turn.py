from creature import monster
import combat


def player_move():

    ##status check


def ai_move():
    ##status check
    if isinstance(ai,monster):
        combat.attack(ai,player)
    ##else (is boss)


def fight(player,ai):
    while (player.dead!="dead" or ai.dead!="dead"):
        player_move()
        if(ai.dead=="dead"):
            break
        else:
            ai_move()

fight()