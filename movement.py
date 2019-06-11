import room
from level import dungeon

def move(room,x,y,direction):
    if(direction=="up"):
        if(y==room.lenght-1):
            return 1
        else:
            if(room.tab[x-1][y]=="m"):
                room.add_element("hero",x-1,y)
                room.add_element("blank",x,y)
                return 2
            elif(room.tab[x-1][y]=="b"):
                room.add_element("hero",x-1,y)
                room.add_element("blank",x,y)
                return 3
            elif(room.tab[x-1][y]=="f"):
                room.add_element("hero",x-1,y)
                room.add_element("blank",x,y)
                return 4
            elif(room.tab[x-1][y]=="e"):
                room.add_element("hero",x-1,y)
                room.add_element("blank",x,y)
                return 5
            else:
                room.add_element("hero",x-1,y)
                room.add_element("blank",x,y)
                return 0

    elif(direction=="left"):
        if(x==room.width-1):
            return 1
        else:
            if(room.tab[x][y-1]=="m"):
                room.add_element("hero",x,y-1)
                room.add_element("blank",x,y)
                return 2
            elif(room.tab[x][y-1]=="b"):
                room.add_element("hero",x,y-1)
                room.add_element("blank",x,y)
                return 3
            elif(room.tab[x][y-1]=="f"):
                room.add_element("hero",x,y-1)
                room.add_element("blank",x,y)
                return 4
            elif(room.tab[x][y-1]=="e"):
                room.add_element("hero",x,y-1)
                room.add_element("blank",x,y)
                return 5
            else:
                room.add_element("hero",x,y-1)
                room.add_element("blank",x,y)
                return 0

    elif(direction=="right"):
        if(x==0):
            return 1
        else:
            if(room.tab[x][y+1]=="m"):
                room.add_element("hero",x,y+1)
                room.add_element("blank",x,y)
                return 2
            elif(room.tab[x][y+1]=="b"):
                room.add_element("hero",x,y+1)
                room.add_element("blank",x,y)
                return 3
            elif(room.tab[x][y+1]=="f"):
                room.add_element("hero",x,y+1)
                room.add_element("blank",x,y)
                return 4
            elif(room.tab[x][y+1]=="e"):
                room.add_element("hero",x,y+1)
                room.add_element("blank",x,y)
                return 5
            else:
                room.add_element("hero",x,y+1)
                room.add_element("blank",x,y)
                return 0

    elif(direction=="down"):
        if(y==0):
            return 1
        else:
            if(room.tab[x+1][y]=="m"):
                room.add_element("hero",x+1,y)
                room.add_element("blank",x,y)
                return 2
            elif(room.tab[x+1][y]=="b"):
                room.add_element("hero",x+1,y)
                room.add_element("blank",x,y)
                return 3
            elif(room.tab[x+1][y]=="f"):
                room.add_element("hero",x+1,y)
                room.add_element("blank",x,y)
                return 4
            elif(room.tab[x+1][y]=="e"):
                room.add_element("hero",x+1,y)
                room.add_element("blank",x,y)
                return 5
            else:
                room.add_element("hero",x+1,y)
                room.add_element("blank",x,y)
                return 0