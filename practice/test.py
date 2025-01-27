def get_logic_type_of_table(directory):
    import os

    with open('../resources/tenantization.wfm.json', 'r') as f:
        tenantization_dict = json.load(f)

    logic_type_1 = []
    logic_type_2 = []
    logic_type_3 = []
    logic_type_4 = []
    logic_type_10 = []
    other = {}
    c = 0
    table_not_found = []
    for filename in os.listdir(directory):
        if ('.csv' or '.parquet') in filename:
            table = filename.split('.')[0]
            # c+=1
            for data in tenantization_dict:
                table_tenn_json = data['tablename']
                table_tenn_json = table_tenn_json.split('_')
                tenn_table = ''
                for word in table_tenn_json:
                    if tenn_table:
                        tenn_table = tenn_table + '_' + word.lower()
                    else:
                        tenn_table = tenn_table + word.lower()
                # print(tenn_table)
                # print(table)
                if tenn_table == table:
                    # print(table)
                    # print(tenn_table)
                    c += 1
                    # pass

            else:
                print(f'{table}, not found in tennatization.json')

                    # if data['logictype'] == 1:
                    #     logic_type_1.append(table)
                    # elif data['logictype'] == 2:
                    #     logic_type_2.append(table)
                    # if data['logictype'] == 3:
                    #     logic_type_3.append(table)
                    #     print(data)
                    #     print(table)
                    #     c += 1
                    # elif data['logictype'] == 4:
                    #     logic_type_4.append(table)
                    # elif data['logictype'] == 10:
                    #     logic_type_10.append(table)
                    # else:
                    #     other[table] = data['logictype']
            # else:
            #     table_not_found.append(table)
    print(c)

    # for table in logic_type_3:
    #     print(table)

    # print()
    # for table in table_not_found:
    #     print(table)
    # print(f'logic_type_1 \n{logic_type_1}\n')
    # print(f'logic_type_2 \n{logic_type_2}\n')
    # print(f'logic_type_3 \n{logic_type_3}\n')
    # print(f'logic_type_4 \n{logic_type_4}\n')
    # print(f'logic_type_10 \n{logic_type_10}\n')
    # print(f'other \n{other}\n')
    # print(f'table_not_found\n {table_not_found}')



# # get first and last indexes of numbers in list
# # where target sum is equal to sum of element from first index till last index
#
# l = [15, 2, 4, 8, 9, 5, 10, 23]
# tsum = 23
# # indexs of = 2, 4, 8, 9
import asyncio
import csv
import itertools
import json
import multiprocessing
import os.path
import time
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import requests
from selenium import webdriver


# def find_indices_with_target_sum(nums, target):
#     current_sum = 0
#     start_index = 0
#     index_map = {}
#
#     for end_index, num in enumerate(nums):
#         current_sum += num
#
#         while current_sum > target and start_index <= end_index:
#             current_sum -= nums[start_index]
#             start_index += 1
#
#         if current_sum == target:
#             return start_index, end_index
#
#         index_map[current_sum] = end_index
#
#     return -1, -1
#
#
# # Example usage
# nums = [1, 2, 3, 7, 5]
# # target = 12
# target = 5
# start, end = find_indices_with_target_sum(nums, target)
# print(f"The indices with target sum {target} are: {start} to {end}")


# def get_substring(s_):
#
#     c_s = set(s_)
#     d = {}
#     for c in s_:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#
#     for k, v in d.items():
#         if v >= 2:
#             c_s.remove(k)
#     print(c_s, len(c_s))


# get_substring("ababcde")


# ---------------------------------------------------------------------------

def sort_(value):
    res = sorted(value, key=lambda v: v['city'])
    return res


def sort_2(value):
    # res = {k:dict(sorted(v.items(), key=lambda item: item[0])) for k, v in value.items()}
    # return res

    res = dict(map(lambda item: (item[0], sorted(item[1].items(), key=lambda v: v[1])), value.items()))
    return res


# if __name__ == '__main__':
# input_l = [{"name": 'sourav', "age": 30, 'city': 'gwl'},
#            {"name": 'aman', "age": 35, 'city': 'delhi'},
#            {"name": 'pankaj', "age": 56, 'city': 'beng'}
#            ]
#
# input_d = {
#     'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
#     'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
#     'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}
# }
# # print(sort_(input_l))
# print(sort_2(input_d))


# -------------------------------test----------------------------------------
# def compare_dict(d1, d2):
#     flag = True
#     for key in d1:
#         if key not in d2:
#             flag = False
#             print(f'{key} key not found in d2')
#         else:
#             if d1[key] != d2[key]:
#                 flag = False
#                 print(f'{key}"s value not matching')
#     for key in d2:
#         if key not in d1:
#             flag = False
#             print(f'{key} key not found in d1')
#
# dict2 = {"a": 1, "b": 2, "c": 3, "d": 6, "f": 10}
# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# compare_dict(dict1, dict2)


# def add_occurance_string(string_):
#     l = len(string_)
#     op_str = ''
#     char = []
#     for i in range(l):
#         if i < l-1:
#             if string_[i] == string_[i+1]:
#                 char.append(string_[i])
#             else:
#                 char.append(string_[i])
#                 if i < l - 2:
#                     op_str += str(len(char)) + string_[i]
#                     char = []
#         else:
#             if string_[i] == string_[i-1]:
#                 op_str = op_str + str(len(char)+1) + string_[i]
#             else:
#                 op_str = op_str + str(len(char)) + string_[i-1] + '1' + string_[i]
#     print(op_str)
#
# add_occurance_string('aaaabbbccadddbbcccf')


# async def fetch(url):
#     async with aiohttp.ClientSession() as s:
#         async with s.get(url) as res:
#             return res.status
#
# async def fetch2(url, s):
#     async with s.get(url) as res:
#         return res.status
#
# async def main2(url):
#     res = await fetch(url)
#     print(res)

#
# def add_two_nums_from_string_using_carry2(n1, n2):
#     res = ''
#     carry = 0
#     i, j = len(n1)-1, len(n2)-1
#     while i >= 0 or j >= 0 or carry:
#         digit1 = int(n1[i]) if i >= 0 else 0
#         digit2 = int(n2[j]) if j >= 0 else 0
#
#         digit_sum = digit1 + digit2 + carry
#         carry = digit_sum // 10
#
#         res = str(digit_sum % 10) + res
#         i -= 1
#         j -= 1
#     print(res)
#
# if __name__ == '__main__':
#     # asyncio.run(main2("https://www.verint.com/"))
#     add_two_nums_from_string_using_carry2('1099', '108')

