from datetime import datetime
from gridmap import GridMap
from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def main(ampm: bool = False):

    hr, mn, se = str(datetime.now()).split(' ')[1].split('.')[0].split(':')
    print(GridMap.str_to_gm("{0}:{1}:{2}".format(
        hr, mn, se)).grid_without_lines())

    while True:
        _hr, _mn, _se = str(datetime.now()).split(' ')[
            1].split('.')[0].split(':')
        if (hr, mn, se) != (_hr, _mn, _se):
            if ampm:
                if int(_hr) < 12:
                    if int(_hr) == 0:
                        hr, mn, se = ("12", _mn, _se + " AM")
                    else:
                        hr, mn, se = (_hr, _mn, _se + " AM")
                else:
                    hr, mn, se = (str(int(_hr) - 12), _mn, _se + " PM")
            else:
                hr, mn, se = (_hr, _mn, _se)
            clear()
            print(GridMap.str_to_gm("{0}:{1}:{2}".format(
                hr, mn, se)).grid_without_lines())
            if ampm:
                hr, mn, se = (_hr, _mn, _se)


if __name__ == "__main__":
    try:
        main(True)
    except KeyboardInterrupt:
        clear()
