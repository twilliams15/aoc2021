def read_file(file):
    with open(file) as f:
        return f.readlines()


def format_course(ls):
    formatted_course = []
    for item in ls:
        formatted_course.append(item.replace('\n', '').rsplit(' ', ))
    return formatted_course


def calc_position(ls):
    horizontal_position = 0
    depth = 0
    aim = 0
    for item in ls:
        direction, value = item
        match direction:
            case 'forward':
                horizontal_position += int(value)
                depth += int(value) * aim
            case 'up':
                aim -= int(value)
            case 'down':
                aim += int(value)
    return [horizontal_position, depth]


if __name__ == '__main__':
    from support import pipe
    result = pipe(
        read_file,
        format_course,
        calc_position,
    )('./puzzle_input.txt')
    print(result)
