import itertools

def part1():
    with open('Day01/input.txt') as f:
        input = map(int, f.readlines())
    return sum(input)


def part2():
    with open('Day01/input.txt') as f:
        sequence = map(int, f.readlines())
    frequency_sequence = [0]
    result = None
    for delta in itertools.cycle(sequence):
        frequency = frequency_sequence[-1] + delta
        if frequency in frequency_sequence:
            result = frequency
            break
        frequency_sequence.append( frequency )
    return result

def part2b():
    with open('Day01/input.txt') as f:
        delta_sequence = map(int, f.readlines())
        freq_seq = list(itertools.accumulate(delta_sequence))
    period = freq_seq[-1]
    freq_seq = [0] + freq_seq[:-1]
    frequency_offset_pair = ((max(x, y), x-y) for x in freq_seq for y in freq_seq if (x - y) % period == 0 and x != y )
    result = min(frequency_offset_pair, key=lambda t: abs(t[1]))[0]
    return result

if __name__ == '__main__':
    # print(part1())
    # print(part2())
    print(part2b())
