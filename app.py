import sys


def main(list_of_str, expected_sum):
    input = format_input(list_of_str, expected_sum)
    result = find_list_of_pairs(input[0], input[1])
    return result


def format_input(list_of_str, expected_sum):
    return [[int(n) for n in list_of_str.split(',')], int(expected_sum)]


def find_list_of_pairs(list_of_numbers, expected_sum):
    result = []
    visited = {}
    for n in list_of_numbers:
        complement = expected_sum - n
        if visited.get(complement):
            result.append((n, complement))
            visited[complement] = False
        else:
            visited[n] = True
    return result


if __name__ == '__main__':
    r = main(sys.argv[1], sys.argv[2])
    for item in r:
        print(f"{item[0]},{item[1]}")
