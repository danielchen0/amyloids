#!/usr/bin/python
import itertools
import math

#The binomial coefficient nCk...
def binom(n, k):
    if k > n or k < 0:
        return 0
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n - k)
    return a / (b * c)

def a(n):
    if n == 0:
        return 0
    x = math.sqrt(2)
    result = ((3 + 2 * x) / (x + 2) * 1.0) * pow((1.0 / (-1.0 - x)), n) + \
    ((2 * x - 3) / (x - 2) * 1.0) * pow((1.0 / (x - 1)), n)
    return result

def b(n):
    x = math.sqrt(2)
    result = - (1.0 / (2 * x + 2)) * pow((1.0 / (-1 - x)), n) - \
    (1.0 / (2 - 2 * x)) * pow((1.0 / (x - 1)), n)
    return result

def product(lst):
    val = 1.0
    for item in lst:
        val *= item
    return val

#This is the A(n,k) function I defined in my writeup...
def A(n, k):
    result = 0.0
    for q in range(0, n + 1 - 2 * k):
        all_lists = \
        itertools.product(range(2, n - q - 2 * (k - 1)), repeat=k)
        lists_of_sum_n = [lst for lst in all_lists if sum(lst) == n - q]
        innerSum = 0.0
        for lst in lists_of_sum_n:
            a_lst = [a(phi_i) for phi_i in lst]
            innerSum += product(a_lst)
        result += b(q) * innerSum

    return result

#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def expected_value(length):
    result = 0.0
    for i in range(0, length // 2 + 1):
        result += i * A(length, i)
    result /= pow(3, length)
    return result

if __name__ == '__main__':
    for i in range(2, 1000):
        r = 2 * expected_value(i) / i
        print(f"{i}: {r}")
