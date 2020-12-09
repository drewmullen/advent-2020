#! /usr/bin/env python3

# for every num
# subtract next num
# unless sum over 2020
# find_2_nums_that_add_to_sum 

from d1p1 import *

TOTAL = 2020

def find_3_nums_that_add_to_sum(all_nums, total=TOTAL):
    for i, num in enumerate(all_nums):
        temp_array = all_nums[:]
        del(temp_array[i])
        product = find_2_nums_that_add_to_sum(temp_array, (total-num))
        if product:
            print(f'{str(total)} - {num} = want {total-num}')
            return product*num


if __name__ == '__main__':
    all_nums = convert_input_to_int_list('input.txt')
    product = find_3_nums_that_add_to_sum(all_nums)
    print(product)