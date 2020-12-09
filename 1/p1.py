#! /usr/bin/env python3

# x = 2020 - n
# if x in list
# multiply n * x


def convert_input_to_int_list(inputfile):
    f = open(inputfile, "r")
    return [int(line.strip()) for line in f]

def find_2_nums_that_add_to_sum(num_list, total):
    for n in num_list:
        x = total - n
        if x in num_list:
            print(f'n: {n} * x: {x} = total {total}')
            return x*n


if __name__ == '__main__':
    all_nums = convert_input_to_int_list('input.txt')
    product = find_2_nums_that_add_to_sum(all_nums, 2020)
    print(product)