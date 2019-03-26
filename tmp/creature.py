##dict warrior
## hp mnoznik 2
## mana mnoznik 0.5

##dict rouge
## hp mnoznik 1.25
## mana mnoznik 1.25

## dict mage
## hp mnoznik 0.5
## mana mnoznik 2

class monster:
    def __init__(self,level,type):
        self.level=level
        self.type=type
        self.max_hp=100*level
        self.max_mana=100*level
        self.hp=self.max_hp
        self.mana=self.max_mana
        ##self.status=""
        self.dead="alive"

    def lose_hp(self,x):
        if(x>=self.hp):
            self.dead="dead"
            self.hp=0
        else:
            self.hp-=x

    def rest(self):
        self.hp=self.max_hp
        self.mana=self.max_mana

    def heal(self,x):
        if self.hp+x>self.max_hp:
           self.hp=self.max_hp
        else:
            self.hp+=x

    def resore_mana(self,x):
        if self.hp+x>self.max_mana:
            self.mana=self.max_mana
        else:
            self.mana+=x

    def show_stats(self):
        print("hp: ",self.hp)
        print("is alive?:",self.dead)


aa=creature(1,1)
