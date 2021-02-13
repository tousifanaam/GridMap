from collections import deque
from time import time

__version__ = 0.2

class GridMap:
    """
    return: string with points on grid. run >>> print(GridMap.demo)


    ~ ver_len -> type: int, vertical length

    ~ hor_len -> type: int, horizontal length

    ~ scat_plot -> type: list, list_of: tuples, tuple_of: ints
                   example: [(2,3),(1,3),(0,4)]

    ~ lines -> type: bool, default: False,
               if True: display with grid lines
               if False: display without the grid lines
    """

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
    
    def __init__(self, ver_len, hor_len, scat_plot=[], lines=False):
        self.ver_len = int(ver_len)
        self.hor_len = int(hor_len)
        self.scat_plot = scat_plot
        self.lines = lines

    def __str__(self):
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
                if (x,y) in self.scat_plot:
                    grid += "■_|"
                else:
                    grid += "__|"
            grid += "\n"
        return topline + grid

    def grid_without_lines(self,border=False):
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
                if (x,y) in self.scat_plot:
                    grid += "■  "
                else:
                    grid += "   "
            grid += "\n"
        bottomline = ""
        if border == True:
            for _ in range((self.hor_len*3)+1):
                bottomline += "_"
        return topline + grid + bottomline

    @staticmethod
    def merge(a,b=None):
        """a,b: type: Gridmap object
        merge b to right of a"""
        if type(a) == GridMap and b == None:
            return a
        if type(a) != GridMap or type(b) != GridMap:
            raise TypeError("GridMap.merge - Argument(s) not a GridMap object.")
            
        a = str(a).split("\n")
        b = str(b).split("\n")
        if len(a) != len(b):
            raise ValueError(f"{len(a)} & {len(b)} - Unequal vertical length combination") from None
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
                if i == "■":
                    cross_found = True
                if i == "|":
                    if cross_found:
                        plots.append((x,y))
                    x += 1
                    cross_found = False
            y += 1
        return GridMap(l,b,plots,True)

    @staticmethod
    def zero():
        """return: zero as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (1, 5), (2, 5), (5, 5), (6, 5), (1, 6), (2, 6), (5, 6), (6, 6), (1, 7), (2, 7), (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def one():
        """return: one as a 14*8 Gridmap Object"""
        plots = [(3, 1), (4, 1), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (3, 4), (4, 4), (3, 5), (4, 5), (3, 6), (4, 6), (3, 7), (4, 7), (3, 8), (4, 8), (3, 9), (4, 9), (3, 10), (4, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def two():
        """return: two as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (5, 4), (6, 4), (5, 5), (6, 5), (4, 6), (5, 6), (3, 7), (4, 7), (5, 7), (2, 8), (3, 8), (4, 8), (1, 9), (2, 9), (3, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def three():
        """return: three as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (5, 5), (6, 5), (5, 6), (6, 6), (4, 7), (5, 7), (5, 8), (6, 8), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def four():
        """return: four as a 14*8 Gridmap Object"""
        plots = [(6, 1), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3), (3, 4), (4, 4), (5, 4), (6, 4), (2, 5), (3, 5), (5, 5), (6, 5), (1, 6), (2, 6), (5, 6), (6, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (5, 9), (6, 9), (5, 10), (6, 10), (5, 11), (6, 11), (5, 12), (6, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def five():
        """return: five as a 14*8 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (5, 8), (6, 8), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def six():
        """return: six as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def seven():
        """return: seven as a 14*8 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4), (4, 5), (5, 5), (6, 5), (3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (3, 8), (4, 8), (3, 9), (4, 9), (3, 10), (4, 10), (3, 11), (4, 11), (3, 12), (4, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def eight():
        """return: eight as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (2, 6), (3, 6), (4, 6), (5, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def nine():
        """return: nine as a 14*8 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (1, 3), (2, 3), (5, 3), (6, 3), (1, 4), (2, 4), (5, 4), (6, 4), (1, 5), (2, 5), (5, 5), (6, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (5, 8), (6, 8), (5, 9), (6, 9), (1, 10), (5, 10), (6, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (2, 12), (3, 12), (4, 12), (5, 12)]
        return GridMap(14,8,plots,True)

    @staticmethod
    def colon():
        """return: nine as a 14*5 Gridmap Object"""
        plots = [(1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10)]
        return GridMap(14,4,plots,True)

    @staticmethod
    def space():
        """return: space as a 14*8 Gridmap Object"""
        plots = []
        return GridMap(14,8,plots,True)

    @staticmethod
    def period():
        """return: period as a 14*5 Gridmap Object"""
        plots = [(1, 9), (2, 9), (3, 9), (1, 10), (2, 10), (3, 10), (1, 11), (2, 11), (3, 11), (1, 12), (2, 12), (3, 12)]
        return GridMap(14,5,plots,True)

    @staticmethod
    def comma():
        """return: comma as a 14*5 Gridmap Object"""
        plots = [(1, 7), (2, 7), (3, 7), (1, 8), (2, 8), (3, 8), (1, 9), (2, 9), (3, 9), (2, 10), (3, 10), (2, 11), (3, 11), (1, 12), (2, 12)]
        return GridMap(14,5,plots,True)

    @staticmethod
    def semicolon():
        """return: semi-comma as a 14*5 Gridmap Object"""
        plots = [(1, 3), (2, 3), (3, 3), (1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5), (1, 7), (2, 7), (3, 7), (1, 8), (2, 8), (3, 8), (1, 9), (2, 9), (3, 9), (2, 10), (3, 10), (2, 11), (3, 11), (1, 12), (2, 12)]
        return GridMap(14,5,plots,True)

    @staticmethod
    def t_upper():
        """return: uppercase T as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (4, 3), (5, 3), (4, 4), (5, 4), (4, 5), (5, 5), (4, 6), (5, 6), (4, 7), (5, 7), (4, 8), (5, 8), (4, 9), (5, 9), (4, 10), (5, 10), (4, 11), (5, 11), (4, 12), (5, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def o_upper():
        """return: uppercase O as a 14*10 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7), (2, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def u_upper():
        """return: uppercase U as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (7, 2), (8, 2), (1, 3), (2, 3), (7, 3), (8, 3), (1, 4), (2, 4), (7, 4), (8, 4), (1, 5), (2, 5), (7, 5), (8, 5), (1, 6), (2, 6), (7, 6), (8, 6), (1, 7), (2, 7), (7, 7), (8, 7), (1, 8), (2, 8), (7, 8), (8, 8), (1, 9), (2, 9), (7, 9), (8, 9), (1, 10), (2, 10), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def s_upper():
        """return: uppercase S as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (7, 8), (8, 8), (7, 9), (8, 9), (7, 10), (8, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def i_upper():
        """return: uppercase I as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (4, 3), (5, 3), (4, 4), (5, 4), (4, 5), (5, 5), (4, 6), (5, 6), (4, 7), (5, 7), (4, 8), (5, 8), (4, 9), (5, 9), (4, 10), (5, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def f_upper():
        """return: uppercase F as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (1, 12), (2, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def c_upper():
        """return: uppercase C as a 14*10 Gridmap Object"""
        plots = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def k_upper():
        """return: uppercase K as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (7, 1), (8, 1), (1, 2), (2, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (5, 3), (6, 3), (7, 3), (1, 4), (2, 4), (4, 4), (5, 4), (6, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (1, 6), (2, 6), (3, 6), (4, 6), (1, 7), (2, 7), (3, 7), (4, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (1, 9), (2, 9), (4, 9), (5, 9), (6, 9), (1, 10), (2, 10), (5, 10), (6, 10), (7, 10), (1, 11), (2, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (7, 12), (8, 12)]
        return GridMap(14,10,plots,True)

    @staticmethod
    def bar():
        """return: bar/pipe as a 14*4 Gridmap Object"""
        plots = [(1, 1), (2, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (1, 12), (2, 12)]
        return GridMap(14,4,plots,True)

    @staticmethod
    def e_upper():
        """return: uppercase E as a 14*10 Gridmap Object"""
        plots = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (1, 9), (2, 9), (1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12)]
        return GridMap(14,10,plots,True)

    @classmethod
    def str_to_gm(cls,s,custom_dict=None):
        """
        Convert string --> GridMap
        convert strings to GridMap object

        custom_dict -> (optional) type:dict, to add or override
        any existing key in main conversion dict"""

        grid_dict = {
            "0":cls.zero(),
            "1":cls.one(),
            "2":cls.two(),
            "3":cls.three(),
            "4":cls.four(),
            "5":cls.five(),
            "6":cls.six(),
            "7":cls.seven(),
            "8":cls.eight(),
            "9":cls.nine(),
            " ":cls.space(),
            ".":cls.period(),
            ",":cls.comma(),
            ":":cls.colon(),
            ";":cls.semicolon(),
            "T":cls.t_upper(),
            "O":cls.o_upper(),
            "U":cls.u_upper(),
            "S":cls.s_upper(),
            "I":cls.i_upper(),
            "F":cls.f_upper(),
            "C":cls.c_upper(),
            "K":cls.k_upper(),
            "|":cls.bar(),
            "E":cls.e_upper(),
            }
        if custom_dict != None and type(custom_dict) == dict:
            for k,v in custom_dict.items():
                if type(k) == str:
                    if len(k) == 1 and type(v) == GridMap:
                        grid_dict[k] = v
                else:
                    raise ValueError("Custom dict could not be validated.")
        multiple_lines = False
        if "\n" in s:
            multiple_lines = True
            if custom_dict != None:
                done_list = [GridMap.str_to_gm(i,custom_dict=custom_dict) for i in s.split("\n")]
            else:
                done_list = [GridMap.str_to_gm(i) for i in s.split("\n")]
        if len(s) == 0:
            return None
        if not multiple_lines:
            try:
                s = [grid_dict[i] for i in s]
            except KeyError as e:
                if custom_dict == None:
                    print(f"Gridmap.str_to_gm: {e} could not assign to any built-in Gridmap obj.")
                else:
                    print(f"Gridmap.str_to_gm: {e} could assign to any Gridmap obj.")
                exit()
            s = deque(s)
            while True:
                l = []
                while s:
                    a = s.popleft()
                    if len(s) != 0:
                        b = s.popleft()
                        l.append(cls.merge(a,b))
                    else:
                        l.append(cls.merge(a))
                if len(l) != 1:
                    s = deque(l)
                else:
                    break
        if multiple_lines:
            h_len =  max([i.hor_len for i in done_list])
            v_len = sum([i.ver_len for i in done_list])
            plots = []
            load = 0
            for i in done_list:
                points = i.scat_plot
                for p in points:
                    v = (p[0],p[1]+load)
                    plots.append(v)
                load += i.ver_len
            return GridMap(v_len,h_len,plots,True)
        return(l[0])

    @classmethod
    def random_number(cls):
        """return 2-digit and rarely 1-digit 
        true random number as a gridmap object"""
        return cls.str_to_gm(str(time()).split(".")[1][3:5])

if __name__ == '__main__':
    pass