
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
        self.ad=20*level
        self.ap=20*level

    def lose_hp(self,x):
        if(x>=self.hp):
            self.dead="dead"
            self.hp=0
        else:
            self.hp-=x

    def lose_mana(self,x):
        self.mana-=x

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
        print("mana: ",self.mana)
        print("is alive?:",self.dead)