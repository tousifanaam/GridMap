from collections import deque
from time import time


class GridMap:
    """
    return: string with points on grid. run >>> print(GridMap.demo)


    ~ ver_len -> type: int, vertical length

    ~ hor_len -> type: int, horizontal length

    ~ scat_plot -> type: list, list_of: tuples, tuple_of: two int
                   example: [(2,3),(1,3),(0,4)]

    ~ lines -> type: bool, default: False,
               if True: display with grid lines
               if False: display without the grid lines
    """

    __version__ = 0.2

    demo = """
    A blank 5x5 grid:

        0  1  2  3  4
      ________________
    0 |__|__|__|__|__|
    1 |__|__|__|__|__|
    2 |__|__|__|__|__|
    3 |__|__|__|__|__|
    4 |__|__|__|__|__|

    After plotting [(2,3),(1,3),(0,4)]

        0  1  2  3  4
      ________________
    0 |__|__|__|__|__|
    1 |__|__|__|__|__|
    2 |__|__|__|__|__|
    3 |__|■_|■_|__|__|
    4 |■_|__|__|__|__|

    """

    def __init__(self, ver_len, hor_len, scat_plot=[], lines=False, char="■"):
        self.ver_len = int(ver_len)
        self.hor_len = int(hor_len)
        self.scat_plot = scat_plot
        self.plot_count = len(self.scat_plot)
        self.char = char
        self.lines = lines

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        if self.lines == True:
            return self.grid_with_lines()
        else:
            return self.grid_without_lines()

    def grid_with_lines(self):
        topline = ""
        for _ in range((self.hor_len*3)+1):
            topline += "_"
        topline += "\n"
        grid = ""
        for y in range(self.ver_len):
            grid += "|"
            for x in range(self.hor_len):
                if (x, y) in self.scat_plot:
                    grid += f"{self.char}_|"
                else:
                    grid += "__|"
            grid += "\n"
        return topline + grid

    def grid_without_lines(self, border=False):
        topline = ""
        for _ in range((self.hor_len*3)+1):
            topline += " "
        topline += "\n"
        if border == True:
            topline += "\n"
        grid = ""
        for y in range(self.ver_len):
            grid += " "
            for x in range(self.hor_len):
                if (x, y) in self.scat_plot:
                    grid += f"{self.char}  "
                else:
                    grid += "   "
            grid += "\n"
        bottomline = ""
        if border == True:
            for _ in range((self.hor_len*3)+1):
                bottomline += "_"
        return topline + grid + bottomline

    def vflip(self):
        """
        vertically flip a GridMap object

        From:
        ________________
        |__|__|__|__|__|
        |x_|x_|x_|__|__|
        |x_|__|__|__|__|
        |x_|x_|__|__|__|
        |__|__|__|__|__|
        v_len = 5, h_len = 5
        Plots: [(0, 1), (1, 1), (2, 1), (0, 2), (0, 3)]

        To:
        ________________
        |__|__|__|__|__|
        |x_|x_|__|__|__|
        |x_|__|__|__|__|
        |x_|x_|x_|__|__|
        |__|__|__|__|__|
        v_len = 5, h_len = 5
        Plots: [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
        """
        plots = list(
            map(lambda x: (x[0], self.ver_len-x[1]-1), self.scat_plot))
        self.scat_plot = plots

    def hflip(self):
        """
        horizontally flip a GridMap object

        From:
        ________________
        |__|__|__|__|__|
        |__|__|x_|x_|x_|
        |__|__|__|__|x_|
        |__|__|__|x_|x_|
        |__|__|__|__|__|
        v_len = 5, h_len = 5
        Plots: [(2, 1), (3, 1), (4, 1), (4, 2), (3, 3), (4, 3)]

        To:
        ________________
        |__|__|__|__|__|
        |x_|x_|x_|__|__|
        |x_|__|__|__|__|
        |x_|x_|__|__|__|
        |__|__|__|__|__|
        v_len = 5, h_len = 5
        Plots: [(0, 1), (1, 1), (2, 1), (0, 2), (0, 3), (1,3)]
        """
        plots = list(
            map(lambda x: (self.hor_len-x[0]-1, x[1]), self.scat_plot))
        self.scat_plot = plots

    def r_rotate(self):
        """rotate right any gridmap obj"""
        plots = list(map(lambda x: (
            self.ver_len-x[0]-1, x[1]), list(map(lambda x: (x[1], x[0]), self.scat_plot))))
        self.scat_plot = plots

    def l_rotate(self):
        """rotate left any gridmap obj"""
        plots = list(
            map(lambda x: (x[0], self.hor_len-x[1]-1), list(map(lambda x: (x[1], x[0]), self.scat_plot))))
        self.scat_plot = plots

    def addrow_down(self, n: int = 1):

        self.ver_len += n
        self.scat_plot = [(i[0], i[1]) for i in self.scat_plot]

    def addrow_up(self, n: int = 1):

        self.ver_len += n
        self.scat_plot = [(i[0], i[1] + n) for i in self.scat_plot]

    def addrow(self, n: int = 1):

        self.ver_len += n
        self.scat_plot = [(i[0], i[1] + n // 2) for i in self.scat_plot]

    def addcolumn_right(self, n: int = 1):

        self.hor_len += n
        self.scat_plot = [(i[0], i[1]) for i in self.scat_plot]

    def addcolumn_left(self, n: int = 1):

        self.hor_len += n
        self.scat_plot = [(i[0] + n, i[1]) for i in self.scat_plot]

    def addcolumn(self, n: int = 1):

        self.hor_len += n
        self.scat_plot = [(i[0] + n // 2, i[1]) for i in self.scat_plot]

    @staticmethod
    def merge(a, b=None, force_merge=False, char="■"):
        """a,b: type: Gridmap object
        merge b to right of a"""
        if type(a) == GridMap and b == None:
            return a
        if type(a) != GridMap or type(b) != GridMap:
            raise TypeError(
                "GridMap.merge - Argument(s) not a GridMap object.")
        if not a.lines:
            a = GridMap(a.ver_len, a.hor_len, a.scat_plot, True)
        if not b.lines:
            b = GridMap(b.ver_len, b.hor_len, b.scat_plot, True)
        m, n = a, b
        a = str(a).split("\n")
        b = str(b).split("\n")
        error, switch = False, False
        if len(a) != len(b):
            error = True
            if len(a) < len(b):
                m, n = (n, m)
                switch = True
            if (m.ver_len - n.ver_len) % 2 == 0:
                n.addrow(m.ver_len - n.ver_len)
                error = False
        if error and force_merge:
            n.addrow(m.ver_len - n.ver_len)
            n.addrow_up(m.ver_len - n.ver_len)
            error = False
        if switch:
            a, b = (n, m)
        else:
            a, b = (m, n)
        a = str(a).split("\n")
        b = str(b).split("\n")
        if error:
            raise ValueError(
                f"{len(a) - 2} & {len(b) - 2} - Unequal vertical length combination") from None
        res = []
        for i in range(len(a)):
            res.append(a[i] + b[i][1:])
        l = len(res) - 2
        b = int((len(res[1]) - 1) / 3)
        del res[0]
        del res[-1]
        res = res[::-1]
        plots = []
        y = 0
        while res:
            check = list(res.pop())
            del check[0]
            cross_found = False
            x = 0
            for i in check:
                if i == char:
                    cross_found = True
                if i == "|":
                    if cross_found:
                        plots.append((x, y))
                    x += 1
                    cross_found = False
            y += 1
        return GridMap(l, b, plots, True)

    @classmethod
    def merge_many(cls, *args, force_merge=False, char="■"):
        "merge multiple Gridmap objects together"
        args = list(args)
        foo = args.pop()
        while args:
            foo = cls.merge(foo, args.pop(),
                            force_merge=force_merge, char=char)
        return foo

    @staticmethod
    def zero():
        """return: zero as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (1, 5), (2, 5), (5, 5), (6, 5), (1, 6), (2, 6), (5, 6), (6, 6), (1, 7),
                 (2, 7), (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def one():
        """return: one as a 14*8 Gridmap Object"""
        plots = [(3, 1), (4, 1), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (3, 4), (4, 4), (3, 5), (4, 5), (3, 6), (4, 6), (3, 7), (4, 7), (3, 8),
                 (4, 8), (3, 9), (4, 9), (3, 10), (4, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def two():
        """return: two as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (5, 4), (6, 4), (5, 5), (6, 5), (4, 6), (5, 6), (3, 7), (4, 7),
                 (5, 7), (2, 8), (3, 8), (4, 8), (1, 9), (2, 9), (3, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def three():
        """return: three as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (5, 5), (6, 5), (5, 6), (6, 6),
                 (4, 7), (5, 7), (5, 8), (6, 8), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def four():
        """return: four as a 14*8 Gridmap Object"""
        plots = [(6, 1), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3), (3, 4), (4, 4), (5, 4), (6, 4), (2, 5), (3, 5), (5, 5), (6, 5), (1, 6), (2, 6), (5, 6), (6, 6), (1, 7),
                 (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (5, 9), (6, 9), (5, 10), (6, 10), (5, 11), (6, 11), (5, 12), (6, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def five():
        """return: five as a 14*8 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7), (2, 7),
                 (3, 7), (4, 7), (5, 7), (6, 7), (5, 8), (6, 8), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def six():
        """return: six as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (1, 7), (2, 7), (3, 7), (4, 7),
                 (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def seven():
        """return: seven as a 14*8 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4), (4, 5),
                 (5, 5), (6, 5), (3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (3, 8), (4, 8), (3, 9), (4, 9), (3, 10), (4, 10), (3, 11), (4, 11), (3, 12), (4, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def eight():
        """return: eight as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (2, 6), (3, 6), (4, 6), (5, 6), (1, 7), (2, 7),
                 (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def nine():
        """return: nine as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (1, 5), (2, 5), (5, 5), (6, 5), (1, 6), (2, 6), (3, 6),
                 (4, 6), (5, 6), (6, 6), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (5, 8), (6, 8), (5, 9), (6, 9), (1, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14, 8, plots, True)

    @staticmethod
    def colon():
        """return: nine as a 14*5 Gridmap Object"""
        plots = [(1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5),
                 (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10)]
        return GridMap(14, 5, plots, True)

    @staticmethod
    def space():
        """return: space as a 14*8 Gridmap Object"""
        plots = []
        return GridMap(14, 8, plots, True)

    @staticmethod
    def period():
        """return: period as a 14*5 Gridmap Object"""
        plots = [(1, 9), (2, 9), (3, 9), (1, 10), (2, 10), (3, 10),
                 (1, 11), (2, 11), (3, 11), (1, 12), (2, 12), (3, 12)]
        return GridMap(14, 5, plots, True)

    @staticmethod
    def comma():
        """return: comma as a 14*5 Gridmap Object"""
        plots = [(1, 7), (2, 7), (3, 7), (1, 8), (2, 8), (3, 8), (1, 9), (2, 9),
                 (3, 9), (2, 10), (3, 10), (2, 11), (3, 11), (1, 12), (2, 12)]
        return GridMap(14, 5, plots, True)

    @staticmethod
    def semicolon():
        """return: semi-comma as a 14*5 Gridmap Object"""
        plots = [(1, 3), (2, 3), (3, 3), (1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5), (1, 7), (2, 7), (3, 7),
                 (1, 8), (2, 8), (3, 8), (1, 9), (2, 9), (3, 9), (2, 10), (3, 10), (2, 11), (3, 11), (1, 12), (2, 12)]
        return GridMap(14, 5, plots, True)

    @staticmethod
    def parenthesis(left: bool, right: bool):
        """return: parenthesis as a 14*5 Gridmap Object"""
        plots = [(3, 1), (4, 1), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6),
                 (1, 7), (2, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (2, 11), (3, 11), (4, 11), (3, 12), (4, 12)]
        if left:
            return GridMap(14, 5, plots, True)
        elif right:
            foo = GridMap(14, 5, plots, True)
            foo.hflip()
            return foo

    @staticmethod
    def equals():
        """return: equals sign as a 14*5 Gridmap Object"""
        plots = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                 (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9)]
        return GridMap(14, 5, plots, True)

    @staticmethod
    def t_upper():
        """return: uppercase T as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (4, 3), (5, 3),
                 (4, 4), (5, 4), (4, 5), (5, 5), (4, 6), (5, 6), (4, 7), (5, 7), (4, 8), (5, 8), (4, 9), (5, 9), (4, 10), (5, 10), (4, 11), (5, 11), (4, 12), (5, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def o_upper():
        """return: uppercase O as a 14*10 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7),
                 (2, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def u_upper():
        """return: uppercase U as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7), (2, 7), (7, 7), (8, 7),
                 (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def s_upper():
        """return: uppercase S as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (1, 7),
                 (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (7, 8), (8, 8), (7, 9), (8, 9), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def i_upper():
        """return: uppercase I as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (4, 3), (5, 3), (4, 4), (5, 4), (4, 5), (5, 5), (4, 6), (5, 6), (4, 7),
                 (5, 7), (4, 8), (5, 8), (4, 9), (5, 9), (4, 10), (5, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def f_upper():
        """return: uppercase F as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5),
                 (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (1, 12), (2, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def c_upper():
        """return: uppercase C as a 14*10 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7),
                 (2, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def k_upper():
        """return: uppercase K as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (5, 3), (6, 3), (7, 3), (1, 4), (2, 4), (4, 4), (5, 4), (6, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (1, 6), (2, 6), (3, 6), (4, 6), (1, 7),
                 (2, 7), (3, 7), (4, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (1, 9), (2, 9), (4, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (7, 10), (1, 11), (2, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def bar():
        """return: bar/pipe as a 14*4 Gridmap Object"""
        plots = [(1, 1), (2, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6),
                 (1, 7), (2, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (1, 12), (2, 12)]
        return GridMap(14, 4, plots, True)

    @staticmethod
    def e_upper():
        """return: uppercase E as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7),
                 (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def x_upper():
        """return: uppercase X as a 14*10 Gridmap Object"""
        plots = [(1, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (3, 3), (6, 3), (7, 3), (8, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (3, 5), (4, 5), (5, 5), (6, 5), (4, 6), (5, 6),
                 (4, 7), (5, 7), (3, 8), (4, 8), (5, 8), (6, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (1, 10), (2, 10), (3, 10), (6, 10), (7, 10), (8, 10), (1, 11), (2, 11), (7, 11), (8, 11), (1, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def n_upper():
        """return: uppercase N as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (7, 2), (8, 2), (1, 3), (2, 3), (3, 3), (7, 3), (8, 3), (1, 4), (2, 4), (3, 4), (4, 4), (7, 4), (8, 4), (1, 5), (2, 5), (3, 5), (4, 5), (7, 5), (8, 5), (1, 6), (2, 6), (4, 6), (5, 6), (7, 6), (8, 6), (1, 7),
                 (2, 7), (4, 7), (5, 7), (7, 7), (8, 7), (1, 8), (2, 8), (5, 8), (6, 8), (7, 8), (8, 8), (1, 9), (2, 9), (5, 9), (6, 9), (7, 9), (8, 9), (1, 10), (2, 10), (6, 10), (7, 10), (8, 10), (1, 11), (2, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def h_upper():
        """return: uppercase H as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
                 (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def d_upper():
        """return: uppercase D as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (7, 3), (1, 4), (2, 4), (6, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7),
                 (2, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (6, 9), (7, 9), (8, 9), (1, 10), (2, 10), (5, 10), (6, 10), (7, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def p_upper():
        """return: uppercase P as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5),
                 (8, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (1, 12), (2, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def r_upper():
        """return: uppercase R as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                 (8, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (1, 9), (2, 9), (4, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (7, 10), (1, 11), (2, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def a_upper():
        """return: uppercase A as a 14*10 Gridmap Object"""
        plots = [(4, 1), (5, 1), (3, 2), (4, 2), (5, 2), (6, 2), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (2, 4), (3, 4), (6, 4), (7, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7), (2, 7), (3, 7), (4, 7),
                 (5, 7), (6, 7), (7, 7), (8, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def v_upper():
        """return: uppercase V as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7),
                 (2, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (3, 9), (6, 9), (7, 9), (8, 9), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (3, 11), (4, 11), (5, 11), (6, 11), (4, 12), (5, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def l_upper():
        """return: uppercase L as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10),
                 (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def y_upper():
        """return: uppercase Y as a 14.10 Gridmap Object"""
        plots = [(1, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (3, 3), (6, 3), (7, 3), (8, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                 (3, 5), (4, 5), (5, 5), (6, 5), (4, 6), (5, 6), (4, 7), (5, 7), (4, 8), (5, 8), (4, 9), (5, 9), (4, 10), (5, 10), (4, 11), (5, 11), (4, 12), (5, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def z_upper():
        """return: uppercase Z as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (7, 3), (8, 3), (7, 4), (8, 4), (6, 5), (7, 5), (5, 6), (6, 6), (4, 7),
                 (5, 7), (3, 8), (4, 8), (2, 9), (3, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def q_upper():
        """return: uppercase Q as a 14.10 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7), (2, 7), (7, 7),
                 (8, 7), (1, 8), (2, 8), (4, 8), (5, 8), (7, 8), (8, 8), (1, 9), (2, 9), (4, 9), (5, 9), (6, 9), (8, 9), (1, 10), (2, 10), (5, 10), (6, 10), (7, 10), (1, 11), (2, 11), (3, 11), (4, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def j_upper():
        """return: uppercase J as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (7, 3), (8, 3), (7, 4), (8, 4), (7, 5), (8, 5), (7, 6), (8, 6), (7, 7), (8, 7),
                 (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def m_upper():
        """return: uppercase M as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (3, 3), (6, 3), (7, 3), (8, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (1, 5), (2, 5), (4, 5), (5, 5), (7, 5), (8, 5),
                 (1, 6), (2, 6), (4, 6), (5, 6), (7, 6), (8, 6), (1, 7), (2, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def w_upper():
        """return: uppercase W as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7), (2, 7), (4, 7), (5, 7), (7, 7), (8, 7), (1, 8),
                 (2, 8), (4, 8), (5, 8), (7, 8), (8, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (1, 10), (2, 10), (3, 10), (6, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def b_upper():
        """return: uppercase B as a 14.10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (1, 7),
                 (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14, 10, plots, True)

    @staticmethod
    def g_upper():
        """return: uppercase G as a 14.10 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7), (7, 7), (8, 7), (1, 8),
                 (2, 8), (5, 8), (6, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12)]
        return GridMap(14, 10, plots, True)

    @classmethod
    def str_to_gm(cls, s, custom_dict: dict = None, uppercase=False, lowercase=False):
        """
        Convert string --> GridMap
        convert strings to GridMap object

        custom_dict -> (optional) type:dict, to add or override
        any existing key in main conversion dict"""

        grid_dict = {
            "0": cls.zero(),
            "1": cls.one(),
            "2": cls.two(),
            "3": cls.three(),
            "4": cls.four(),
            "5": cls.five(),
            "6": cls.six(),
            "7": cls.seven(),
            "8": cls.eight(),
            "9": cls.nine(),
            " ": cls.space(),
            ".": cls.period(),
            ",": cls.comma(),
            ":": cls.colon(),
            ";": cls.semicolon(),
            "(": cls.parenthesis(left=True, right=False),
            ")": cls.parenthesis(left=False, right=True),
            "=": cls.equals(),
            "A": cls.a_upper(),
            "B": cls.b_upper(),
            "C": cls.c_upper(),
            "D": cls.d_upper(),
            "E": cls.e_upper(),
            "F": cls.f_upper(),
            "G": cls.g_upper(),
            "H": cls.h_upper(),
            "I": cls.i_upper(),
            "J": cls.j_upper(),
            "K": cls.k_upper(),
            "L": cls.l_upper(),
            "M": cls.m_upper(),
            "N": cls.n_upper(),
            "O": cls.o_upper(),
            "P": cls.p_upper(),
            "Q": cls.q_upper(),
            "R": cls.r_upper(),
            "S": cls.s_upper(),
            "T": cls.t_upper(),
            "U": cls.u_upper(),
            "V": cls.v_upper(),
            "W": cls.w_upper(),
            "X": cls.x_upper(),
            "Y": cls.y_upper(),
            "Z": cls.z_upper(),
        }
        if custom_dict != None and type(custom_dict) == dict:
            for k, v in custom_dict.items():
                if type(k) == str:
                    if len(k) == 1 and type(v) == GridMap:
                        grid_dict[k] = v
                else:
                    raise ValueError("Custom dict could not be validated.")
        multiple_lines = False
        if uppercase == True:
            s = s.upper()
        if lowercase == True:
            s = s.lower()
        if "\n" in s:
            multiple_lines = True
            if custom_dict != None:
                done_list = [GridMap.str_to_gm(
                    i, custom_dict=custom_dict) for i in s.split("\n")]
            else:
                done_list = [GridMap.str_to_gm(i) for i in s.split("\n")]
        if len(s) == 0:
            return None
        if not multiple_lines:
            try:
                s = [grid_dict[i] for i in s]
            except KeyError as e:
                if custom_dict == None:
                    print(
                        f"Gridmap.str_to_gm: {e} could not assign to any built-in Gridmap obj.")
                else:
                    print(
                        f"Gridmap.str_to_gm: {e} could assign to any Gridmap obj.")
                exit()
            s = deque(s)
            while True:
                l = []
                while s:
                    a = s.popleft()
                    if len(s) != 0:
                        b = s.popleft()
                        l.append(cls.merge(a, b))
                    else:
                        l.append(cls.merge(a))
                if len(l) != 1:
                    s = deque(l)
                else:
                    break
        if multiple_lines:
            h_len = max([i.hor_len for i in done_list])
            v_len = sum([i.ver_len for i in done_list])
            plots = []
            load = 0
            for i in done_list:
                points = i.scat_plot
                for p in points:
                    v = (p[0], p[1]+load)
                    plots.append(v)
                load += i.ver_len
            return GridMap(v_len, h_len, plots, True)
        return(l[0])

    @classmethod
    def random_number(cls):
        """return 2-digit and rarely 1-digit
        true random number as a gridmap object"""
        return cls.str_to_gm(str(time()).split(".")[1][3:5])


if __name__ == '__main__':
    # print(GridMap.str_to_gm("TO\nOU\nSIF").grid_without_lines())
    # print(GridMap(10, 12, [(0,0)]).grid_with_lines())
    pass
