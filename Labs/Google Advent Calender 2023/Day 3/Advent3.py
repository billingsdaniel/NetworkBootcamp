import math
from operator import truediv
from pprint import pprint

from httplib2.auth import token
from pkg_resources import working_set
from pysss import password

filename = 'advent3data.txt'

class Token(object):
    def __init__(self, start_pos, end_pos, row_num):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.row_num = row_num
    def __repr__(self):
        return f'start_pos: {self.start_pos}, end_pos: {self.end_pos}, row_num: {self.row_num}'

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

def str_has_symbol(in_str):

    # assume no symbol
    has_symbol = False
    # check for symbol(s)
    for x in in_str:
        if x in "!@#$%^&*-+/=":
            has_symbol = True
            break
    return has_symbol


# Open the file in read mode
with open(filename, 'r') as file:
    rows = file.readlines()
    rows = [x.strip() for x in rows]
    rows = ["." + row + "." for row in rows]
    rows.append("." * len(rows[-1]))
    rows.insert(0, "." * len(rows[0]))

i = 0
tokens = []
for row in rows:

    tokens.extend(parse_row_for_tokens(row=row, row_num=i))
    i = i + 1

token_values = []
for token in tokens:

    above_token = rows[token.row_num-1][token.start_pos-1: token.end_pos+2]
    below_token = rows[token.row_num + 1][token.start_pos-1: token.end_pos + 2]
    sides_token = rows[token.row_num][token.start_pos-1: token.end_pos+2]
    # print row starting from start pos to end pos for every token
    if str_has_symbol(in_str="".join([above_token,sides_token,below_token])):
        token_values.append(rows[token.row_num][token.start_pos: token.end_pos+1])


token_int = [int(x) for x in token_values]
token_sum = sum(token_int)
print(
token_sum
        )


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