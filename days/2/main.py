color_limit_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def play_game_part_one(line):
    # split line into list of numbers
    subset = line.split(";")
    # compare each number of cubes to the max amount, if it is greater, return false, otherwise return true
    for c in [cube for cubes in subset for cube in cubes.split(",")]:
        amount, color = c.strip().split(" ")
        color_max = color_limit_dict[color]
        if int(amount) > color_max:
            return False
    return True


def play_game_part_two(line):
    # split line into list of numbers
    subset = line.split(";")
    color_max_dict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    # compare each number of cubes to the max amount, if it is greater, return false, otherwise return true
    for c in [cube for cubes in subset for cube in cubes.split(",")]:
        amount, color = c.strip().split(" ")
        color_max_dict[color] = max([color_max_dict[color], int(amount)])
    power = color_max_dict["red"] * color_max_dict["green"] * color_max_dict["blue"]
    return power

if __name__ == "__main__":
    # read text file as input
    with open('input.txt') as f:
        input = f.read()

    # loop through lines in the input and add total sum of each line to output
    output = []
    for line in input.splitlines():
        game_id, game = line.split(":")
        output.append(play_game_part_two(game))
    # print output
    print(sum(output))