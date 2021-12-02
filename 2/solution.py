def read_file(file):
    with open(file) as f:
        return f.readlines()


def format_course(ls):
    new_ls = []
    for ln in ls:
        new_ls.append(ln.replace('\n', '').rsplit(' ', ))
    return new_ls


def calc_position(c):
    x = 0
    y = 0
    for path in c:
        direction, value = path
        match direction:
            case 'forward':
                x += int(value)
            case 'up':
                y -= int(value)
            case 'down':
                y += int(value)
    return [x, y]


if __name__ == '__main__':
    course = read_file('./puzzle_input.txt')
    formatted_course = format_course(course)
    print(calc_position(formatted_course))
