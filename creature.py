
class monster:
    def __init__(self,level,type):
        if (type=="skeleton"):
            self.type_mod=1
        elif(type=="zombie"):
            self.type_mod=1.5
        elif(type=="vampire"):
            self.type_mod=2
        elif(type=="boss"):
            self.type_mod=4
        self.type=type
        self.level=level
        self.max_hp=100*level*self.type_mod
        self.hp=self.max_hp
        self.status=0
        self.dead="alive"
        self.ad=20*level*self.type_mod
        self.epx_reward=250*self.type_mod

    def lose_hp(self,x):
        if(x>=self.hp):
            self.dead="dead"
            self.hp=0
        else:
            self.hp-=x


    def update_status(self,x):
        self.status=str(x)

    def heal(self,x):
        if self.hp+x>self.max_hp:
           self.hp=self.max_hp
        else:
            self.hp+=x


    def show_stats(self):
        print("hp: ",self.hp)
        print("status: ",self.status)
        print("is alive?:",self.dead)