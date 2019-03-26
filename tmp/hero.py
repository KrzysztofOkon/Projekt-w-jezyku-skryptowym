from creatue import monster

class character(monster):
    def __init__(self):
        self.exp=0

    def gain_level(self):
        self.level+=1;
        self.exp=0

    def gsin_exp(self,x):
        if self.exp+x>=1000:
            self.gain_level()
        else:
            self.exp+=x

