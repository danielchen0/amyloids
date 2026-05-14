#!/usr/bin/python
"""Verify the finite-n variance formulas by brute force for small n."""

import itertools
from fractions import Fraction


def split_count(amyloid):
    fused = [False] * len(amyloid)
    total = 0
    for i in range(1, len(amyloid)):
        if not fused[i - 1] and amyloid[i] != amyloid[i - 1]:
            total += 1
            fused[i - 1] = True
            fused[i] = True
    return total


def split_sup35_count(amyloid):
    fused = [False] * len(amyloid)
    total = 0
    for i in range(1, len(amyloid)):
        if not fused[i - 1] and {amyloid[i - 1], amyloid[i]} == {"A", "B"}:
            total += 1
            fused[i - 1] = True
            fused[i] = True
    return total


def fret_count(amyloid):
    return sum(
        1
        for i in range(1, len(amyloid))
        if {amyloid[i - 1], amyloid[i]} == {"C", "Y"}
    )


def brute_moments(alphabet, n, counter):
    values = [counter(word) for word in itertools.product(alphabet, repeat=n)]
    total = len(values)
    mean = Fraction(sum(values), total)
    second = Fraction(sum(value * value for value in values), total)
    return mean, second - mean * mean


def var_split(n):
    return (
        Fraction(6 * n + 2, 81)
        + Fraction((12 * n + 2) * (-1) ** n, 81 * 2**n)
        - Fraction(4, 81 * 4**n)
    )


def var_split_sup35(n):
    return (
        Fraction(56 * n - 27, 576)
        + Fraction((4 * n + 3) * (-1) ** n, 48 * 3**n)
        - Fraction(1, 64 * 9**n)
    )


def var_fret(n):
    return Fraction(n - 1, 4)


def var_fret_sup35(n):
    return Fraction(18 * n - 22, 81)


CASES = [
    ("split-YFP", "AB", split_count, var_split),
    ("split-YFP + Sup35p", "ABS", split_sup35_count, var_split_sup35),
    ("FRET", "CY", fret_count, var_fret),
    ("FRET + Sup35p", "CYS", fret_count, var_fret_sup35),
]


for name, alphabet, counter, formula in CASES:
    print(f"=== {name} ===")
    print(f"{'n':>3}  {'E_brute':>12}  {'Var_brute':>14}  {'Var_formula':>14}  match")
    for n in range(2, 8):
        mean, variance = brute_moments(alphabet, n, counter)
        expected_variance = formula(n)
        print(
            f"{n:3d}  {str(mean):>12}  {str(variance):>14}  "
            f"{str(expected_variance):>14}  "
            f"{'OK' if variance == expected_variance else 'FAIL'}"
        )
    print()
