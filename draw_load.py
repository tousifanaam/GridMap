from os import sys
from gridmap import GridMap

def create(filename,l,b):
    with open(filename, "w") as f:
        f.write(str(GridMap(l,b,lines=True)))

if "-c" in sys.argv or "--create" in sys.argv:
    create(input("filename:  "),input("v_len:  "),input("h_len:  "))
    exit()

def loader(filename=None):
    with open(filename) as f:
        f = [i.rstrip("\n") for i in f.readlines() if i != "\n"]
        l = len(f) - 1
        b = int((len(f[1]) - 1) / 3)
        del f[0]
        f = f[::-1]
        plots = []
        y = 0
        while f:
            check = list(f.pop())
            del check[0]
            cross_found = False
            x = 0
            for i in check:
                if i == "x" or i == "■":
                    cross_found = True
                if i == "|":
                    if cross_found == True:
                        plots.append((x,y))
                    x += 1
                    cross_found = False
            y += 1
    print(GridMap(l,b,plots,True))
    print(GridMap(l,b,plots))
    return l,b,plots
       
filename = input("filename:  ")
l, b, plots = loader(filename)
with open(filename, 'a') as x:
    x.write("\n")
    x.write(f"v_len = {l}, h_len = {b}\n")
    x.write(f"\n\nPlots:  \n{plots}")
print("\n--> DONE")