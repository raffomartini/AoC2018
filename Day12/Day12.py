'''

'''
import re
from collections import Counter

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
        evolution = dict(p_evolution.match(l).groups() for l in f.readlines() if p_evolution.match(l))
    line = start_
    i_zero=0
    for i in range(iter):
        line,i_zero = evolve(line,evolution,i_zero)
        # print(i, line)
    # -> line, i_zero = ('.#....##....#####...#######....#.#..##', 3)
    result = sum( i+i_zero for i,c in enumerate(line) if c=='#' )
    print('Part1: ', result)
    print(line, i_zero)

def part2(iter=50000000000, file=FILE):
    # iter = 20
    p_init = re.compile(r'initial state: (.*)')
    p_evolution = re.compile(r'(.{5}) => (.)')
    with open(file) as f:
        line = f.readline()
        start_ = p_init.match(line).group(1)
        evolution = [p_evolution.match(l).group(1) for l in f.readlines() if p_evolution.match(l) and p_evolution.match(l).group(2)=='#' ]
    state = [ i for i, c in enumerate(start_) if c =='#']

    def evolve(state,evolution=evolution):
        possibilities = set(j for s in (range(i - 1, i + 2) for i in state) for j in s)
        # blocks = (''.join('#' if j in state else '.' for j in range(i - 2, i + 3)) for i in possibilities)
        return [i for i in possibilities if ''.join('#' if j in state else '.' for j in range(i - 2, i + 3)) in evolution]

    diff = []
    score_ = 0
    for i in range(iter):
        state = evolve(state)
        score = sum(state)
        diff.append(score - score_)
        score_ = score
        if len(diff) > 100:
            diff.pop(0)
            if all(i == diff[0] for i in diff):
                break
    result = score + (iter - i ) * diff[0]
    print('Part2: ', result)

# part1()
part2()