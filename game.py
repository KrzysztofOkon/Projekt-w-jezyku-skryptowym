import combat
from turn import fight
import turn
from hero import character
from creature import monster
import room
from level import dungeon
from movement import move
import random
import numpy as np


def game():
    main_loop=int(input("wybierz opcję:\n1.nowa gra\n2.wczytaj grę\n3.wyjdź\n "))
    while(main_loop!=3):
        if (main_loop==1):
            type=input("podaj klasę postaci: \n(mage) (palladyn) (warrior)\n(rouge) (warlock) (priest)\n(hunter) (dk -death knight) (shaman)\n ")
            player=character(1,type)
            map=dungeon()
            counter=0
            a=0
            x=map.layout[0].lenght-1
            y=0
            while(counter!=5):
                map.layout[counter].add_element("hero",map.layout[counter].lenght-1,0)
                while(a!=5):
                    print(map)
                    direction=input("podaj kierunek (left, right, up, down): ")
                    a=move(map.layout[counter],x,y,direction)
                    if a!=1:
                        if direction=="left":
                            x-=1
                        elif direction=="right":
                            x+=1
                        elif direction=="up":
                            y-=1
                        elif direction=="down":
                            y+=1
                        if a==2:
                            type=random.randint(1,3)
                            if type==1:
                                ai=monster(player.level,"skeleton")
                            elif type==2:
                                ai=monster(player.level,"zombie")
                            elif type==3:
                                ai=monster(player.level,"vampire")
                            fight(player,ai)
                        elif a==3:
                            ai = monster(player.level, "boss")
                            fight(player,ai)
                        elif a==4:
                            player.rest()
                    else:
                        print("zly kierunek\n\n")
                counter+=1

        ##elif(main_loop==2):
                ## wczytaj grę


game()