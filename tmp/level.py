import room
import random

class level:
    def __init__(self):
        self.layout=[]
        for i in range(random.randint(3,5)):
            self.layout.append(room.fight_room())
            self.layout.append(room.resting_room())
        self.layout.append(room.boss_room())
        self.layout.append(room.fountain_room())

    def __str__(self):
        tmp=""
        for i in self.layout:
            tmp+=str(i)
        return tmp

