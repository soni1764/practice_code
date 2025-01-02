# ----------------------------------selection sort---------------------------------------
# # for non duplicate number
# def sort_using_selection_sort(given_list):
#     for i in range(len(given_list)):
#         min_v = min(given_list[i:])
#         min_idx = given_list.index(min_v)
#         given_list[i], given_list[min_idx] = given_list[min_idx], given_list[i]
#         print(given_list)


# work on duplicates
def sort_using_selection_sort2(given_list):
    # len(given_list)-1, because last element will be on last position no need to iterate
    for i in range(len(given_list)-1):
        min_v = min(given_list[i:])
        # start from i
        min_idx = given_list.index(min_v, i)
        # doing swapping only if nums are not equal
        if given_list[i] != given_list[min_idx]:
            given_list[i], given_list[min_idx] = given_list[min_idx], given_list[i]
        # print(given_list)
    print(given_list)


# work on duplicates
def sort_using_selection_sort3(given_list):
    # len(given_list)-1, because last element will be on last position no need to iterate
    for i in range(len(given_list)-1):
        min_idx = i
        for j in range(i+1, len(given_list)):
            if given_list[j] < given_list[min_idx]:
                min_idx = j
        # doing swapping only if nums are not equal
        if given_list[i] != given_list[min_idx]:
            given_list[i], given_list[min_idx] = given_list[min_idx], given_list[i]
        # print(given_list)
    print(given_list)


# if __name__ == '__main__':
#     # l_ = [56, 3, 2, 78, 6, 0]
#     l_ = [56, 3, 2, 78, 6, 0, 6]
#     # sort_using_selection_sort2(l_)
#     sort_using_selection_sort3(l_)


# ------------------------------------bubble sort----------------------------------------------
def sort_number(given_list):
    n = len(given_list)
    for i in range(n-1):
        for j in range(i+1, n):
            if given_list[j] < given_list[i]:
                given_list[i], given_list[j] = given_list[j], given_list[i]
    print(given_list)


def sort_number_using_bubble_sort(given_list):
    for i in range(len(given_list)-1):
        for j in range(len(given_list)-1-i):
            if given_list[j+1] < given_list[j]:
                given_list[j], given_list[j+1] = given_list[j+1], given_list[j]
            # print(given_list)
        # print(given_list)
    # print(given_list)


# if __name__ == '__main__':
#     # l_ = [56, 3, 2, 78, 6, 0]
#     l_ = [56, 3, 2, 78, 6, 0, 6]
#     # sort_number(l_)
#     sort_number_using_bubble_sort(l_)


# ------------------------------------quick sort----------------------------------------------
def sort_number2(given_list):
    for i in range(len(given_list)-1):
        for j in range(len(given_list)-1-i):
            if given_list[j+1] < given_list[j]:
                given_list[j], given_list[j+1] = given_list[j+1], given_list[j]
            # print(given_list)
        # print(given_list)
    # print(given_list)


if __name__ == '__main__':
    # l_ = [56, 3, 2, 78, 6, 0]
    l_ = [56, 3, 2, 78, 6, 0, 6]
    # sort_number(l_)
    sort_number2(l_)