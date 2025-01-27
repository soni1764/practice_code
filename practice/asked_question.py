# 1.----------------------------------------Print all Substring----------------------------------------------------
import itertools
import os
import time
from itertools import permutations


def print_all_substring(given_string, n):
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += given_string[j]
            print(temp)


# if __name__ == '__main__':
#     s = "English"
#     print_all_substring(s, len(s))


# ----------------------------------------Compare two dictionaries----------------------------------------------------
def compare_dict(d1, d2):
    flag = True
    for key in d1:
        if key in d2:
            if not d1[key] == d2[key]:
                print(f'Difference D1 {key}:{d1[key]}, D2 {key}:{d2[key]}')
                flag = False
        else:
            print(f'D1 key {key} not found in D2')
            flag = False

    for key in d2:
        if key not in d1:
            print(f'D2 key {key} not found in D1')
            flag = False

    if flag:
        print('Both dictinaries D1 and D2 are same')
    else:
        print("Both dictinaries D1 and D2 are different")


def compare_dict2(d1, d2):
    flag = True
    for key in d1:
        if key not in d2:
            print(f"not equal, key {key} not found in d2")
            flag = False
        else:
            if d1[key] != d2[key]:
                print(f"not equal, key {key} value not equal {key}: value in d1: {d1[key]} and value in d2: {d2[key]}")
                flag = False
    for key in d2:
        if key not in d1:
            print(f"not equal, key {key} not found in d1")
            flag = False

    if flag:
        print("Equals")
    else:
        print("Not equals")


# if __name__ == '__main__':
#     dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#     dict2 = {"a": 1, "b": 2, "c": 3, "d": 6, "f": 10}
#
#     # dict1 = {"a": 1, "b": 2, "c": 3}
#     # dict2 = {"a": 1, "b": 2, "c": 3}
#     compare_dict(dict1, dict2)
#     compare_dict2(dict1, dict2)


# ------------------------format_string_with_occurrence---------------------------------------------------------------
class MyClass:
    format_string = ''

    def format_string_with_occurrence(self, given_string, n):
        l_ch = []
        for i in range(n):
            if i < n - 1:
                if given_string[i] == given_string[i + 1]:
                    l_ch.append(given_string[i])
                else:
                    l_ch.append(given_string[i])
                    if not i == n - 2:
                        self.format_string = self.format_string + str(len(l_ch)) + given_string[i]
                        l_ch = []
            else:
                if given_string[i] == given_string[i - 1]:
                    self.format_string = self.format_string + str(len(l_ch) + 1) + given_string[i]
                else:
                    self.format_string = self.format_string + str(len(l_ch)) + given_string[i - 1] + "1" + given_string[
                        i]

        print(self.format_string)


def format_string_with_occurrence2(given_string, n):
    formatted_string = ''
    char_list = []
    for i in range(n):
        if i < n - 1:
            if given_string[i] == given_string[i + 1]:
                char_list.append(given_string[i])
            else:
                char_list.append(given_string[i])
                if i < n - 2:
                    formatted_string += str(len(char_list)) + given_string[i]
                    char_list = []
        else:
            if given_string[i] == given_string[i - 1]:
                formatted_string += str(len(char_list) + 1) + given_string[i]
            else:
                formatted_string += str(len(char_list)) + given_string[i - 1] + '1' + given_string[i]

    print(formatted_string)


# if __name__ == '__main__':
#     s = "aaaabbbccadddbbcccf"
#     # mc = MyClass()
#     # mc.format_string_with_occurrence(s, len(s))
#     format_string_with_occurrence2(s, len(s))


# -----------------------------get sum of all numbers in nested list ------------------
def get_sum(nums):
    total = 0
    for ele in nums:
        if isinstance(ele, list):
            # if type(ele) == type([]):
            total += get_sum(ele)
        else:
            total += ele
    return total


# if __name__ == "__main__":
#     total_ = get_sum([1, 2, 3, [4, 5], 6])
#     print(total_)


