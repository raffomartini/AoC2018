'''
For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:

The rack ID is 3 + 10 = 13.
The power level starts at 13 * 5 = 65.
Adding the serial number produces 65 + 8 = 73.
Multiplying by the rack ID produces 73 * 13 = 949.
The hundreds digit of 949 is 9.
Subtracting 5 produces 9 - 5 = 4.
So, the power level of this fuel cell is 4.

Here are some more example power levels:

Fuel cell at  122,79, grid serial number 57: power level -5.
Fuel cell at 217,196, grid serial number 39: power level  0.
Fuel cell at 101,153, grid serial number 71: power level  4.

--- Part Two ---
You discover a dial on the side of the device; it seems to let you select a square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total power. Identify this square by including its size as a third parameter after the top-left coordinate: a 9x9 square with a top-left corner of 3,5 is identified as 3,5,9.

For example:

For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.
What is the X,Y,size identifier of the square with the largest total power?
'''

from collections import namedtuple
PUZZLE_INPUT = 7165

Coord = namedtuple('Coord',('x','y'))

def power_level(x, y, serial = PUZZLE_INPUT):
    rack_id = x + 10
    pow = ((rack_id * y + serial) * rack_id) // 100 % 10
    return pow - 5

def part1(serial= PUZZLE_INPUT):

    def power_level_(x,y):
        return power_level(x,y,serial)

    grid = [[ power_level_(x,y) for x in range(300)] for y in range(300)]

    pow_grid = [ [ sum(sum(grid[yy][x:x+3]) for yy in range(y,y+3)) for x in range(300-2)] for y in range(300-2)]

    max_ = max(max(pow_grid[y]) for y in range(300-2))

    result = [(x,y) for x in range(300-2) for y in range(300-2) if pow_grid[y][x] == max_ ]

    print('Part1: {},{}'.format(result[0][0], result[0][1]))

def part2(serial= PUZZLE_INPUT):

    def power_level_(x,y):
        return power_level(x,y,serial)

    grid = [[ power_level_(x,y) for x in range(300)] for y in range(300)]

    max = -100000000
    coords = []
    def copy_table(grid):
        return [l.copy() for l in grid]
    s_grid = copy_table(grid)
    for s in range(300):
        # print(s)
        for y in range(300 - s):
            for x in range(300 - s):
                s_power = s_grid[y][x] + sum(grid[yy][x+s] for yy in range(y,y+s)) + sum(grid[y+s][x:x+s+1])
                s_grid[y][x] = s_power
                if s_power > max:
                    max = s_power
                    coords = x,y,s,

    print('Part2: {},{},{}'.format(coords[0],coords[1],coords[2]+1))

part1()
part2()