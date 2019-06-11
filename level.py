import room
import random

class dungeon:
    def __init__(self):
        self.layout=[]
        for i in range(3):
            self.layout.append(room.fight_room())
        self.layout.append(room.boss_room())
        self.layout.append(room.fountain_room())

    def __str__(self):
        tmp=""
        for i in self.layout:
            tmp+=str(i)
        return tmp
