from creature import monster


def atack(attacker,target):
    target.lose_hp(attacker.ad)

##mage
def fireball(attacker,target):
    target.lose_hp(attacker.ap*3)
    attacker.lose_mana(40)

def blizzard(attacker,target):
    target.lose_hp(attacker.ap*1.5)
    attacker.lose_mana(30)
    #freeze/stun

##palladyn
def lay_on_hands(attacker,target):
    target.heal(attacker.ap*4)
    attacker.lose_mana(20)

def smite(attacker, target):
    target.lose_hp(attacker.ad+(attacker.ap*1.2))
    attacker.lose_mana(30)
    ##stagger/weaken

##warrior
def shield_slam(attacker, target):
    target.lose_hp(attacker.ad*1.2)
    attacker.lose_mana(30)
    ##stagger/weaken

def mortal_strike(attacker,target):
    target.lose_hp(attacker.ad)
    attacker.heal(attacker.ad)
    attacker.lose_mana(30)

##rouge
def backstab(attacker,target):
    target.lose_hp(attacker.ad*3)
    attacker.lose_mana(40)

def eviscerate(attacker,target):
    target.lose_hp(attacker.ad)
    attacker.lose_mana(10)
    ##bleed

##warlock

##priest

##druid

##death knight

##shaman