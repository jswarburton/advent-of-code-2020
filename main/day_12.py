from main.file_reader import read

directions = ["N", "E", "S", "W"]


def turn(current_dir, clockwise, degrees):
    current_location = directions.index(current_dir)
    if not clockwise:
        degrees = -degrees
    return directions[(current_location + degrees // 90) % len(directions)]


def solve_1(input: list) -> int:
    (x, y) = (0, 0)
    facing_dir = "E"

    for line in input:
        action, value = (line[0], int(line[1:]))

        if action == "F":
            action = facing_dir

        if action == "E":
            x -= value
        elif action == "W":
            x += value
        elif action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "L" or action == "R":
            facing_dir = turn(current_dir=facing_dir, clockwise=action == "R", degrees=value)

    return abs(x) + abs(y)


def solve_2(input: list) -> int:
    (ship_x, ship_y) = (0, 0)
    (waypoint_x, waypoint_y) = (-10, 1)

    for line in input:
        action, value = (line[0], int(line[1:]))

        if action == "E":
            waypoint_x -= value
        elif action == "W":
            waypoint_x += value
        elif action == "N":
            waypoint_y += value
        elif action == "S":
            waypoint_y -= value
        elif action == "L":
            if value == 90:
                (waypoint_x, waypoint_y) = (waypoint_y, -waypoint_x)
            elif value == 180:
                (waypoint_x, waypoint_y) = (-waypoint_x, -waypoint_y)
            elif value == 270:
                (waypoint_x, waypoint_y) = (-waypoint_y, waypoint_x)

        elif action == "R":
            if value == 90:
                (waypoint_x, waypoint_y) = (-waypoint_y, waypoint_x)
            elif value == 180:
                (waypoint_x, waypoint_y) = (-waypoint_x, -waypoint_y)
            elif value == 270:
                (waypoint_x, waypoint_y) = (waypoint_y, -waypoint_x)
        elif action == "F":
            ship_x += value * waypoint_x
            ship_y += value * waypoint_y

    return abs(ship_x) + abs(ship_y)


if __name__ == "__main__":
    input = read("day12-01.txt")
    print(solve_1(input))  # 2280
    print(solve_2(input))  # 38693
