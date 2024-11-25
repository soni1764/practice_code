from itertools import permutations


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


if __name__ == "__main__":
    small_str = "abc"
    large_str = "cbabadcbbabbcbabaabccbabc"
    # get_per(small_str)
    # get_per2(small_str)
    get_per_of_a_in_b(small_str, large_str)






