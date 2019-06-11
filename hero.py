from creature import monster
import combat

class character:
    def __init__(self,level,type):
        self.exp=0
        self.level = level
        self.type = type
        self.dead = "alive"
        self.ad = 20
        self.ap = 20
        self.max_hp = 100
        self.max_mana = 100
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.update_stats(level,type)


    def update_stats(self,level,type):
        if (type == "mage"):
            self.max_hp = 100 * level
            self.max_mana = 400 * level
            self.ad = 10 * level
            self.ap = 40 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "palladyn"):
            self.max_hp = 250 * level
            self.max_mana = 250 * level
            self.ad = 20 * level
            self.ap = 20 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "warrior"):
            self.max_hp = 400 * level
            self.max_mana = 100 * level
            self.ad = 30 * level
            self.ap = 0 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "rouge"):
            self.max_hp = 200 * level
            self.max_mana = 200 * level
            self.ad = 40 * level
            self.ap = 0 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "warlock"):
            self.max_hp = 250 * level
            self.max_mana = 300 * level
            self.ad = 10 * level
            self.ap = 30 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "priest"):
            self.max_hp = 400 * level
            self.max_mana = 200 * level
            self.ad = 10 * level
            self.ap = 20 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "hunter"):
            self.max_hp = 150 * level
            self.max_mana = 200 * level
            self.ad = 50 * level
            self.ap = 0 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "dk"):
            self.max_hp = 400 * level
            self.max_mana = 200 * level
            self.ad = 35 * level
            self.ap = 0 * level
            self.hp = self.max_hp
            self.mana = self.max_mana

        elif (type == "shaman"):
            self.max_hp = 300 * level
            self.max_mana = 200 * level
            self.ad = 10 * level
            self.ap = 30 * level
            self.hp = self.max_hp
            self.mana = self.max_mana





    def gain_level(self):
        self.level+=1;
        self.exp=0
        self.update_stats(self.level,self.type)

    def gsin_exp(self,x):
        if self.exp+x>=1000:
            self.gain_level()
        else:
            self.exp+=x


    def lose_hp(self,x):
        if(x>=self.hp):
            self.dead="dead"
            self.hp=0
        else:
            self.hp-=x

    def lose_mana(self,x):
        self.mana-=x

    def set_status(self,x):
        self.status=x

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

