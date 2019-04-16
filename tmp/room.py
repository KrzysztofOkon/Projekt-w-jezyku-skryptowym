import random
class room:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
        self.tab=list()
        tmp=list()
        for i in range(width):
            tmp.append("#")
        for i in range(lenght):
            self.tab.append(tmp)

    def add_element(self,element,x,y):
        if element=="monster":
            self.tab[x][y]="m"
        elif element=="boss":
            self.tab[x][y] = "b"
        elif element=="resting_place":
            self.tab[x][y] = "r"
        elif element=="fountain":
            self.tab[x][y] = "f"


    def __str__(self):
        tmp=("_")*(self.width+2)+"\n"
        for i in range(self.lenght):
            tmp+="|"
            for j in range(self.width):
                print("\n"+"\n"+self.tab[i][j]+"\n"+"\n")
                tmp+=self.tab[i][j]
            tmp +=( "|"+"\n")
        tmp += ("-") * (self.width + 2) + "\n"
        return(tmp)

def fight_room():
    tmp=room(random.randint(3,6),random.randint(3,6))
    for i in range(tmp.lenght):
        for j in range(tmp.width):
            if random.randint(1,4)==1:
                tmp.add_element("monster",i,j)
    return tmp

def boss_room():
    tmp=room(3,3)
    tmp.add_element("boss",1,1)
    return tmp


def resting_room():
    tmp=room(3,3)
    tmp.add_element("resting_place",1,1)
    return tmp

def fountain_room():
    tmp = room(3, 3)
    tmp.add_element("fountain", 1, 1)
    return tmp

aa=fountain_room()
print(aa)
