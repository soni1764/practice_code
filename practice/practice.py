import sys


# ------------check even/ odd---------------------
def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


# if __name__ == '__main__':
#     print(check_even_odd(9))


# ------------get even/ odd---------------------
def get_even_odd(given_list):
    e_l = []
    o_l = []
    for i in given_list:
        type_o_n = check_even_odd(i)
        if type_o_n == "even":
            e_l.append(i)
        else:
            o_l.append(i)

    print(f'Even num list: {e_l}')
    print(f'Odd num list: {o_l}')


# if __name__ == '__main__':
#     get_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])

# ------------check positive or negative ---------------------
def check_pos_neg(n):
    if n > 0:
        return "positive"
    elif n == 0:
        return "zero"
    else:
        return "negative"


# if __name__ == '__main__':
#     print(check_pos_neg(18))

def get_pos_neg(given_list):
    p_n = []
    n_n = []
    z_n = []
    for i in given_list:
        type_o_n = check_pos_neg(i)
        if type_o_n == "positive":
            p_n.append(i)
        elif type_o_n == "negative":
            n_n.append(i)
        else:
            z_n.append(i)
    print(f'Original list: {p_n}')
    print(f'Positive nums: {p_n}')
    print(f'Negative nums: {n_n}')
    print(f'Zero nums: {z_n}')


# if __name__ == '__main__':
#     get_pos_neg([1,2 , 3, 4, 0, -5, -2, -3, 0])


# --------------sum of num in a list ---------------

def sum_num_in_list_num(given_list):
    s = 0
    for i in given_list:
        s += i
    print(f"Sum is: {s}")


# if __name__ == "__main__":
#     nums = []
#     print("hello")
#     count = int(input("Enter total how many numbers you want to sum up:\n"))
#     for num in range(count):
#         nums.append(int(input(f"Enter number\n")))
#     sum_num_in_list_num(nums)


# ------------sum of n positive nums ---------------------
def sum_n_pos_num_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_n_pos_num_recursion(n - 1)


def sum_n_pos_num(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("enter num\n"))
#     except ValueError:
#         print("Please enter integer number")
#         sys.exit("Stopping execution")
#     except Exception as e:
#         print(e)
#         sys.exit("Stopping execution")
#     print(sum_n_pos_num(num))
#     print(sum_n_pos_num_recursion(num))


# ------------sum of n*n, n*n*n positive nums ---------------------
def sum_sqr_n_p_num(n):
    s = 0
    for i in range(n + 1):
        s = s + i * i
    print(s)


def sum_sqr_n_p_num_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * n + sum_sqr_n_p_num_rec(n - 1)


def sum_cube_n_p_num_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * n * n + sum_cube_n_p_num_rec(n - 1)


# if __name__ == '__main__':
#     try:
#         num = int(input("enter num\n"))
#     except ValueError:
#         print("enter integer nums")
#         sys.exit("Stopping exe")
#     except Exception as e:
#         print(e)
#         sys.exit("Stopping exe")
#
#     sum_sqr_n_p_num(num)
#     print(sum_sqr_n_p_num_rec(num))
#     print(sum_cube_n_p_num_rec(num))


