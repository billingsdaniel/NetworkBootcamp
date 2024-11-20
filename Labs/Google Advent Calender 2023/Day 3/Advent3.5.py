import math
from operator import truediv
from pprint import pprint

from babel.messages.extract import extract
from httplib2.auth import token
from pkg_resources import working_set
from pysss import password

filename = 'advent3data.txt'

class Token(object):
    def __init__(self, start_pos, end_pos, row_num, token_value):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.row_num = row_num
        self.token_value = token_value
    def __repr__(self):
        return f'start_pos: {self.start_pos}, end_pos: {self.end_pos}, row_num: {self.row_num}, token_value:{self.token_value}'

class StarToken(object):
    def __init__(self, pos_of_star, row_num, gear_num_count=0):
        self.pos_of_star = pos_of_star
        self.row_num = row_num
        self.gear_num_count = gear_num_count
    def __repr__(self):
        return f'pos_of_star: {self.pos_of_star}, row_num: {self.row_num}, gear_num_count: {self.gear_num_count}'


def parse_row_for_tokens(row: str, row_num: int):
    tokens = []

    working_on_token = False
    cur_token_start = None
    cur_token_end = None

    for i in range(0,len(row)):
        cur_char = row[i]
    # if number
        if str(cur_char).isnumeric():
            # if number and working on token
            if working_on_token:
                pass
            # if number and not working on token, start token
            else:
                working_on_token = True
                cur_token_start = i
        # if not number
        else:
            # if not number and working on token, end token
            if working_on_token:
                cur_token_end = i - 1
                tokens.append(
                    Token(
                        start_pos=cur_token_start,
                        end_pos=cur_token_end,
                        row_num=row_num,
                        token_value=row[cur_token_start:cur_token_end+1]
                    )
                )
                working_on_token = False
                cur_token_start = None
                cur_token_end = None
                continue
            # if not number and not wo0rking on token, skip
            else:
                continue

    return tokens

def parse_row_for_star_tokens(row: str, row_num: int):
    star_tokens = []
    #
    # cur_token_start = None
    # cur_token_end = None

    for i in range(0,len(row)):
        cur_char = row[i]
    # if number
        if str(cur_char) == "*":
            # if number and working on token
            cur_pos_of_star = i
            # if number and not working on token, start token
            star_tokens.append(
                StarToken(
                    pos_of_star=cur_pos_of_star,
                    row_num=row_num,
                )
            )
    return star_tokens


def str_has_gear(in_str):

    # assume no symbol
    has_gear = False
    # check for symbol(s)
    for x in in_str:
        if x in "*":
            has_gear = True

            break
    return has_gear

def str_has_num(in_str, in_star_token):

    # assume no symbol
    has_num = False
    # check for symbol(s)
    for x in in_str:
        if x.isnumeric():
            has_num = True
            in_star_token.gear_num_count = in_star_token.gear_num_count + 1
            break
    return has_num

def extract_numeric_indexes(in_str):
    numeric_indexes = []
    i = 0
    for x in in_str:
        if x.isnumeric():
            numeric_indexes.append(i)
        i = i+1
    return numeric_indexes

def locate_token_in_pos(x_pos, y_pos, tokens):
    for token in tokens:
        if token.row_num == y_pos:
            if x_pos >= token.start_pos and x_pos <= token.end_pos:
                return token




# Open the file in read mode
with open(filename, 'r') as file:
    rows = file.readlines()
    rows = [x.strip() for x in rows]
    rows = ["....." + row + "......" for row in rows]
    rows.append("." * len(rows[-1]))
    rows.insert(0, "." * len(rows[0]))

i = 0
tokens = []
star_tokens = []
for row in rows:

    tokens.extend(parse_row_for_tokens(row=row, row_num=i))
    star_tokens.extend(parse_row_for_star_tokens(row=row, row_num=i))
    i = i + 1

token_values = []
# for token in tokens:
#
#     above_token = rows[token.row_num-1][token.start_pos-1: token.end_pos+2]
#     below_token = rows[token.row_num + 1][token.start_pos-1: token.end_pos + 2]
#     sides_token = rows[token.row_num][token.start_pos-1: token.end_pos+2]
    # print row starting from start pos to end pos for every token
    # if str_has_gear(in_str="".join([above_token,sides_token,below_token])):
    #     token_values.append(rows[token.row_num][token.start_pos: token.end_pos+1])
    #

    #
    # print(
    #     "\n" + above_token + "\n" + sides_token + "\n" + below_token
    # )
