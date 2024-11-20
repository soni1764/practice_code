
# 1.----------------------------------------Print all Substring----------------------------------------------------

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


# if __name__ == '__main__':
#     dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#     dict2 = {"a": 1, "b": 2, "c": 3, "d": 6, "f": 10}
#
#     # dict1 = {"a": 1, "b": 2, "c": 3}
#     # dict2 = {"a": 1, "b": 2, "c": 3}
#     compare_dict(dict1, dict2)


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


if __name__ == '__main__':
    s = "aaaabbbccadddbbcccf"
    mc = MyClass()
    mc.format_string_with_occurrence(s, len(s))
