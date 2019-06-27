'''
--- Day 5: Alchemical Reduction ---
You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)

--- Part Two ---
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
'''

# FILE='test1.txt'
FILE='input.txt'
import itertools as it
import string


def reaction(pair):
    a, b = pair
    return None if (a.islower() and a.upper() == b) or (a.isupper() and a.lower() == b) else a


def step(sequence):
    pairs = ((i, next) for i, next in zip(sequence, sequence[1:]))
    s1 = ''.join(it.takewhile(lambda x: x, map(reaction, pairs)))
    if len(s1) == len(sequence) - 1:
        return sequence
    else:
        s2 = sequence[len(s1) + 2:]
        return s1 + s2

def step2(sequence):
    pairs = ((i, next) for i, next in zip(sequence, sequence[1:]))
    seq1 = map(reaction, pairs)
    prev_ = ''
    out = ''
    for i in it.chain(seq1,sequence[-1]):
        if prev_ is not None and i is not None:
            out += i
        if prev_ is None and i is None:
            # case cCc, only the first sequence will react
            prev_ = ''
        else:
            prev_ = i
    return out

def solve(input):
    current = input
    while True:
        next_ = step(current)
        if next_ == current:
            return next_
        else:
            current = next_

def solve2(input):
    current = input
    while True:
        next_ = step2(current)
        if next_ == current:
            return next_
        else:
            current = next_

def part1():

    with open(FILE) as infile:
        input = infile.readline().strip()

    print(solve(input))


def part2():
    with open(FILE) as infile:
        input = infile.readline().strip()

    result = len(input)
    for alpha_ in set(input.lower()):
        sequence = ''.join(it.filterfalse(lambda x: x == alpha_ or x ==alpha_.upper(), input))
        sequence = solve2(sequence)
        len_ = len(sequence)
        if len_ < result:
            result = len_

    print(result)

part2()




