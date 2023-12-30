from Utilities import *


def part1(input_list):
    sum = 0
    non_symbols = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
    coords_to_visited = {}
    symbol_coords = set()
    length_horizontal = len(input_list[0])
    length_vertical = len(input_list)
    for line_index, line in enumerate(input_list):
        for character_index, character in enumerate(line):
            coords_to_visited[(line_index, character_index)] = False
            if character not in non_symbols:
                symbol_coords.add((line_index, character_index))

    for symbol_coord in symbol_coords:
        x = symbol_coord[1]
        y = symbol_coord[0]
        symbol = input_list[y][x]
        bottom_visited = False
        bottom_right_visited = False
        top_visited = False
        top_right_visited = False
        digit_list = []
        for index in range(x + 1, length_horizontal):
            if input_list[y][index] != ".":
                digit_list.append(input_list[y][index])
            else:
                break
        if digit_list:
            sum += int("".join(digit_list))

        digit_list = []
        for index in range(x - 1, -1, -1):
            if input_list[y][index] != "." and input_list[y][index] != symbol:
                digit_list.append(input_list[y][index])
            else:
                break
        if digit_list:
            sum += int("".join(digit_list[::-1]))

        digit_list = []

        for index in range(x - 1, -1, -1):
            if input_list[y + 1][index] == ".":
                x_start = index + 1
                break
            elif index == 0:
                x_start = 0

        for index in range(x_start, length_horizontal):
            if input_list[y + 1][index] != ".":
                digit_list.append(input_list[y + 1][index])
                if index == x:
                    bottom_visited = True
                elif index == x + 1:
                    bottom_right_visited = True
            else:
                break
        if digit_list:
            sum += int("".join(digit_list))

        digit_list = []
        if not bottom_visited:
            for index in range(x, length_horizontal):
                if input_list[y + 1][index] != ".":
                    digit_list.append(input_list[y + 1][index])
                    if index == x + 1:
                        bottom_right_visited = True
                else:
                    break
            if digit_list:
                sum += int("".join(digit_list))

        digit_list = []
        if not bottom_right_visited:
            for index in range(x + 1, length_horizontal):
                if input_list[y + 1][index] != ".":
                    digit_list.append(input_list[y + 1][index])
                else:
                    break
            if digit_list:
                sum += int("".join(digit_list))

        digit_list = []

        for index in range(x - 1, -1, -1):
            if input_list[y - 1][index] == ".":
                x_start = index + 1
                break
            if index == 0:
                x_start = 0

        for index in range(x_start, length_horizontal):
            if input_list[y - 1][index] != ".":
                digit_list.append(input_list[y - 1][index])
                if index == x:
                    top_visited = True
                elif index == x + 1:
                    top_right_visited = True
            else:
                break
        if digit_list:
            sum += int("".join(digit_list))

        digit_list = []
        if not top_visited:
            for index in range(x, length_horizontal):
                if input_list[y - 1][index] != ".":
                    digit_list.append(input_list[y - 1][index])
                    if index == x + 1:
                        top_right_visited = True
                else:
                    break
            if digit_list:
                sum += int("".join(digit_list))

        digit_list = []
        if not top_right_visited:
            for index in range(x + 1, length_horizontal):
                if input_list[y - 1][index] != ".":
                    digit_list.append(input_list[y - 1][index])
                else:
                    break
            if digit_list:
                sum += int("".join(digit_list))
    return sum


def part2(input_list):
    sum = 0
    non_symbols = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
    coords_to_visited = {}
    symbol_coords = set()
    length_horizontal = len(input_list[0])
    length_vertical = len(input_list)
    for line_index, line in enumerate(input_list):
        for character_index, character in enumerate(line):
            coords_to_visited[(line_index, character_index)] = False
            if character == "*":
                symbol_coords.add((line_index, character_index))

    for symbol_coord in symbol_coords:
        x = symbol_coord[1]
        y = symbol_coord[0]
        symbol = input_list[y][x]
        bottom_visited = False
        bottom_right_visited = False
        top_visited = False
        top_right_visited = False
        gear_numbers = []
        digit_list = []
        for index in range(x + 1, length_horizontal):
            if input_list[y][index] != ".":
                digit_list.append(input_list[y][index])
            else:
                break
        if digit_list:
            gear_numbers.append(int("".join(digit_list)))

        digit_list = []
        for index in range(x - 1, -1, -1):
            if input_list[y][index] != "." and input_list[y][index] != symbol:
                digit_list.append(input_list[y][index])
            else:
                break
        if digit_list:
            gear_numbers.append("".join(digit_list[::-1]))

        digit_list = []

        for index in range(x - 1, -1, -1):
            if input_list[y + 1][index] == ".":
                x_start = index + 1
                break
            elif index == 0:
                x_start = 0

        for index in range(x_start, length_horizontal):
            if input_list[y + 1][index] != ".":
                digit_list.append(input_list[y + 1][index])
                if index == x:
                    bottom_visited = True
                elif index == x + 1:
                    bottom_right_visited = True
            else:
                break
        if digit_list:
            gear_numbers.append("".join(digit_list))

        digit_list = []
        if not bottom_visited:
            for index in range(x, length_horizontal):
                if input_list[y + 1][index] != ".":
                    digit_list.append(input_list[y + 1][index])
                    if index == x + 1:
                        bottom_right_visited = True
                else:
                    break
            if digit_list:
                gear_numbers.append("".join(digit_list))

        digit_list = []
        if not bottom_right_visited:
            for index in range(x + 1, length_horizontal):
                if input_list[y + 1][index] != ".":
                    digit_list.append(input_list[y + 1][index])
                else:
                    break
            if digit_list:
                gear_numbers.append("".join(digit_list))

        digit_list = []

        for index in range(x - 1, -1, -1):
            if input_list[y - 1][index] == ".":
                x_start = index + 1
                break
            if index == 0:
                x_start = 0

        for index in range(x_start, length_horizontal):
            if input_list[y - 1][index] != ".":
                digit_list.append(input_list[y - 1][index])
                if index == x:
                    top_visited = True
                elif index == x + 1:
                    top_right_visited = True
            else:
                break
        if digit_list:
            gear_numbers.append("".join(digit_list))

        digit_list = []
        if not top_visited:
            for index in range(x, length_horizontal):
                if input_list[y - 1][index] != ".":
                    digit_list.append(input_list[y - 1][index])
                    if index == x + 1:
                        top_right_visited = True
                else:
                    break
            if digit_list:
                gear_numbers.append("".join(digit_list))

        digit_list = []
        if not top_right_visited:
            for index in range(x + 1, length_horizontal):
                if input_list[y - 1][index] != ".":
                    digit_list.append(input_list[y - 1][index])
                else:
                    break
            if digit_list:
                gear_numbers.append("".join(digit_list))
        if len(gear_numbers) == 2:
            sum += int(gear_numbers[0]) * int(gear_numbers[1])
    return sum


if __name__ == "__main__":
    input_list = parse("Day3.txt")
    #input_list = parse("Day3Sample.txt")
    #input_list = parse("Day2Sample2.txt")
    #print(part1(input_list))
    print(part2(input_list))