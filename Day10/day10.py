'''

'''
FILE = 'input.txt'

import re
from collections import namedtuple
import matplotlib.pyplot as plt

Coord = namedtuple('Coord',('x','y','vx','vy'))
p = re.compile(r'position=<(.*),(.*)> velocity=<(.*),(.*)>')


with open(FILE) as f:
    puzzle_ = (p.match(line).groups() for line in f.readlines())
    t0 =  tuple(Coord(*map(int,x)) for x in puzzle_)


table = {}
for v in set((x.vy for x in t0)):
    y_v = [x.y for x in t0 if x.vy == v ]
    table[v] = min(y_v), max(y_v), max(y_v)-min(y_v), sum(y_v)/len(y_v)

'''
table ->
 v: (min(y , max(y), d, average(y) )
-------------------------------------
{1: (-10536, -10527, 9, -10531.125),
 2: (-21192, -21183, 9, -21188.076923076922),
 3: (-31848, -31839, 9, -31843.4375),
 4: (-42504, -42495, 9, -42499.55882352941),
 5: (-53160, -53151, 9, -53155.294117647056),
 -1: (10776, 10785, 9, 10780.575757575758),
 -5: (53400, 53409, 9, 53405.09375),
 -4: (42744, 42753, 9, 42749.3870967742),
 -3: (32088, 32097, 9, 32093.277777777777),
 -2: (21432, 21441, 9, 21435.925)}
'''
'''
Few notes:
1- as points with the same speed are solidal, the min (or max) for the starting point will be also
 the min or max for all point with the same speed
2- the input make the math easier as the veriance on y is 9 for all speeds
Some math:
y'n = y'0 + v' n
y''n = y''0 + v'' n  ->
...
n = (y'0 - y''0) / (v'' - v')
'''
v1, v2 = list(set((x.vy for x in t0)))[:2]
n = (table[v1][0] - table[v2][0])/(v2 - v1)
n = int(n)
# y coords are inverted
sky = [ (p.x + n*p.vx, -p.y -n*p.vy) for p in t0 ]

def display(sky):
    plt.scatter(*zip(*sky))
    plt.show()

display(sky)

print('Part2:', n)
