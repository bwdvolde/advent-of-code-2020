from read_file.read_file import read_file

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Command:

    def __init__(self, command, argument):
        self.command = command
        self.argument = argument

    def __repr__(self):
        return f"({self.command}, {self.argument})"


def part_1(commands):
    x = 0
    y = 0
    direction = EAST

    def move_direction(command):
        nonlocal x, y
        if command.command == NORTH:
            y += command.argument
        if command.command == SOUTH:
            y -= command.argument
        if command.command == EAST:
            x += command.argument
        if command.command == WEST:
            x -= command.argument

    for command in commands:

        if command.command in DIRECTIONS:
            move_direction(command)
        if command.command == RIGHT:
            steps = command.argument // 90
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + steps) % len(DIRECTIONS)]
        if command.command == LEFT:
            steps = command.argument // 90
            direction = DIRECTIONS[(DIRECTIONS.index(direction) - steps) % len(DIRECTIONS)]
        if command.command == FORWARD:
            move_direction(Command(direction, command.argument))

    return abs(x) + abs(y)


def part_2(commands):
    waypoint_x, waypoint_y = 10, 1
    ship_x, ship_y = 0, 0

    for command in commands:
        if command.command == NORTH:
            waypoint_y += command.argument
        if command.command == SOUTH:
            waypoint_y -= command.argument
        if command.command == EAST:
            waypoint_x += command.argument
        if command.command == WEST:
            waypoint_x -= command.argument
        if command.command == RIGHT:
            steps = command.argument // 90
            while steps:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
                steps -= 1
        if command.command == LEFT:
            steps = command.argument // 90
            while steps:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
                steps -= 1
        if command.command == FORWARD:
            ship_x += command.argument * waypoint_x
            ship_y += command.argument * waypoint_y

    return abs(ship_x) + abs(ship_y)


if __name__ == '__main__':
    lines = read_file("input.txt")
    commands = [Command(line[0], int(line[1:])) for line in lines if line]

    answer_part_1 = part_1(commands)
    print(f"Part 1: {answer_part_1}")

    answer_part_2 = part_2(commands)
    print(f"Part 2: {answer_part_2}")
