'''

'''
import re

FILE = 'test.txt'
FILE = 'input.txt'

def evolve(line,evolution,i_zero=0):
    if line[0] == '#':
        i_zero += 1
        line = '...' + line
    elif line[1] == '#':
        line = '..' + line
    elif line[2] == '#':
        i_zero -= 1
        line = '.' + line
    if line[-1] == '#':
        line = line + '...'
    elif line [-2] == '#':
        line = line + '..'
    elif line[-1] == '#':
        line = line + '.'
    return ''.join( evolution[line[i:i+5]] for i,c in enumerate(line[:-4])), i_zero,


def part1(file=FILE,iter=20):
    p_init = re.compile(r'initial state: (.*)')
    p_evolution = re.compile(r'(.{5}) => (.)')
    with open(file) as f:
        line = f.readline()
        start_ = p_init.match(line).group(1)
        evolution = dict(p_evolution.match(line).groups() for line in f.readlines() if p_evolution.match(line))
    line = start_
    i_zero=0
    for i in range(iter):
        line,i_zero = evolve(line,evolution,i_zero)
        # print(i, line)
    # -> line, i_zero = ('.#....##....#####...#######....#.#..##', 3)
    result = sum( i+i_zero for i,c in enumerate(line) if c=='#' )
    print('Part1: ', result)
    print(line, i_zero)

def part2(file=FILE):
    solve(file,50000000000)

part1()
# part2()