# -------------------------------prime-----------------------------------
def is_prime(n):
    flag = False
    if n >= 2:
        for i in range(2, int(n // 2) + 1):
            if n % i == 0:
                break
        else:
            flag = True
            return flag
    else:
        return flag
    return flag


def get_prime(given_list):
    p_l = []
    for n in given_list:
        status = is_prime(n)
        if status:
            p_l.append(n)
    print(f"Prime nums: {p_l}")


# if __name__ == '__main__':
#     try:
#         num = int(input("enter num\n"))
#         print(f"Is {num} prime")
#     except ValueError:
#         print("enter integer nums")
#         sys.exit("Stopping exe")
#     except Exception as e:
#         print(e)
#         sys.exit("Stopping exe")
#
#     print(is_prime(num))
#     get_prime([1, 2, 3, 4, 5, 6, 7, 8, 9])


# --------------------------------is palindrome------------------------
def is_palindrome(n):
    new_num = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        new_num = (new_num * 10) + digit
        temp = temp // 10
    print(new_num, n)
    if new_num == n:
        print("Yes")
    else:
        print("No")


def reverse_num_rec(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse_num_rec(n // 10)))


def is_palindrome2(n):
    if n == reverse_num_rec(n):
        print("Yes")
    else:
        print("No")


# if __name__ == '__main__':
#     try:
#         num = int(input("enter num\n"))
#         print(f"Is {num} Palindrome ?")
#     except ValueError:
#         print("enter integer nums")
#         sys.exit("Stopping exe")
#     except Exception as e:
#         print(e)
#         sys.exit("Stopping exe")
#     is_palindrome(num)
#     is_palindrome2(1881)


# --------------------------------is Armstrong------------------------
def is_armstrong(n):
    new_num = 0
    temp = n
    power = len(str(n))
    while temp > 0:
        digit = temp % 10
        new_num = new_num + digit ** power
        temp = temp // 10
    if new_num == n:
        print("Yes")
    else:
        print("No")


# if __name__ == '__main__':
#     try:
#         num = int(input("enter num\n"))
#         print(f"Is {num} arm ?")
#     except ValueError:
#         print("enter integer nums")
#         sys.exit("Stopping exe")
#     except Exception as e:
#         print(e)
#         sys.exit("Stopping exe")
#     is_armstrong(num)


# ---------------------------------Fibonacci----------------------------------------------------------
def get_fibonacci_series(n):
    n1 = 0
    n2 = 1
    while n >= 0:
        print(n1, end=' ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        n -= 1


def nth_fibonacci_number(n):
    n1 = 0
    n2 = 1
    nth = 0
    while n >= 0:
        nth = n1
        print(n1, end=' ')
        next_ = n1 + n2
        n1 = n2
        n2 = next_
        n -= 1
    print()
    print(nth)


def nth_fibonacci_number_rec(n):
    if n <= 1:
        return n
    else:
        return nth_fibonacci_number_rec(n - 1) + nth_fibonacci_number_rec(n - 2)


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#
    # get_fibonacci_series(10)
    # nth_fibonacci_number(10)
    # print(nth_fibonacci_number_rec(10))


# -----------------------pattern------------------------------------------------
def print_pattern(n):
    for row in range(n):
        for i in range(0, n - row - 1):
            print(end=' ')
        for col in range(row + 1):
            print('* ', end='')
        print()


def print_pattern2(n):
    num_ = 65
    for row in range(n):
        for col in range(row + 1):
            print(chr(num_), end=' ')
        num_ += 1
        print()


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     print_pattern(5)
#     print_pattern2(5)


# ---------------------------Largest num--------------------------------------------------
def get_largest_num(given_list):
    l_n = given_list[0]
    for num_ in given_list:
        if num_ > l_n:
            l_n = num_
    print(l_n)


def sec_largest(given_list):
    l_n = given_list[0]
    sec_l_n = 0
    for num_ in given_list:
        if num_ > l_n:
            sec_l_n = l_n
            l_n = num_
        elif num_ > sec_l_n and num_ != l_n:
            sec_l_n = num_
    print(l_n, sec_l_n)


def n_largest(given_list, n):
    new_l = []
    for i in range(n):
        l_n = given_list[0]
        for num_ in given_list:
            if num_ > l_n:
                l_n = num_
        new_l.append(l_n)
        given_list.remove(l_n)
    print(new_l)


# if __name__ == '__main__':
    # get_largest_num([1, 3, 5, 10, 6, 40, 7, 90, 4, 2])
    # sec_largest([1, 3, 5, 10, 6, 40, 7, 90, 4, 2, 100, 2, 1, 1, 98])
    # n_largest([1, 3, 5, 10, 6, 40, 7, 90, 4, 11, 100, 16, 9, 8, 98], 3)


# ------------------------Reverse string----------------------------------------------------

def reverse_string(s):
    rev_s = ''
    for char in s:
        rev_s = char + rev_s
    print(rev_s)


def rev_word_in_string(s):
    rev_s = ''
    for word in s.split():
        new_word = ''
        for char in word:
            new_word = char + new_word
        rev_s = rev_s + " " + new_word
    print(rev_s.strip())


def reverse_num(n):
    temp = n
    rev_n = 0
    while temp > 0:
        rem = temp % 10
        rev_n = rev_n * 10 + rem
        temp = temp // 10
    print(rev_n)


# if __name__ == '__main__':
#     reverse_string("Gourav")
#     rev_word_in_string("Gourav Soni From Verint")
#     reverse_num(12345)


# ---------------------------Factorial----------------------------------------------------

def get_factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    print(fac)


def get_factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * get_factorial_rec(n - 1)


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     get_factorial(num)
#     print(get_factorial_rec(num))


# -----------------------------Is Binary----------------------------------------------

def is_Binary(n):
    while n > 0:
        d = n % 10
        if d not in [0, 1]:
            return False
        n //= 10
    return True


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     print(is_Binary(101))


# -----------------------------Sum of digit-----------------------------------------------------

def sum_of_digit(n):
    sum_ = 0
    while n > 0:
        dig = n % 10
        sum_ += dig
        n = n // 10
    return sum_


def sum_of_digit_rec(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digit(n // 10)


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     print(sum_of_digit(num))
#     print(sum_of_digit_rec(num))

# ------------------Factor of a number-------------------------------------------------------------

def prime_fac(n):
    i = 2
    while i <= n:
        if n % i:
            i += 1
        else:
            print(i, end=' ')
            n = n // i


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     prime_fac(10)


# -----------------------Number Is perfect ----sum of factor(except self) == number-----------------------------------

def is_perfect(n):
    sum_ = 0
    for i in range(1, int(n // 2) + 1):
        if n % i == 0:
            sum_ += i
    if sum_ == n:
        print("Yes")
    else:
        print("No")


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     is_perfect(num)


# --------------------get first n prime nums-------------------------------------------------
def is_prime2(n):
    if n >= 2:
        for i in range(2, int(n // 2) + 1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


def get_n_prime(n):
    p_n_l = []
    num_ = 2
    while len(p_n_l) <= n:
        if is_prime2(num_):
            p_n_l.append(num_)
        num_ += 1
    print(p_n_l)


def get_primes(n1, n2):
    for i in range(n1, n2 + 1):
        if is_prime2(i):
            print(i, end=' ')


# if __name__ == '__main__':
#     num = 0
#     try:
#         num = int(input("Enter num\n"))
#         while num < 0:
#             num = int(input("Enter a positive number num\n"))
#     except Exception as e:
#         print(e)
#     is_prime2(num)
#     get_n_prime(num)
#     get_primes(1, 20)


# ------------------------------------Get LCM------------------------------------
def get_LCM(n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while True:
        if (greater % n1 == 0) & (greater % n2 == 0):
            lcm = greater
            break
        greater += 1
    print(lcm)


# if __name__ == '__main__':
#     get_LCM(10, 20)


# ------------------------------------Get HCF------------------------------------
def get_HCF(n1, n2):
    if n1 < n2:
        smaller = n1
    else:
        smaller = n2
    while True:
        if (n1 % smaller == 0) & (n2 % smaller == 0):
            hcf = smaller
            break
        smaller -= 1
    print(hcf)


def get_HCF2(n1, n2):
    if n2 == 0:
        return n1
    else:
        return get_HCF2(n2, n1 % n2)


# if __name__ == '__main__':
#     get_HCF(10, 20)
#     get_HCF2(10, 20)


# ------------------------------dec to bin-------------------------------------------------
def dec_bin(n):
    l_n = []
    while n >= 1:
        l_n.insert(0, n % 2)
        n //= 2
    print(*l_n, end='')


def dec_bin_rec(n):
    l_ = []
    if n >= 1:
        l_.insert(0, n % 2)
        dec_bin_rec(n // 2)
    print(*l_, end='')


# if __name__ == '__main__':
#     dec_bin(10)
#     print()
#     dec_bin_rec(10)