# -----------------------------flatten nested list ------------------
def flatten(given_list, res=[]):
    for ele in given_list:
        if isinstance(ele, list):
            flatten(ele, res)
        else:
            res.append(ele)
    return res


# if __name__ == "__main__":
#     total_ = flatten([1, [2, 3, [4, 5]], 6])
#     print(total_)


# -----------------------------get longest palindrome from string ------------------

def get_longest_palindrome(given_string):
    n = len(given_string)
    longest_p = ''

    for i in range(n):
        for j in range(i + 1, n + 1):
            word = given_string[i:j]
            if word == word[::-1]:  # checking palindrome here, if reverse and self are equals
                if len(word) > len(longest_p):
                    longest_p = word

    print(longest_p)


# if __name__ == "__main__":
#     get_longest_palindrome("acaabcbamalayalam")


# -----------------------------get longest common prefix from the list elements------------------
def longest_common_prefix(words):
    if not words:
        print("List is empty")

    else:
        common_prefix = words[0]
        # getting the shortest word
        for word in words:
            if len(word) < len(common_prefix):
                common_prefix = word

        for _ in common_prefix:
            for word in words:
                if common_prefix not in word:
                    common_prefix = common_prefix[:-1]

        print(common_prefix)


def longest_common_prefix2(words):
    if not words:
        print("List is empty")

    else:
        words.sort()
        print(words)
        comm_word = words[0]

        # print(comm_word)

        for i in comm_word:
            status = is_char_present_in_list_element(comm_word, words)
            if not status:
                comm_word = comm_word[:-1]
        print(comm_word)


def is_char_present_in_list_element(word, list_):
    for ele in list_:
        if word not in ele:
            return False
    else:
        return True


# if __name__ == '__main__':
#     w = ["flower", "flow", "floght", "flows"]
#     longest_common_prefix(w)
# longest_common_prefix2(w)


# -----------------------------search all permutaions of a string in given string------------------
def get_per(a):
    for p in permutations(a):
        # print(p)
        print(''.join(p))


def get_per2(a):
    p = [''.join(p) for p in permutations(a)]
    print(p)


def get_per_of_a_in_b(a, b):
    perms = [''.join(p) for p in permutations(a)]
    # ans = [p for p in perms if p in b]
    # print(ans)
    for p in perms:
        if p in b:
            print(p)


# if __name__ == "__main__":
#     small_str = "abc"
#     large_str = "cbabadcbbabbcbabaabccbabc"
#     get_per(small_str)
#     get_per2(small_str)
#     get_per_of_a_in_b(small_str, large_str)


def search_all_perm(given_string, string_to_search):
    pass


# if __name__ == "__main__":
#     search_all_perm("", "")


# ----------------------------------program to wait for file in a drive----------------------------------
def wait_for_file(file_path, interval):
    # while not os.path.exists(file_path):
    while not os.path.isfile(file_path):
        time.sleep(interval)
        print("waiting for file")
    print("File appeared")


# if __name__ == "__main__":
#     wait_for_file("test.csv", 2)


# ----------------------------------program to get alphanumeric string from list-----------------------------------
def is_alnum(string_):
    for char in string_:
        if not (char.isdigit() or char.isalpha()):
            return False
    return True


def get_alpha_num_string(list_):
    an = []
    # for word in list_:
    #     if type(word) == str and len(word) >=2:
    #         # if word.isalnum():
    #         #     print(word, end=', ')
    #         if is_alnum(word):
    #             an.append(word)
    an = [word for word in list_ if type(word) == str and len(word) >=2 if is_alnum(word)]
    print(an)


# if __name__ == "__main__":
#     get_alpha_numeric_string([1, "abc12", "abc", "xyz12", "123"])


