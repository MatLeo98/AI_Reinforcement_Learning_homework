# Constants
ROWS = range(4)
COLS = range(9)
EPSILON = 0.1
ALPHA = 0.8
GAMMA = 0.9


def path_for_beater(policy):
    s = 0
    print('\nPath to reach the beater:')
    for i in ROWS:
        for j in COLS:
            var = True

            if i == 1 and j == 0 or i == 1 and j == 7:
                print('({})'.format('$'), end=" ")
                continue

            if j == 4:
                print('({})'.format('|'), end=" ")
                continue

            for p in policy:
                if p[0][0] == i and p[0][1] == j and p[0][2] == 0:
                    s = p[1]
                    var = False

            if var:
                print("({})".format('-'), end=" ")
            else:
                print('({})'.format(s), end=" ")
        print()


def path_for_oven(policy):
    s = 0
    print('Path to reach the oven:')
    for i in ROWS:
        for j in COLS:
            var = True

            if i == 0 and j == 7:
                print('({})'.format('$'), end=" ")
                continue

            if j == 4:
                print('({})'.format('|'), end=" ")
                continue

            for p in policy:
                if p[0][0] == i and p[0][1] == j and p[0][2] == 1:
                    s = p[1]
                    var = False

            if var:
                print("({})".format('-'), end=" ")
            else:
                print('({})'.format(s), end=" ")
        print()


# Mapping of the grid's boundary walls
def boundary_wall(row, column):
    return (row == 0 and column == 4) or (row == 1 and column == 4) or (row == 2 and column == 4) \
           or (row == 3 and column == 4) or row < 0 or row >= 4 or column < 0 or column >= 9


# Mapping of the grid's inner walls
def inner_walls():
    return [(0, 0, 'D'),
            (0, 7, 'D'),
            (0, 8, 'D'),
            (1, 0, 'U'), (1, 0, 'R'),
            (1, 1, 'L'), (1, 1, 'D'),
            (1, 2, 'D'),
            (1, 6, 'R'),
            (1, 7, 'U'), (1, 7, 'L'),
            (1, 8, 'U'),
            (2, 0, 'D'),
            (2, 1, 'U'), (2, 1, 'D'),
            (2, 2, 'U'),
            (2, 6, 'R'),
            (2, 7, 'L'), (2, 7, 'D'),
            (3, 0, 'U'),
            (3, 1, 'U'),
            (3, 7, 'U')
            ]


def is_beater(row, column):
    return (row, column) == (1, 0) or (row, column) == (1, 7)
