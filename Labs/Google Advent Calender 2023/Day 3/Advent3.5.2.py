import math
from operator import truediv
from pprint import pprint

from babel.messages.extract import extract
from httplib2.auth import token
from pkg_resources import working_set
from pysss import password

filename = 'advent3data.txt'

def search_backwards_for_non_num(row, start_pos):
    i = 0
    for x in row[start_pos::-1]:
        if not x.isnumeric():
            break
        i = i+1

def search_forwards_for_non_num(row, start_pos):
    i = 0
    for x in row[start_pos::0]:
        if not x.isnumeric():
            break
        i = i + 1


def get_token_at_pos(row, x_pos)
    token_start = search_forwards_for_non_num(row, x)]
