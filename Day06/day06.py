'''
--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

--- Part Two ---
On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:

..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.
In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as follows, where abs() is the absolute value function:

Distance to coordinate A: abs(4-1) + abs(3-1) =  5
Distance to coordinate B: abs(4-1) + abs(3-6) =  6
Distance to coordinate C: abs(4-8) + abs(3-3) =  4
Distance to coordinate D: abs(4-3) + abs(3-4) =  2
Distance to coordinate E: abs(4-5) + abs(3-5) =  3
Distance to coordinate F: abs(4-8) + abs(3-9) = 10
Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
Because the total distance to all coordinates (30) is less than 32, the location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

'''

# FILE='test.txt' ; MAXD = 32
FILE='input.txt' ; MAXD = 10000


from dataclasses import dataclass
import csv

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def distance(self, other=None):
        if other is None:
            other = Point(0, 0)
        return abs(self.x-other.x) + abs(self.y - other.y)

def filter_edge(input, sequence):
    excluded = set()
    for p in sequence:
        d_p = [q.distance(p) for q in input]
        excluded_ = [index for index, value in enumerate(d_p) if value == min(d_p)]
        if len(excluded_) == 1:
            excluded |= set(excluded_)
    return excluded

def filter_edges(x_min,x_max,y_min,y_max):
    w_side = [Point(x_min-1,y) for y in range(y_min-1, y_max+2)]
    n_side = [Point(x,y_min-1) for x in range(x_min-1, x_max+2) ]
    e_side = [Point(x_max+1,y) for y in range(y_min-1, y_max+2) ]
    s_side = [Point(x, y_max+1) for x in range(x_min - 1, x_max + 2)]
    excluded = filter_edge(input,w_side) | filter_edge(input,n_side) | filter_edge(input,e_side) | filter_edge(input,s_side)
    return excluded

def get_boundary(input):
    x_min = min([p.x for p in input])
    x_max = max([p.x for p in input])
    y_min = min([p.y for p in input])
    y_max = max([p.y for p in input])
    return x_min, x_max,y_min,y_max

def part1():

    with open(FILE, newline='') as f:
        reader = csv.reader(f)
        input = *(Point(*map(int,row)) for row in reader),

        boundary = get_boundary(input)
        x_min,x_max,y_min,y_max = boundary
        excluded = filter_edges(*boundary)

        count_ = [0 for x in input]
        for x in range(x_min, x_max+1):
            for y in range(y_min,y_max+1):
                p = Point(x,y)
                dist = [q.distance(p) for q in input]
                min_ = [index for index, value in enumerate(dist) if value == min(dist)]
                if len(min_) == 1:
                    index = min_[0]
                    count_[index] += 1
        result = max([ count_[i] for i in range(len(input)) if i not in excluded ])
        print ('Part1: ',result)


def part2():

    with open(FILE, newline='') as f:
        reader = csv.reader(f)
        input = *(Point(*map(int, row)) for row in reader),

        boundary = get_boundary(input)
        x_min, x_max, y_min, y_max = boundary

        inclusion_area = (Point(x,y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1))
        dist = ( sum(q.distance(p) for q in input) for p in inclusion_area )
        result = len([d for d in dist if d < MAXD])
        print('Part2: ', result)

# part1()
part2()
