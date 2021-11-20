from datetime import datetime
from gridmap import GridMap
from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def main():
    hr, mn, se = str(datetime.now()).split(' ')[1].split('.')[0].split(':')
    print(GridMap.str_to_gm("{0}:{1}:{2}".format(
        hr, mn, se)).grid_without_lines())

    while True:
        _hr, _mn, _se = str(datetime.now()).split(' ')[
            1].split('.')[0].split(':')
        if (hr, mn, se) != (_hr, _mn, _se):
            hr, mn, se = (_hr, _mn, _se)
            clear()
            print(GridMap.str_to_gm("{0}:{1}:{2}".format(
                hr, mn, se)).grid_without_lines())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
