from time import sleep
from os import system
from gridmap import GridMap

while True:
    ver = 10
    hor = 10
    p = []
    step = 1
    for x in range(hor):
        for y in range(ver):
            p.append((x,y))
    for y in range(ver):
        for x in range(hor):
            p.append((x,y))
        print(GridMap(ver,hor,p,True))
        print(GridMap(ver,hor,p))
        print(f"\n--> Point count: {len(p)}")
        sleep(0.08)
        system('cls')
        if step == 3:
            step = 0
            p = []
        step += 1
        pp = []
        stepp = 1
    break