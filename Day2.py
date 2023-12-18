from Utilities import *


def part1(input_list):
    sum = 0
    color_to_number = {"blue": 14, "red": 12, "green": 13}
    for line_index, line in enumerate(input_list):
        bag_info = line.split(": ")[1]
        bag_info_split = bag_info.split("; ")
        impossible = False
        for subset in bag_info_split:
            if impossible:
                break
            number_and_color_list = subset.split(", ")
            for number_and_color in number_and_color_list:
                number = int(number_and_color.split(" ")[0])
                color = number_and_color.split(" ")[1]
                if number > color_to_number[color]:
                    impossible = True
                    break
        if not impossible:
            sum += line_index + 1
    return sum



def part2(input_list):
    sum = 0
    for line_index, line in enumerate(input_list):
        bag_info = line.split(": ")[1]
        bag_info_split = bag_info.split("; ")
        color_to_min_number = {"blue": 0, "red": 0, "green": 0}
        for subset in bag_info_split:
            number_and_color_list = subset.split(", ")
            for number_and_color in number_and_color_list:
                number = int(number_and_color.split(" ")[0])
                color = number_and_color.split(" ")[1]
                if number > color_to_min_number[color]:
                    color_to_min_number[color] = number
        power = color_to_min_number["blue"] * color_to_min_number["red"] * color_to_min_number["green"]
        sum += power
    return sum


if __name__ == "__main__":
    input_list = parse("Day2.txt")
    #input_list = parse("Day2Sample.txt")
    #input_list = parse("Day2Sample2.txt")
    #print(part1(input_list))
    print(part2(input_list))