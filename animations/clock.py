from datetime import datetime
from os import system, sys, name
from time import sleep
from random import choice
from gridmap import GridMap as gm

zero = gm.zero()
one = gm.one()
two = gm.two()
three = gm.three()
four = gm.four()
five = gm.five()
six = gm.six()
seven = gm.seven()
eight = gm.eight()
nine = gm.nine()

grid_dict = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
}


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


col_plot = [(1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5),
            (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10)]
col = gm(14, 4, col_plot, lines=True)
colors = False
if "--color" in sys.argv:
    colors = True
alph = ['a', 'b', 'c', 'd']
clear()
prev_color = 'a'
try:
    while True:
        def color():
            while True:
                now = choice(alph)
                if now != prev_color:
                    system(f'color 0{now}')
                    globals()['prev_color'] = now
                    break
        if colors and name == "nt":
            color()
        var = tuple(str(datetime.now()).split(" ")[1].split(".")[0].split(":"))
        h = var[0]
        m = var[1]
        s = var[2]
        hms_grid_obj = gm.merge(gm.merge(gm.merge(gm.merge(grid_dict[h[0]], grid_dict[h[1]]), col), gm.merge(gm.merge(grid_dict[m[0]], grid_dict[m[1]]), col)), gm.merge(grid_dict[s[0]], grid_dict[s[1]]))
        print(hms_grid_obj.grid_without_lines())
        #print(f"\n[*] Points: {len(hms_grid_obj.scat_plot)}")
        sleep(1)
        clear()
except KeyboardInterrupt:
    system('color 0f')
    clear()
    print("Closed.")
