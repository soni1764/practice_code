# 1.----------------------------------------Print all Substring----------------------------------------------------
from itertools import permutations


def print_substring(given_string, n):
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += given_string[j]
            print(temp)


# if __name__ == '__main__':
#     s = "English"
#     print_substring(s, len(s))


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
    # dict1 = {"a": 1, "b": 2, "c": 3}
    # dict2 = {"a": 1, "b": 2, "c": 3}
#   compare_dict(dict1, dict2)
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
            if given_string[i] == given_string[i+1]:
                char_list.append(given_string[i])
            else:
                char_list.append(given_string[i])
                if i < n - 2:
                    formatted_string += str(len(char_list)) + given_string[i]
                    char_list = []
        else:
            if given_string[i] == given_string[i-1]:
                formatted_string += str(len(char_list) + 1) + given_string[i]
            else:
                formatted_string += str(len(char_list)) + given_string[i-1] + '1' + given_string[i]

    print(formatted_string)


# if __name__ == '__main__':
#     s = "aaaabbbccadddbbcccf"
#     mc = MyClass()
#     mc.format_string_with_occurrence(s, len(s))
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

        for i in common_prefix:
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
# #     get_per(small_str)
# #     get_per2(small_str)
#     get_per_of_a_in_b(small_str, large_str)



def search_all_perm(given_string, string_to_search):
    pass


# if __name__ == "__main__":
#     search_all_perm("", "")
