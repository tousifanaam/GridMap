"""
________________
|__|__|__|__|__|
|__|■ |__|__|__|
|__|__|__|__|__|
|__|__|__|__|__|
|__|__|__|■ |__|

"""
from os import system,name
from time import sleep
from random import randint

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def drawgrid(l,b,scatter):
    topline = ""
    for _ in range((b*3)+1):
        topline += " "
    topline += "|\n"

    grid = ""
    for y in range(l):
        grid += " "
        for x in range(b):
            if (x,y) in scatter:
                grid += "■  "
            else:
                grid += "   "
        grid += "|\n"
    bottomline = ""
    for _ in range((b*3)+1):
        bottomline += "_"
    clear()
    return topline + grid + bottomline

a = 20
b = 20
p = 100
while True:
    plots = []
    def op():
        for _ in range(p):
            x = (randint(0,b),randint(0,a))
            plots.append(x)
    op()
    print(drawgrid(a,b,plots),end="")
    points = len(plots) - (len(plots) - len(set(plots)))
    print(f"\n\n\n[*] points: {points}")
    sleep(0.1)