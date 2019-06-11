import random
import numpy
class room:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
        self.tab=numpy.full((width,lenght),"#")


    def add_element(self,element,x,y):
        if element=="monster":
            self.tab[x][y]="m"
        elif element=="boss":
            self.tab[x][y] = "b"
        elif element=="fountain":
            self.tab[x][y] = "f"
        elif element=="exit":
            self.tab[x][y]="e"
        elif element=="hero":
            self.tab[x][y]="h"
        elif element=="blank":
            self.tab[x][y]="#"


    def __str__(self):
        tmp=""
        for i in range(self.lenght):
            for j in range(self.width):
                tmp+="|"+self.tab[i][j]+"|"
            tmp+="\n"
        tmp+="\n\n"
        return(tmp)


def fight_room():
    tmp=room(5,5)
    for i in range(5):
        for j in range(5):
            if random.randint(1,4)==1:
                tmp.add_element("monster",i,j)
    tmp.add_element("exit", 0, 0)
    return tmp

def boss_room():
    tmp=room(3,3)
    tmp.add_element("boss",1,1)
    tmp.add_element("exit",0,0)
    return tmp


def fountain_room():
    tmp = room(3, 3)
    tmp.add_element("fountain", 1, 1)
    tmp.add_element("exit",0,0)
    return tmp
