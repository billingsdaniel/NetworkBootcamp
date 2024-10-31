def add_spelled_numbers(in_line: str):
    num_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }

    for num_str in num_map.keys():
        if num_str in in_line:
            in_line = in_line.replace(num_str, f'{num_str}{num_map[num_str]}{num_str}')
    print(in_line)

    return in_line


with open('advent1.txt') as f:
    lines = f.readlines()

    _sum = 0
    for line in lines:
        line = add_spelled_numbers(in_line=line)
        line_nums = [x for x in line if str(x).isnumeric()]
        left = line_nums[0]
        right = line_nums[-1]
        _sum = _sum + int(f'{left}{right}')
    print(_sum)