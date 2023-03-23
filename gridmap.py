from time import sleep


class NotPlottableError(Exception):
    pass

class NotMergeableError(Exception):
    pass


class GridMap:


    BASE_DICT = {
            '0':
                    (14, 8, (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (4, 1), (4, 2), (4, 5), (4, 6), (5, 1), (5, 2), (5, 5), (5, 6), (6, 1), (6, 2), (6, 5), (6, 6), (7, 1), (7, 2), (7, 5), (7, 6), (8, 1), (8, 2), (8, 5), (8, 6), (9, 1), (9, 2), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 2), (12, 3), (12, 4), (12, 5)),
            '1':
                    (14, 8, (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 3), (4, 4), (5, 3), (5, 4), (6, 3), (6, 4), (7, 3), (7, 4), (8, 3), (8, 4), (9, 3), (9, 4), (10, 3), (10, 4), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6)),
            '2':
                    (14, 8, (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (4, 5), (4, 6), (5, 5), (5, 6), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 2), (8, 3), (8, 4), (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6)),
            '3':
                    (14, 8, (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (4, 1), (4, 2), (4, 5), (4, 6), (5, 5), (5, 6), (6, 5), (6, 6), (7, 4), (7, 5), (8, 5), (8, 6), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 2), (12, 3), (12, 4), (12, 5)),
            '4':
                    (14, 8, (1, 6), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 3), (4, 4), (4, 5), (4, 6), (5, 2), (5, 3), (5, 5), (5, 6), (6, 1), (6, 2), (6, 5), (6, 6), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (9, 5), (9, 6), (10, 5), (10, 6), (11, 5), (11, 6), (12, 5), (12, 6)),
            '5':
                    (14, 8, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 5), (8, 6), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6)),
            '6':
                    (14, 8, (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 1), (8, 2), (8, 5), (8, 6), (9, 1), (9, 2), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 2), (12, 3), (12, 4), (12, 5)),
            '7':
                    (14, 8, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 5), (3, 6), (4, 5), (4, 6), (5, 4), (5, 5), (5, 6), (6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (8, 3), (8, 4), (9, 3), (9, 4), (10, 3), (10, 4), (11, 3), (11, 4), (12, 3), (12, 4)),
            '8':
                    (14, 8, (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (4, 1), (4, 2), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 2), (6, 3), (6, 4), (6, 5), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (9, 1), (9, 2), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 2), (12, 3), (12, 4), (12, 5)),
            '9':
                    (14, 8, (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (4, 1), (4, 2), (4, 5), (4, 6), (5, 1), (5, 2), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 5), (8, 6), (9, 5), (9, 6), (10, 1), (10, 5), (10, 6), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 2), (12, 3), (12, 4), (12, 5)),
            ' ':
                    (14, 8),
            '.':
                    (14, 5, (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (12, 1), (12, 2), (12, 3)),
            ',':
                    (14, 5, (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 2), (10, 3), (11, 2), (11, 3), (12, 1), (12, 2)),
            ':':
                    (14, 5, (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2)),
            '\'':
                    (14, 5, (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 2), (4, 3), (5, 2), (5, 3), (6, 1), (6, 2)),
            ';':
                    (14, 5, (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 2), (10, 3), (11, 2), (11, 3), (12, 1), (12, 2)),
            '(':
                    (14, 5, (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (7, 1), (7, 2), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2), (11, 2), (11, 3), (11, 4), (12, 3), (12, 4)),
            ')':
                    (14, 5, (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (3, 3), (3, 2), (4, 3), (4, 2), (5, 3), (5, 2), (6, 3), (6, 2), (7, 3), (7, 2), (8, 3), (8, 2), (9, 3), (9, 2), (10, 3), (10, 2), (11, 2), (11, 1), (11, 0), (12, 1), (12, 0)),
            '=':
                    (14, 5, (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4)),
            'A':
                    (14, 10, (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (2, 6), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 2), (4, 3), (4, 6), (4, 7), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'B':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6)),
            'C':
                    (14, 10, (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (7, 1), (7, 2), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8)),
            'D':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 6), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 7), (7, 8), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 6), (9, 7), (9, 8), (10, 1), (10, 2), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5)),
            'E':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8)),
            'F':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2), (11, 1), (11, 2), (12, 1), (12, 2)),
            'G':
                    (14, 10, (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (7, 1), (7, 2), (7, 5), (7, 6), (7, 7), (7, 8), (8, 1), (8, 2), (8, 5), (8, 6), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)),
            'H':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'I':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 4), (3, 5), (4, 4), (4, 5), (5, 4), (5, 5), (6, 4), (6, 5), (7, 4), (7, 5), (8, 4), (8, 5), (9, 4), (9, 5), (10, 4), (10, 5), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8)),
            'J':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 7), (3, 8), (4, 7), (4, 8), (5, 7), (5, 8), (6, 7), (6, 8), (7, 7), (7, 8), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)),
            'K':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 1), (6, 2), (6, 3), (6, 4), (7, 1), (7, 2), (7, 3), (7, 4), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 1), (9, 2), (9, 4), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'L':
                    (14, 10, (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (7, 1), (7, 2), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8)),
            'M':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 3), (3, 6), (3, 7), (3, 8), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 1), (5, 2), (5, 4), (5, 5), (5, 7), (5, 8), (6, 1), (6, 2), (6, 4), (6, 5), (6, 7), (6, 8), (7, 1), (7, 2), (7, 7), (7, 8), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'N':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 7), (2, 8), (3, 1), (3, 2), (3, 3), (3, 7), (3, 8), (4, 1), (4, 2), (4, 3), (4, 4), (4, 7), (4, 8), (5, 1), (5, 2), (5, 3), (5, 4), (5, 7), (5, 8), (6, 1), (6, 2), (6, 4), (6, 5), (6, 7), (6, 8), (7, 1), (7, 2), (7, 4), (7, 5), (7, 7), (7, 8), (8, 1), (8, 2), (8, 5), (8, 6), (8, 7), (8, 8), (9, 1), (9, 2), (9, 5), (9, 6), (9, 7), (9, 8), (10, 1), (10, 2), (10, 6), (10, 7), (10, 8), (11, 1), (11, 2), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'O':
                    (14, 10, (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 7), (7, 8), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)),
            'P':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 1), (8, 2), (9, 1), (9, 2), (10, 1), (10, 2), (11, 1), (11, 2), (12, 1), (12, 2)),
            'Q':
                    (14, 10, (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 7), (7, 8), (8, 1), (8, 2), (8, 4), (8, 5), (8, 7), (8, 8), (9, 1), (9, 2), (9, 4), (9, 5), (9, 6), (9, 8), (10, 1), (10, 2), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 3), (11, 4), (11, 6), (11, 7), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 7), (12, 8)),
            'R':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 1), (9, 2), (9, 4), (9, 5), (9, 6), (10, 1), (10, 2), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'S':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 7), (8, 8), (9, 7), (9, 8), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8)),
            'T':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 4), (3, 5), (4, 4), (4, 5), (5, 4), (5, 5), (6, 4), (6, 5), (7, 4), (7, 5), (8, 4), (8, 5), (9, 4), (9, 5), (10, 4), (10, 5), (11, 4), (11, 5), (12, 4), (12, 5)),
            'U':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 7), (7, 8), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 7), (9, 8), (10, 1), (10, 2), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)),
            'V':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 7), (7, 8), (8, 1), (8, 2), (8, 7), (8, 8), (9, 1), (9, 2), (9, 3), (9, 6), (9, 7), (9, 8), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (11, 3), (11, 4), (11, 5), (11, 6), (12, 4), (12, 5)),
            'W':
                    (14, 10, (1, 1), (1, 2), (1, 7), (1, 8), (2, 1), (2, 2), (2, 7), (2, 8), (3, 1), (3, 2), (3, 7), (3, 8), (4, 1), (4, 2), (4, 7), (4, 8), (5, 1), (5, 2), (5, 7), (5, 8), (6, 1), (6, 2), (6, 7), (6, 8), (7, 1), (7, 2), (7, 4), (7, 5), (7, 7), (7, 8), (8, 1), (8, 2), (8, 4), (8, 5), (8, 7), (8, 8), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (10, 1), (10, 2), (10, 3), (10, 6), (10, 7), (10, 8), (11, 1), (11, 2), (11, 3), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 7), (12, 8)),
            'X':
                    (14, 10, (1, 1), (1, 8), (2, 1), (2, 2), (2, 7), (2, 8), (3, 1), (3, 2), (3, 3), (3, 6), (3, 7), (3, 8), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (5, 6), (6, 4), (6, 5), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5), (8, 6), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 1), (10, 2), (10, 3), (10, 6), (10, 7), (10, 8), (11, 1), (11, 2), (11, 7), (11, 8), (12, 1), (12, 8)),
            'Y':
                    (14, 10, (1, 1), (1, 8), (2, 1), (2, 2), (2, 7), (2, 8), (3, 1), (3, 2), (3, 3), (3, 6), (3, 7), (3, 8), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (5, 6), (6, 4), (6, 5), (7, 4), (7, 5), (8, 4), (8, 5), (9, 4), (9, 5), (10, 4), (10, 5), (11, 4), (11, 5), (12, 4), (12, 5)),
            'Z':
                    (14, 10, (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 7), (3, 8), (4, 7), (4, 8), (5, 6), (5, 7), (6, 5), (6, 6), (7, 4), (7, 5), (8, 3), (8, 4), (9, 2), (9, 3), (10, 1), (10, 2), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8)),
    }

    NUM_CHARS = ['\u2460', '\u2461', '\u2462', '\u2463', '\u2464', '\u2465', '\u2466', '\u2467', '\u2468']
    SQR_CHARS = ["■", "⬛"]

    def __init__(self, r, c, *plots, char="■"):
        self.r = r # row
        self.c = c # column
        self.char = char
        self._plots = None # this stores a dictionary
        self.plots = plots # [(rowX0, columnY0), ...]

    def shape(self):
        return (self.r, self.c)

    @property
    def plots(self):
        return self._plots

    @plots.setter
    def plots(self, plots):
        plot_dict = {}
        for i in range(self.r):
            plot_dict[i] = []
        for i in plots:
            if i[1] >= 0 and i[1] < self.c and i[0] >= 0 and i[0] < self.r:
                plot_dict[i[0]].append(i[1])
            else:
                raise NotPlottableError(
                    f"Can't plot {i[0], i[1]} in a {self.r} * {self.c} grid.")
        self._plots = plot_dict

    @property
    def listplots(self):
        return [(r, i) for r in range(self.r) for i in self.plots[r]]

    def arange_plots(self):
        if isinstance(self.plots, dict):
            for k, v in self._plots.items():
                v.sort()
                self.plots[k] = list(set(v))

    def add_plot(self, r, c):
        try:
            if r >= 0 and c < self.c:
                if c not in self._plots[r]:
                    self._plots[r].append(c)
            else:
                raise NotPlottableError(f"Column index does not exist. - {c}")
        except KeyError:
            raise NotPlottableError(f"Row index does not exist. - {r}")

    def __repr__(self) -> str:
        return f"GridMap({self.r}, {self.c})"

    def __str__(self) -> str:
        self.arange_plots()
        return "\n".join(
            "".join(f"{self.char}" if i in self.plots[x] else " "
                    for i in range(self.c)) for x in range(self.r))

    def cells(self) -> str:
        self.arange_plots()
        res = (" " + "__ " * self.c)[:-1] + "\n"
        res += "\n".join(
            "|" + "".join(f"_{self.char}|" if i in self.plots[x] else "__|"
                          for i in range(self.c)) for x in range(self.r))
        return res
    
    def font0(self) -> str:
        return str(self)
    
    def font1(self) -> str:
        return self.cells()
    
    def font2(self) -> str:
        return self.font1().replace('|', '').replace('_', ' ')

    def addrow_up(self, count: int) -> None:
        for i in range(self.r + count -1, -1, -1):
            try:
                self._plots[i] = self.plots.get(i - count, [])
            except KeyError:
                self._plots[i] = []
        self.r += count

    def addrow_down(self, count: int) -> None:
        for i in range(self.r, self.r + count):
            self._plots[i] = []
        self.r += count

    def addrow_ud(self, count: int) -> None:
        self.addrow_up((c := count // 2))
        if count % 2 == 0:
            self.addrow_down(c)
        else:
            self.addrow_down(count - c)

    def addcolumn_left(self, count: int) -> None:
        for k, v in self.plots.items():
            self._plots[k] = [i + count for i in v]
        self.c += count

    def addcolumn_right(self, count: int) -> None:
        self.c += count    

    def addcolumn_rl(self, count: int) -> None:
        self.addcolumn_left((c := count // 2))
        if count % 2 == 0:
            self.addcolumn_right(c)
        else:
            self.addcolumn_right(count - c)

    def removecolumn_rl(self, count: int) -> None:
        self.removecolumn_left((c := count // 2))
        if count % 2 == 0:
            self.removecolumn_right(c)
        else:
            self.removecolumn_right(count - c)

    def removerow_up(self, count: int) -> None:
        for i in range(count):
            del self._plots[i]
        for i in range(count, self.r):
            self._plots[i - count] = self._plots.pop(i)
        self.r -= count

    def removerow_down(self, count: int) -> None:
        for i in range(self.r - 1, self.r - count - 1, -1):
            del self._plots[i]
        self.r -= count

    def removerow_ud(self, count: int) -> None:
        c = count // 2
        self.removerow_up(c)
        if count % 2 == 0:
            self.removerow_down(c)
        else:
            self.removerow_down(count - c)

    def removecolumn_right(self, count: int) -> None:
        self.c -= count
        for k in self._plots:
            for n, v in enumerate(self._plots[k]):
                if v >= self.c:
                    self._plots[k] = self._plots[k][:n]

    def removecolumn_left(self, count: int) -> None:
        self.c -= count
        for k, v in self._plots.items():
            self._plots[k] = [c for c in [i - count for i in v] if c >= 0]

    def addrow(self, rowidx: int, count: int) -> None:
        foo = self.copy()
        foo.removerow_up(rowidx - 1)
        foo.addrow_up(count)
        self.removerow_down(self.r - rowidx + 1)
        n = self.bottom_merge(self, foo)
        self.r, self.c = n.r, n.c
        self.plots = n.listplots

    def removerow(self, rowidx) -> None:
        self._plots[rowidx] = []
        for i in range(rowidx, self.r - 1):
            self._plots[i] = self._plots[i + 1]
        del self._plots[self.r - 1]
        self.r -= 1

    def removecolumn(self, colidx: int) -> None:
        for k, v in self._plots.items():
            self._plots[k] = [i for i in v if i < colidx] + [i - 1 for i in v if i > colidx]
        self.removecolumn_right(1)

    def copy(self):
        res = GridMap(self.r, self.c)
        res._plots = self.plots.copy()
        return res

    @classmethod
    def side_merge(cls, a, b, force_merge: bool = False):
        """merge b on right of a"""
        if not isinstance(a, cls) and not isinstance(b, cls):
            raise NotMergeableError(f"Can merge only Gridmap objects not {type(a)} with {type(b)}")
        foo0, foo1 = a.copy(), b.copy()
        del a, b
        if foo0.r != foo1.r:
            if force_merge:
                if foo0.r < foo1.r:
                    foo0.addrow_ud(foo1.r - foo0.r)
                else:
                    foo1.addrow_ud(foo0.r - foo1.r)
            else:
                raise NotMergeableError(f"Failed to merge varying row counts.")
        for r, c in foo1._plots.items():
            foo1._plots[r] = [i + foo0.c for i in c]
        res = cls(foo0.r, foo0.c + foo1.c)
        for k in res._plots.keys():
            res._plots[k] = foo0._plots[k] + foo1._plots[k]
        return res
    
    @classmethod
    def bottom_merge(cls, a, b, force_merge: bool = False):
        """merge b below a"""
        if not isinstance(a, cls) and not isinstance(b, cls):
            raise NotMergeableError(f"Can merge only Gridmap objects not {type(a)} with {type(b)}")
        foo0, foo1 = a.copy(), b.copy()
        del a, b
        if foo0.c != foo1.c:
            if force_merge:
                if foo0.c < foo1.c:
                    foo0.addcolumn_rl(foo1.c - foo0.c)
                else:
                    foo1.addcolumn_rl(foo0.c - foo1.c)
            else:
                raise NotMergeableError(f"Failed to merge varying column counts.")
        res = cls(foo0.r + foo1.r, foo0.c)
        for k, v in foo0.plots.items():
            res._plots[k] = v
        for k, v in foo1.plots.items():
            res._plots[k + foo0.r] = v
        return res
    
    @classmethod
    def animate(cls, frames: list, *, r: int = None, c: int = None, time_delay: float or int = 0.5, correction: int = 1, style: int = 0, max_loops):
        """
        r: int -> frame size vertically
        c: int -> frame size horizontally
        frames: list -> a list containing list of frame plots in sublists
        time_delay: int or float -> frame change delay
        correction: int
        """
        if r is None:
            r = max([a[0] for a in [i[-1] for i in frames]]) + 1
        if c is None:
            c = max([a[1] for a in [i[-1] for i in frames]]) + 1
        frame = cls(r, c)
        assert isinstance(max_loops, int) and max_loops > 0, "arg: max_loops must be an integer and greater than 0."
        max_loops = float("inf") if max_loops == None else max_loops
        count = 0
        while count < max_loops:
            for i in frames:
                frame.plots = i
                if style == 0:
                    print(frame)
                elif style == 1:
                    print(frame.cells())
                    if correction == 1:
                        correction += 1
                elif style == 2:
                    print(frame.font2())
                    if correction == 1:
                        correction += 1
                sleep(time_delay)
                count += 1
                print("\033[{}A".format(frame.r + correction))
    
    def __add__(self, _o):
        return self.side_merge(self, _o)
        
    @classmethod
    def str_to_gm(cls, s: str, force_merge: bool = True):
        foo = s.split("\n")
        if foo[-1] == "": foo = foo[:-1]
        if len(foo) == 1:
            res = cls(*(cls.BASE_DICT[foo[0][0]]))
            for i in foo[0][1:]:
                res = cls.side_merge(res, cls(*(cls.BASE_DICT[i])), force_merge=force_merge)
            return res
        else:
            foo = [cls.str_to_gm(i) for i in foo]
            res = foo[0]
            for i in foo[1:]:
                res = res.bottom_merge(res, i, force_merge=force_merge)
            return res

    @classmethod
    def strlist_to_animate(cls, *sl: list, time_delay: int or float = 0.5, r: int = None, c: int = None, correction: int = 1, style: int = 0, max_loops: int = None):
        cls.animate([cls.str_to_gm(i).listplots for i in sl], time_delay=time_delay, r=r, c=c, correction=correction, style=style, max_loops=max_loops)
        
    def invert(self):
        plots = []
        for k, v in self.plots.items():
            for i in v:
                plots.append((i, k))
        self.r, self.c = (self.c, self.r)
        self.plots = plots

    def hflip(self):
        plots = []
        for k, v in self.plots.items():
            for i in v:
                plots.append((k, i))
        plots = list(map(lambda x: (x[0], self.c - x[1] - 1), plots))
        self.plots = plots

    def vflip(self):
        plots = []
        for k, v in self.plots.items():
            for i in v:
                plots.append((k, i))
        plots = list(map(lambda x: (self.r - x[0] - 1, x[1]), plots))
        self.plots = plots

    def rotate_right(self):
        rotated_plots = {}
        for row in range(self.c-1, -1, -1):
            new_row = []
            for col in range(self.r):
                if col in self._plots and row in self._plots[col]:
                    new_row.append(self.r - col - 1)
            rotated_plots[row] = new_row
        self._plots = rotated_plots
        self.r, self.c = self.c, self.r

    def rotate_left(self):
        self.invert()
        self.vflip()


if __name__ == "__main__":

    import time

    def animation0(r: int, char = GridMap.SQR_CHARS[0]):
        assert(isinstance(r, int) and r > 1), "argument must be a positive integer which is greater than 1."
        assert(r % 2 != 0), "row count cannot be an even number"
        a = GridMap(r, r, (r//2, r//2), char=char)

        def precompute_neighbours(r):
            neighbours = {}
            for row in range(r):
                for col in range(r):
                    n = set((row + dr, col + dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr != 0 or dc != 0) and (0 <= row + dr < r) and (0 <= col + dc < r))
                    neighbours[(row,col)] = n
            return neighbours

        neighbours = precompute_neighbours(r)

        animation_plots = [a.listplots]

        for i in range(r//2):
            if i == 0:
                a.plots = a.listplots + list(neighbours[(a.r //2,a.r //2)])
                animation_plots.append(a.listplots)
            else:
                n = []
                for i in a.listplots:
                    n += list(neighbours[i])
                a.plots = list(set(n))
                animation_plots.append(a.listplots)

        GridMap.animate(animation_plots, time_delay=0.1, r=r, c=r)
        
    # a.plots = plots = a.listplots + [(i, i) for i in range(a.r)] # d1
    # a.plots = plots = a.listplots + [(i, a.r - i - 1) for i in range(a.r)] # d2

    animation0(17)