# ----------------------------------program to find equilibrium index------------------------------
def get_equilibrium_index(given_list, n):
    for i in range(n):
        left_sum = sum(given_list[:i])
        right_sum = sum(given_list[i + 1:])
        if left_sum == right_sum:
            return f"Equilibrium index is: {i}"
    return -1


def get_equilibrium_index2(given_list, n=0):
    right_sum = sum(given_list)
    left_sum = 0
    for i, num in enumerate(given_list):
        right_sum -= num
        if left_sum == right_sum:
            return f"Equilibrium index is: {i}"
        left_sum += num
    return -1


# if __name__ == "__main__":
#     l_ = [-4, 1, 5, 2, -4, 4, 2]
#     print(get_equilibrium_index(l_, len(l_)))
#     print(get_equilibrium_index2(l_, len(l_)))

# -----------------------------get start and end index for target sum----------------------------------------
def find_indices_with_target_sum(nums, target):
    current_sum = 0
    start_index = 0
    index_map = {}

    for end_index, num in enumerate(nums):
        current_sum += num

        while current_sum > target and start_index <= end_index:
            current_sum -= nums[start_index]
            start_index += 1

        if current_sum == target:
            return start_index, end_index

        index_map[current_sum] = end_index

    return -1, -1


# # Example usage
# nums = [1, 2, 3, 7, 5]
# # target = 12
# target = 5
# start, end = find_indices_with_target_sum(nums, target)
# print(f"The indices with target sum {target} are: {start} to {end}")


# -----------program to find start and end index from list where element sum is equal to given target sum--------------


# ----------------------------------find product/combination using itertools--------------------------------------
def get_product_combination(list1, list2):
    print(list(itertools.product(list1, list2)))


# if __name__ == "__main__":
#     l1 = [1, 2, 3]
#     l2 = [4, 5, 6]
#     get_product_combination(l1, l2)


# -------------------------get_count_of_operation_to_make_num_0-----------------------------------------------
def get_count_of_operation_to_make_num_0(given_string):
    V = int(given_string, 2)
    count = 0
    while V != 0:
        if V % 2 == 0:
            V = V // 2
        else:
            V = V - 1
        count += 1
    return count


# if __name__ == "__main__":
#     c = get_count_of_operation_to_make_num_0('1111010101111')
#     print(c)

# ------------------------------get shortest balanced fragment (both upper and lower case exist)-----------------
def shortest_balanced_fragment(S):
    def is_balanced(sub):
        lower = set()
        upper = set()
        for char in sub:
            if char.islower():
                lower.add(char)
            elif char.isupper():
                upper.add(char.lower())
        # print(lower, upper)
        return lower == upper

    n = len(S)
    min_length = float('inf')
    # min_length = n
    result = ""

    for start in range(n):
        for end in range(start + 1, n + 1):
            fragment = S[start:end]
            if is_balanced(fragment):
                if end - start < min_length:
                    min_length = end - start
                    result = fragment

                # if min_len > len(fragment):
                #     min_len = len(fragment)
                #     result = fragment
    print(result)
    return len(result) if min_length != float('inf') else -1


# if __name__ == "__main__":
#     # Example usage
#     S = "CATattac"
#     print(f"The shortest balanced fragment in '{S}' is '{shortest_balanced_fragment(S)}'")


# -------------------------get sum of element in two list at index using lambda and map----------------------------
def get_sum_at_index(l1, l2):
    add = lambda a, b: a + b
    sum_ = list(map(add, l1, l2))
    print(sum_)


# if __name__ == "__main__":
#     get_sum_at_index([1, 2, 3, 4], [5, 6, 7, 8, 9])


# ------------------get all possible palindrome in a string---------------------------------------------

def get_all_palindrome(given_string):
    n = len(given_string)
    for start in range(n):
        for end in range(start + 1, n + 1):
            sub_string = given_string[start:end]
            if len(sub_string) > 1 and sub_string == sub_string[::-1]:
                print(sub_string)


# if __name__ == "__main__":
#     get_all_palindrome("abcacbdcacbab")


