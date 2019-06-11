from creature import monster
from hero import character
import combat


def player_move(player,ai):
    print("\n\n1. ataak")
    if player.type=="mage":
        print("2. fireball")
        print("3. blizzard")

    elif player.type=="palladyn":
        print("2. lay on hands")
        print("3. smite")

    elif player.type=="warrior":
        print("2. shield slam")
        print("3. mortal strike")

    elif player.type=="rouge":
        print("2. smoke bomb")
        print("3. eviscerate")

    elif player.type=="warlock":
        print("2. drain soul")
        print("3. hellfire")

    elif player.type=="priest":
        print("2. bless")
        print("3. shadow word")

    elif player.type=="hunter":
        print("2. hunters mark")
        print("3. snipe")

    elif player.type=="dk":
        print("2. frost blade")
        print("3. corrupted blade")

    elif player.type=="shaman":
        print("2. healing ritual")
        print("3. hex")

    tmp=int(input("twój ruch: "))

    if tmp==1:
        combat.attack(player,ai)

    else:

        if player.type == "mage":
            if tmp==2:
                combat.fireball(player,ai)
            elif tmp==3:
                combat.blizzard(player,ai)

        elif player.type == "palladyn":
            if tmp == 2:
                combat.lay_on_hands(player, player)
            elif tmp == 3:
                combat.smite(player, ai)

        elif player.type == "warrior":
            if tmp == 2:
                combat.shield_slam(player, ai)
            elif tmp == 3:
                combat.mortal_strike(player, ai)

        elif player.type == "rouge":
            if tmp == 2:
                combat.smoke_bomb(player, ai)
            elif tmp == 3:
                combat.eviscerate(player, ai)

        elif player.type == "warlock":
            if tmp == 2:
                combat.drain_soul(player, ai)
            elif tmp == 3:
                combat.hellfire(player, ai)

        elif player.type == "priest":
            if tmp == 2:
                combat.bless(player, player)
            elif tmp == 3:
                combat.shadow_word(player, ai)

        elif player.type == "hunter":
            if tmp == 2:
                combat.hunters_mark(player, ai)
            elif tmp == 3:
                combat.snipe(player, ai)

        elif player.type == "shaman":
            if tmp == 2:
                combat.healing_ritual(player, player)
            elif tmp == 3: \
                combat.hex(player, ai)

        elif player.type == "dk":
            if tmp == 2:
                combat.frost_blade(player, ai)
            elif tmp == 3:
                combat.corrupted_blade(player, ai)

def ai_move(ai,player):
        combat.attack(ai,player)


def fight(player,ai):
    while (player.dead!="dead" or ai.dead!="dead"):
        print("\nplayer status:")
        player.show_stats()
        print("\nenemy",ai.type,":")
        ai.show_stats()
        player_move(player,ai)
        if(ai.dead=="dead"):
            break
        else:
            ai_move(ai,player)

