from creature import monster


def attack(attacker,target):
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
    target.lose_hp(attacker.ad+(attacker.ap*0.2))
    attacker.lose_mana(30)
    ##stagger/weaken

##warrior
def shield_slam(attacker, target):
    target.lose_hp(attacker.ad*1.2)
    attacker.lose_mana(30)
    ##stagger/weaken/stun

def mortal_strike(attacker,target):
    target.lose_hp(attacker.ad)
    attacker.heal(attacker.ad)
    attacker.lose_mana(30)

##rouge
def smoke_bomb(attacker,target):
    target.lose_hp(attacker.ad)
    attacker.lose_mana(10)
    ##stun

def eviscerate(attacker,target):
    target.lose_hp(attacker.ad)
    attacker.lose_mana(10)
    ##bleed

##warlock
def drain_soul(attacker,target):
    target.lose_hp(attacker.ap)
    attacker.heal(attacker.ap)
    attacker.lose_mana(5)

def hellfire(attacker,target):
    target.lose_hp(attacker.ap*4)
    attacker.lose_hp(20)
    ##burn

##priest
def bless(attacker,target):
    target.heal(attacker.ap * 6)
    attacker.lose_mana(20)

def shadow_word(attacker,target):
    target.lose_hp(attacker.ap*0.5)
    attacker.lose_mana(30)

##hunter
def hunters_mark(attacker,target):
    attacker.lose_mana(20)
    ##marked

def snipe(attacker,target):
    ##if not marked
    target.lose_hp(attacker.ad * 2)
    ##if marked
    ##target.lose_hp(attacker.ad * 4)
    attacker.lose_mana(40)


##death knight
def frost_blade(attacker,target):
    target.lose_hp(attacker.ad * 2)
    attacker.heal(attacker.ad * 0.2)
    attacker.lose_mana(30)

def corrupted_blade(attacker,target):
    target.lose_hp(attacker.ad)
    attacker.heal(attacker.ad * 0.1)
    attacker.lose_mana(10)
    ##corruption


##shaman
def healing_ritual(attacker,target):
    target.heal(attacker.ap * 2)
    attacker.heal(attacker.ap*2)
    attacker.lose_mana(20)

def hex(attacker,target):
    attacker.lose_mana(20)
    ##hexed