# ------------------find all index of vowel in a list---------------------------------------------
def get_all_index(given_list):
    vowel = "aeiouAEIOU"
    vowel_dict = {}
    for idx, char in enumerate(given_list):
        if char in vowel:
            if char not in vowel_dict:
                vowel_dict[char] = []
            vowel_dict[char].append(idx)
    print(vowel_dict)


# if __name__ == "__main__":
#     s = "Gourav Soni"
#     get_all_index(s)


# -------------------sort list of dict using key---------------------------------------------------------------------
def sort_list_by_key(given_list):
    new_list = sorted(given_list, key= lambda d: d['age'], reverse=False)
    print(new_list)


# if __name__ == "__main__":
#     l = [
#         {'name': "sourav", 'age': 30},
#         {'name': "ajay", 'age': 25},
#         {'name': "vimal", 'age': 28}
#     ]
#     sort_list_by_key(l)


# -----------------------check if brackets are balanced ---------------------------------
# input_ = "{{][}}}()[]"

def is_balanced(string_):
    p_count = 0
    c_count = 0
    s_count = 0
    for char in string_:
        if char == '(':
            p_count += 1
        elif char == ')':
            p_count -= 1
            if p_count < 0:
                return False
        elif char == '{':
            c_count += 1
        elif char == '}':
            c_count -= 1
            if c_count < 0:
                return False
        elif char == '[':
            s_count += 1
        elif char == ']':
            s_count -= 1
            if s_count < 0:
                return False

    return p_count == 0 and c_count == 0 and s_count == 0


# if __name__ == "__main__":
#     s = "({[()]}{})"
#     res = is_balanced(s)
#     print(res)

# ----------------------check if brackets are balanced------------------------------------------
def is_balanced2(s):
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to map closing brackets to opening ones
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Loop through each character in the string
    for char in s:
        # If it's an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map.keys():
            # Check if the stack is empty or top of the stack doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Pop the matched opening bracket from the stack

    # If the stack is empty, all brackets matched correctly
    return not stack

# if __name__ == "__main__":
# Test cases
#     print(is_balanced2("()"))  # True
#     print(is_balanced2("{[()]}"))  # True
#     print(is_balanced2("([)]"))  # False
#     print(is_balanced2("{[(])}"))  # False
#     print(is_balanced2("((()))"))  # True
#     print(is_balanced2("{[}"))  # False

# --------------------------find duplicate in list--------------------------------------------------
def get_duplicate(given_list):
    duplicate_ = []
    n = len(given_list)
    for i in range(n):
        for j in range(i+1, n):
            if given_list[j] == given_list[i] and given_list[i] not in duplicate_:
                duplicate_.append(given_list[i])
    print(duplicate_)

    unique_2= []
    duplicate_2 = []
    for i in given_list:
        if i not in unique_2:
            unique_2.append(i)
        elif i not in duplicate_2:
            duplicate_2.append(i)

    print(unique_2)
    print(duplicate_2)

# if __name__ == "__main__":
#     l_ = [1, 2, 4, 5, 5, 6, 7, 8, 8, 9]
#     get_duplicate(l_)

# -------------------call common method from parent class using subclass-----------------------------------------------------
class A:
    # def __init__(self):
    #     print("class A constructor")
    #     # print(msg)

    def method_A(self):
        print("class A method")

    def common(self):
        print("class A common method")

class B(A):
    # def __init__(self):
    #     # super().__init__()
    #     print("class B constructor")

    def method_B(self):
        print("class B method")

    def common(self):
        print("class B common method")

class C(B):
    # def __init__(self):
    #     # super().__init__()
    #     print("class C constructor")

    def method_C(self):
        print("class C method")

    def common(self):
        print("class C common method")


# a = A("ellow")
# if __name__ == '__main__':
#     c = C()
#     c.common()
#     super(C, c).common()
#     super(B, c).common()