token_int = [int(x) for x in token_values]
token_sum = sum(token_int)


star_token_values = []
star_token_tokens = set()
for star_token in star_tokens:
    above_star= rows[star_token.row_num - 1][star_token.pos_of_star - 1: star_token.pos_of_star + 2]
    sides_star= rows[star_token.row_num][star_token.pos_of_star - 1: star_token.pos_of_star + 2]
    below_star = rows[star_token.row_num+1][star_token.pos_of_star - 1: star_token.pos_of_star + 2]
    if str_has_num(in_str="".join([above_star,sides_star,below_star]), in_star_token=star_token):
        abs_cords_pos = []
        above_star_num_pos = extract_numeric_indexes(in_str=above_star)
        abs_cords_pos.extend(
            [[x+star_token.pos_of_star -1, star_token.row_num - 1] for x in above_star_num_pos]
        )
        sides_star_num_pos = extract_numeric_indexes(in_str=sides_star)
        abs_cords_pos.extend(
            [[x + star_token.pos_of_star - 1, star_token.row_num] for x in sides_star_num_pos]
        )
        below_star_num_pos = extract_numeric_indexes(in_str=above_star)
        abs_cords_pos.extend(
            [[x + star_token.pos_of_star - 1, star_token.row_num + 1] for x in below_star_num_pos]
        )
            # USE EXTRACT LOCATION NEXT
        cur_star_token_tokens = set()
        for cord in abs_cords_pos:
            cur_star_token_tokens.add(locate_token_in_pos(x_pos=cord[0], y_pos=cord[1], tokens=tokens))
        if len(cur_star_token_tokens)==2: # this is the gear that has 2 edges ( 2 numbers connected to the grid around star)





        print (abs_cords_pos, cur_star_token_tokens)


        # sides_star_num_pos = extract_numeric_indexes(in_str=sides_star)
        # below_star_num_pos = extract_numeric_indexes(in_str=below_star)


        # for numeric in above_star append to star_token_tokens



        #
        #
        # for x in star_token_token
        # print(
        #     "\n" + above_star + "\n" + sides_star + "\n" + below_star
        # )


        # if star_token.gear_num_count == 2:
        #     above_star_2 = rows[star_token.row_num - 1][star_token.pos_of_star - 5: star_token.pos_of_star + 5]
        #     sides_star_2 = rows[star_token.row_num][star_token.pos_of_star - 5: star_token.pos_of_star + 5]
        #     below_star_2 = rows[star_token.row_num + 1][star_token.pos_of_star - 5: star_token.pos_of_star + 5]
        #     str_has_num(in_str="".join([above_star_2, sides_star_2, below_star_2]), in_star_token=star_token)
        #
        #     for token in tokens:
        #         above_token = rows[token.row_num - 1][token.start_pos - 1: token.end_pos + 2]
        #         below_token = rows[token.row_num + 1][token.start_pos - 1: token.end_pos + 2] # star_token_values.append(token_values)
        #         sides_token = rows[token.row_num][token.start_pos - 1: token.end_pos + 2]
        #         if str_has_gear(in_str="".join([above_token, sides_token, below_token])):
        #             token_values.append(rows[token.row_num][token.start_pos: token.end_pos + 1])
        #             print( # star_token_values.append(token_values)
        #                 "\n" + above_token + "\n" + sides_token + "\n" + below_token
        #             )
        #         # print(
        #         #     "\n" + above_star + "\n" + sides_star + "\n" + below_star
        #         # )
        # else:
        #     continue:


# print(
#     star_token_values
# )
# is i a number, then add to token

# # print(tokens[0].)
# for token in tokens:
#     print(
#         a[token.start_pos:token.end_pos+1]
#     )


#
# tokens = []
# for row in rows:
#     row_tokens = parse_row_for_tokens(row)
#     tokens.extend(row_tokens)
#
#
#
#     from pprint import pprint
#
#     tokens = parse_row(
#         row_num=1,
#         row=a,
#     )
#     pprint.pprint(rows)


#     # Loop through each line in the file
#     _sum = 0
#     for line in file:
#
#         game = parse_game_line(line)


#         game_failed = False
#         for throw in game["throws"]:
#             if throw.get("red", 0) > 12 \
#                     or throw.get("green", 0) > 13 \
#                     or throw.get("blue", 0) > 14:
#                 game_failed = True
#         if not game_failed:
#             _sum = _sum+int(game['game'])
#
#     print(_sum)
#