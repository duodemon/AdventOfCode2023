from Utilities import *


def part1(input_list):
    sum = 0
    for line in input_list:
        i = 0
        first_digit = None
        last_digit = None
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i in range(len(line)):
            if first_digit is None and line[i] in digits:
                first_digit = line[i]
            if last_digit is None and line[len(line) - i - 1] in digits:
                last_digit = line[len(line) - i - 1]
            if first_digit is not None and last_digit is not None:
                break
        sum += int(first_digit + last_digit)
    return sum


def part2(input_list):
    sum = 0
    for line in input_list:
        i = 0
        first_digit = None
        last_digit = None
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        words_to_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        for i in range(len(line)):
            if first_digit is None:
                if line[i] in digits:
                    first_digit = line[i]
                else:
                    if i + 2 < len(line) and line[i:i+3] in words_to_digits:
                        first_digit = words_to_digits[line[i:i+3]]
                    if i + 3 < len(line) and line[i:i+4] in words_to_digits:
                        first_digit = words_to_digits[line[i:i+4]]
                    if i + 4 < len(line) and line[i:i+5] in words_to_digits:
                        first_digit = words_to_digits[line[i:i+5]]
            if last_digit is None:
                if line[len(line) - i - 1] in digits:
                    last_digit = line[len(line) - i - 1]
                else:
                    if len(line) - i - 3 >= 0 and line[len(line) - i - 3: len(line) - i] in words_to_digits:
                        last_digit = words_to_digits[line[len(line) - i - 3: len(line) - i]]
                    if len(line) - i - 4 >= 0 and line[len(line) - i - 4: len(line) - i] in words_to_digits:
                        last_digit = words_to_digits[line[len(line) - i - 4: len(line) - i]]
                    if len(line) - i - 5 >= 0 and line[len(line) - i - 5: len(line) - i] in words_to_digits:
                        last_digit = words_to_digits[line[len(line) - i - 5: len(line) - i]]
            if first_digit is not None and last_digit is not None:
                break
        sum += int(first_digit + last_digit)
    return sum


if __name__ == "__main__":
    input_list = parse("Day1.txt")
    #input_list = parse("Day1Sample1.txt")
    #input_list = parse("Day1Sample2.txt")
    #print(part1(input_list))
    print(part2(input_list))