# ----------------------return string in capital using decorator--------------------------------------------------
def deco_capital(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
        # return func(*args, **kwargs).upper()
    return wrapper


@deco_capital
def funtest(s):

    return s


# if __name__ == "__main__":
    # r = funtest("accolite")

    # print(r)


# -------------------------sort dict of dict using value(inner dict)---------------------------------------------------------
def sort_by_values_inner(inner_dict):
    return dict(sorted(inner_dict.items(), key=lambda item: item[1]))


def sort_by_values(given_dict):
    sorted_dict = {key: sort_by_values_inner(value) for key, value in given_dict.items()}
    print(sorted_dict)


def sort_by_values2(given_dict):
    sorted_dict = {key: dict(sorted(value.items(), key=lambda item: item[1])) for key, value in given_dict.items()}

    print(sorted_dict)


def sort_by_values3(given_dict):
    sorted_dict = dict(
        map(lambda item: (item[0], dict(sorted(item[1].items(), key=lambda v: v[1]))), given_dict.items()))

    print(sorted_dict)


def sort_by_values4(given_dict):
    sorted_dict = dict(map(lambda item: (item[0], dict(sorted(item[1].items(), key=lambda v: v[1], reverse=True))),
                           given_dict.items()))

    print(sorted_dict)


input_ = {
    'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
    'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
    'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}

}

# output_ = {
#     'Nikhil': {'Maths': 2, 'English': 5, 'Science': 14},
#     'Akash': {'Science': 2, 'Maths': 7,'English': 15,},
#     'Akshat': {'English': 5, 'Science': 20, 'Maths': 50}

#     }


# if __name__ == "__main__":
#     sort_by_values(input_)
#     sort_by_values2(input_)
#     sort_by_values3(input_)
#     sort_by_values4(input_)

# -----------------------get sliding max of 3 nums from list---------------------------------------
def get_sliding_max_of_3_num(nums, k):
    l = []
    for i in range(len(nums)-k+1):
        l.append(max(nums[i:i+k]))
    print(l)
    # or
    print([max(nums[i:i + k]) for i in range(len(nums)-k+1)])


# if __name__ == '__main__':
#     get_sliding_max_of_3_num([1, -2, 2, 3, 3, 4, 5, 3, 4, 1, -1, 7], 3)


# -------------------add two nums(are in string) and handle carry as we do in math-----------------------
def add_two_nums_from_string_using_carry(n1, n2):
    max_l = max(len(n1), len(n2))
    n1 = n1.zfill(max_l)
    n2 = n2.zfill(max_l)
    print(n1, n2)
    res = ''
    carry = 0
    for i in range(max_l-1, -1, -1):

        digit_sum = int(n1[i]) + int(n2[i]) + carry
        carry = digit_sum // 10
        res = str(digit_sum % 10) + res

    if carry:
        res = str(carry) + res
    print(res)


#without adding zero in starting
def add_two_nums_from_string_using_carry2(n1, n2):
    res = ''
    carry = 0
    i, j = len(n1)-1, len(n2)-1
    while i >= 0 or j >= 0 or carry:
        digit1 = int(n1[i]) if i >= 0 else 0
        digit2 = int(n2[j]) if j >= 0 else 0

        digit_sum = digit1 + digit2 + carry
        carry = digit_sum // 10

        res = str(digit_sum % 10) + res
        i -= 1
        j -= 1
    print(res)


# if __name__ == '__main__':
#     add_two_nums_from_string_using_carry('1018', '109')

# ----------------------How to download a file in python-----------------------------------
import requests

def download_file(url, local_filename):
    # Send a GET request to the URL
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Check if the request was successful
        # Open a local file with write-binary mode
        with open(local_filename, 'wb') as file:
            # Write the content to the local file in chunks
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"Downloaded {local_filename}")

# Example usage
url = "https://example.com/path/to/file"
local_filename = "downloaded_file.ext"
download_file(url, local_filename)



