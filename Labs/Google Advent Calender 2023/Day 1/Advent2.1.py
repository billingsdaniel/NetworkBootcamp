# Specify the filename
filename = 'Advent2Data.txt'

def parse_throw(throw_str):
    # throw_str = 5 blue, 2 green, 7 red
    throw_strsplit = throw_str.split(",")
    throw_colour_dict = {}
    for cubes_str in throw_strsplit:
        # cube_colour = '5 blue'
        cubes_str = cubes_str.strip()
        cube_quant = int(cubes_str.split(" ")[0])
        cube_colour = cubes_str.split(" ")[1]
        throw_colour_dict[cube_colour] = cube_quant
    return throw_colour_dict

def parse_game_line(line):
    replace_colon = line.replace(":", ";")
    game_string = replace_colon.strip()
    game_array = game_string.split(";")
    game_num = game_array[0].split(" ")[1]
    throws_array = game_array[1:]
    throw_bag_dicts = []
    for throw_str in throws_array:
        # throw_str = 5 blue, 2 green, 7 red
        throw_colour_dict = parse_throw(throw_str)
        throw_bag_dicts.append(throw_colour_dict)
    return {"game":game_num, "throws": throw_bag_dicts}

# Open the file in read mode
with open(filename, 'r') as file:
    # Loop through each line in the file
    _sum = 0
    for line in file:

        game = parse_game_line(line)
        game_failed = False
        for throw in game["throws"]:
            if throw.get("red", 0) > 12 \
                    or throw.get("green", 0) > 13 \
                    or throw.get("blue", 0) > 14:
                game_failed = True
        if not game_failed:
            _sum = _sum+int(game['game'])

    print(_sum)
        #
        # print(f"Game Name {game['game']} {game_failed}"
        #
        # )

#
# 12 red
# 13 green
# 14 blue




        #
        # game = split[0]
        # draw1 = split[1]


        # for letter in line:
        #     if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        #         numberz = numberz + letter
        # sliced = numberz[0]
        # sliced2 = numberz[-1]
        # finalnumberz = (sliced+sliced2)
        # sumnum = sumnum + int(finalnumberz)
        # print (sumnum)