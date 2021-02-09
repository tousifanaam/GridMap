import threading
from time import sleep
from os import system,name
from gridmap import GridMap as g
from playsound import playsound

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

sounds = [
    'ten', 'nine', 'eight', 'seven',
    'six', 'five', 'four', 'three',
    'two', 'one', 'zero']

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def countdown():
    for i in range(len(grid_obj)):
        t1 = threading.Thread(target=print(grid_obj[i].grid_without_lines()))
        t2 = threading.Thread(target=playsound(f"{sounds[i]}.wav"))
        t1.start()
        #sleep(0.2)
        t2.start()
        #print(f"[*] Points: {len(i.scat_plot)}")
        #print(f"{i}")
        sleep(1)
        clear()

if __name__ == '__main__':
    #start = input("\n[*] Press enter to start.	")
    clear()
    countdown()