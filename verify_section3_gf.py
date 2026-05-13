#!/usr/bin/python
"""Verify the Section 3 bivariate generating function

    F(z, w) = (1 + z) / (1 - 2 z - (1 + 2w) z^2)

and the rationalized closed forms for a_n and b_n.
"""

import itertools
from fractions import Fraction
import math


def brute_force_distribution(n):
    """A(n, k) = # of {A,B,S}^n amyloids with k greedy fusions."""
    pgf = {}
    for amyloid in itertools.product('ABS', repeat=n):
        fluor = 0
        fused = [False] * n
        for i in range(1, n):
            if not fused[i - 1] and {amyloid[i - 1], amyloid[i]} == {'A', 'B'}:
                fluor += 1
                fused[i - 1] = True
                fused[i] = True
        pgf[fluor] = pgf.get(fluor, 0) + 1
    return pgf


def gf_distribution(n):
    """A(n, k) via the recurrence f_n = 2 f_{n-1} + (1 + 2w) f_{n-2}."""
    f = [{0: 1}, {0: 3}]
    for i in range(2, n + 1):
        t1, t2 = {}, {}
        for k, v in f[i - 1].items():
            t1[k] = t1.get(k, 0) + 2 * v
        for k, v in f[i - 2].items():
            t2[k] = t2.get(k, 0) + v
            t2[k + 1] = t2.get(k + 1, 0) + 2 * v
        merged = dict(t1)
        for k, v in t2.items():
            merged[k] = merged.get(k, 0) + v
        f.append({k: v for k, v in merged.items() if v != 0})
    return f[n]


def a_n_closed(n):
    """a_n = (1 + sqrt(2)/2)(1 - sqrt(2))^n + (1 - sqrt(2)/2)(1 + sqrt(2))^n, n >= 1."""
    if n == 0:
        return 0
    r2 = math.sqrt(2)
    return (1 + r2 / 2) * (1 - r2) ** n + (1 - r2 / 2) * (1 + r2) ** n


def b_n_closed(n):
    """b_n = ((1 + sqrt(2))^{n+1} + (1 - sqrt(2))^{n+1}) / 2."""
    r2 = math.sqrt(2)
    return ((1 + r2) ** (n + 1) + (1 - r2) ** (n + 1)) / 2


def a_n_recur(n):
    """a_n via the recurrence (exact integer)."""
    if n <= 1:
        return 0
    if n == 2:
        return 2
    a_prev2, a_prev1 = 0, 2
    for _ in range(3, n + 1):
        a_prev2, a_prev1 = a_prev1, 2 * a_prev1 + a_prev2
    return a_prev1


def b_n_recur(n):
    """b_n via the recurrence (exact integer)."""
    if n == 0:
        return 1
    if n == 1:
        return 3
    b_prev2, b_prev1 = 1, 3
    for _ in range(2, n + 1):
        b_prev2, b_prev1 = b_prev1, 2 * b_prev1 + b_prev2
    return b_prev1


if __name__ == '__main__':
    print('=== Section 3 GF vs brute force ===')
    print(f'{"n":>3}  {"GF":>50}  {"brute":>50}  {"match":>6}')
    for n in range(2, 8):
        gf = gf_distribution(n)
        bf = brute_force_distribution(n)
        ok = gf == bf
        gf_str = ', '.join(f'{k}:{v}' for k, v in sorted(gf.items()))
        bf_str = ', '.join(f'{k}:{v}' for k, v in sorted(bf.items()))
        print(f'{n:3d}  {gf_str:>50}  {bf_str:>50}  {"OK" if ok else "FAIL":>6}')

    print('\n=== a_n: rationalized closed form vs recurrence ===')
    print(f'{"n":>3}  {"recurrence":>12}  {"closed-form":>20}  {"diff":>12}')
    for n in range(0, 15):
        rec = a_n_recur(n)
        cf = a_n_closed(n)
        diff = abs(rec - cf)
        print(f'{n:3d}  {rec:>12}  {cf:>20.6f}  {diff:>12.2e}')

    print('\n=== b_n: rationalized closed form vs recurrence ===')
    print(f'{"n":>3}  {"recurrence":>12}  {"closed-form":>20}  {"diff":>12}')
    for n in range(0, 15):
        rec = b_n_recur(n)
        cf = b_n_closed(n)
        diff = abs(rec - cf)
        print(f'{n:3d}  {rec:>12}  {cf:>20.6f}  {diff:>12.2e}')
