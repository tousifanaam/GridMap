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
    def merge(a,b):
        """a,b: type: Gridmap object
        merge b to right of a"""

        if type(a) != GridMap or type(b) != GridMap:
            raise TypeError("GridMap.merge - Argument(s) not a GridMap object.")
            
        a = str(a).split("\n")
        b = str(b).split("\n")
        if len(a) != len(b):
            raise ValueError("Invalid vertical length combination") from None
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

if __name__ == '__main__':
    pass