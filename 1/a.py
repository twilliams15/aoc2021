def does_increase(a, b):
    return a < b


def count_increases(ls):
    count = 0
    for i in range(len(ls) - 1):
        if does_increase(ls[i], ls[i + 1]):
            count += 1
    return count


def sum_three(ls):
    sums = []
    for i in range(len(ls) - 2):
        sums.append(ls[i] + ls[i+1] + ls[i+2])
    return sums


if __name__ == '__main__':
    import puzzle_input
    print(count_increases(sum_three(puzzle_input.depth_measurements)))
