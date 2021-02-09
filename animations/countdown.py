from time import sleep
from os import system
from gridmap import GridMap as g

# merger method
m = g.merge

# create required gridmap objects
zero = m(g.zero(),g.zero())
one = m(g.zero(),g.one())
two = m(g.zero(),g.two())
three = m(g.zero(),g.three())
four = m(g.zero(),g.four())
five = m(g.zero(),g.five())
six = m(g.zero(),g.six())
seven = m(g.zero(),g.seven())
eight = m(g.zero(),g.eight())
nine = m(g.zero(),g.nine())
ten = m(g.one(),g.zero())

grid_obj = [
    ten, nine, eight, seven,
    six, five, four, three,
    two, one, zero]

def countdown():
    for i in grid_obj:
        print(i.grid_without_lines())
        #print(f"[*] Points: {len(i.scat_plot)}")
        #print(f"{i}")
        sleep(1)
        system('cls')

if __name__ == '__main__':
    #start = input("\n[*] Press enter to start.	")
    system('cls')
    countdown()