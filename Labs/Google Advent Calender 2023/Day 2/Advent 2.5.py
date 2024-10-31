import math
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

#
# check the bag of dicts for throw values
# compare throw values to each other\
# print (?) highest value for each colour into new dict
# multiply highest colour value by each other to get colour power
# sum colour power of each game



# Open the file in read mode
with open(filename, 'r') as file:
    # Loop through each line in the file
    _sum = 0
    for line in file:

        game = parse_game_line(line)
        game_colour_max_value = {
            "red":1, "blue":1, "green":1
        }
        for throw in game["throws"]:
            for colour in ["red", "blue", "green"]:
                game_colour_max_value[colour] = max(game_colour_max_value[colour], throw.get(colour, 0))
        colour_power = math.prod(game_colour_max_value.values())
        _sum = _sum + colour_power



        print(_sum)


        #     if throw.get("red", 0) > 12 \
        #             or throw.get("green", 0) > 13 \
        #             or throw.get("blue", 0) > 14:
        #         game_failed = True
        # if not game_failed:
        #     _sum = _sum+int(game['game'])

    # print(_sum)
        #
        # print(f"Game Name {game['game']} {game_failed}"
        #
#         # )
#


