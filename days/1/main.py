import wordtodigits


def add_first_and_last_number(numbers):
    """
    Receive string of numbers and letters and return a combination the first digit and the last digit (in that order) to form a single two-digit number.
    Note that the number can be spelled out so you need to account for real numbers and the english word for the number.
    :param numbers: str
    :return: int
    """
    # remove all non-numeric characters
    number_word_to_digit_dict = {
        "nine": 9,
        "eight": 8,
        "seven": 7,
        "six": 6,
        "five": 5,
        "four": 4,
        "three": 3,
        "two": 2,
        "one": 1,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    # replace occurances of words with digits
    digits_to_insert = {}
    for word, digit in number_word_to_digit_dict.items():
        if (idx := numbers.find(word)) >= 0:
            digits_to_insert[idx] = str(digit)
        if (idx := numbers.rfind(word)) >= 0:
            digits_to_insert[idx] = str(digit)
    sorted_numbers = dict(sorted(digits_to_insert.items()))
    # return the first and last digit
    return int(sorted_numbers[min(sorted_numbers.keys())] + sorted_numbers[max(sorted_numbers.keys())])


if __name__ == "__main__":
    # read text file as input
    with open('input.txt') as f:
        input = f.read()

    # loop through lines in the input and add total sum of each line to output
    output = []
    for line in input.splitlines():
        output.append(add_first_and_last_number(line))

    # print output
    print(sum(output))
