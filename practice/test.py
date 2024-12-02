# # get equilibrium index
#
# l = [1, 1, 2, 2]
# l = [-7, 1, 5, 2, -4, 3, 0]
#
# # get first and last indexes of numbers in list
# # where target sum is equal to sum of element from first index till last index
#
# l = [15, 2, 4, 8, 9, 5, 10, 23]
# tsum = 23
# # indexs of = 2, 4, 8, 9


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



class A:
    def __init__(self, name):
        self.name = name
        print(f"A class constructor called. name: {self.name} ")

class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"B class constructor called. age: {self.age} ")

b = B("soni", 25)







