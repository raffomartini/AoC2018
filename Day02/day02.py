'''
--- Day 2: Inventory Management System ---

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
'''

import collections
import functools
import operator
import itertools

# FILE='test.txt'
# FILE='test2.txt'
FILE='input.txt'


def check_sn(sn):
    result = [0,0]
    for _, count in collections.Counter(sn).items():
        if count == 3:
            result[1] = 1
        if count == 2:
            result[0] = 1
    return result

def part1():
    with open(FILE) as f:
        sn_list = map(str.strip, f.readlines())
    chksum_step1 = (check_sn(x) for x in sn_list)
    chksum_step2 = map(sum, zip(*chksum_step1))
    chksum = functools.reduce(operator.mul, chksum_step2)
    print(chksum)

def likelyhood(sn1, sn2):
    step_1 = [x if x == y else None  for x, y in zip(sn1, sn2)]
    likelihood = len(list(itertools.filterfalse(lambda x: x, step_1)))
    common_sequence = ''.join(list(itertools.filterfalse(lambda x: not(x), step_1)))
    return likelihood, common_sequence

def part2():
    with open(FILE) as f:
        sn_list = list(map(str.strip, f.readlines()))
    for i, sn in enumerate(sn_list[:-1]):
        step_1\
            = list(itertools.filterfalse(lambda x: x[0] != 1 , map(lambda x: likelyhood(sn, x), sn_list[i+1:])))
        if len(step_1) == 1:
            break
        # print(step_1)
    print(step_1[0][1])


if __name__ == '__main__':
    part1()
    part2()
