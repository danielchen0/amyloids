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

def a(n,y):
    if n <= y:
        return 0
    x = math.sqrt(2)
    result = - ((4 + 3 * x) / (x + 2) * 1.0) * pow((1.0/(-1.0-x)),n-y) - \
    ((4 - 3 * x) / (2 - x) * 1.0) * pow((1.0 / (x - 1)), n - y)
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
    for q in range(0, n - k + 1):
        innerSum = 0.0
        for i in range(1, k + 1):
            all_lists = itertools.product(range(1, n - q + 1), repeat=i)
            lists_of_psi = [lst for lst in all_lists if sum(lst) == k]
            all_lists = itertools.product(range(2, n - q + 1), repeat=i)
            lists_of_sum_n=[lst for lst in all_lists if sum(lst)==n - q]
            for lst in lists_of_sum_n:
                for lst2 in lists_of_psi:
                    fin = zip(lst,lst2)
                    a_lst = [a(x,y) for x,y in fin]
                    innerSum += product(a_lst)
        result += b(q) * innerSum
    return result

#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def expected_value(length):
    result = 0.0
    for i in range(0, length):
        result += i * A(length, i)
    result /= pow(3.0, length)
    return result

if __name__ == '__main__':
    for i in range(1, 1000):
        r = expected_value(i) / i
        print(f"{i}: {r}")
