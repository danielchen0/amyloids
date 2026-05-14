#!/usr/bin/python
"""Verify the Section 5 bivariate transfer-matrix generating function

    F(z, w) = (1 + (1-w) z) / (1 - (2+w) z - (1-w) z^2)

against brute-force enumeration. The paper's original block-decomposition
formula over-counts due to block-boundary coupling (verified separately);
the transfer-matrix derivation does not have this problem.
"""

import itertools
from fractions import Fraction


def brute_force_distribution(n):
    """Brute force: A(n, k) = # of {C,Y,S}^n amyloids with k adjacent {C,Y} pairs."""
    pgf = {}
    for amyloid in itertools.product('CYS', repeat=n):
        k = sum(1 for i in range(1, n) if {amyloid[i-1], amyloid[i]} == {'C', 'Y'})
        pgf[k] = pgf.get(k, 0) + 1
    return pgf


def gf_distribution(n):
    """Compute A(n, k) from the GF recurrence f_n = (2+w) f_{n-1} + (1-w) f_{n-2}."""
    # Represent f_n as dict {k: A(n, k)}
    f = [{0: 1}, {0: 3}]  # f_0 = 1, f_1 = 3
    for i in range(2, n + 1):
        t1, t2 = {}, {}
        for k, v in f[i - 1].items():
            t1[k] = t1.get(k, 0) + 2 * v
            t1[k + 1] = t1.get(k + 1, 0) + v
        for k, v in f[i - 2].items():
            t2[k] = t2.get(k, 0) + v
            t2[k + 1] = t2.get(k + 1, 0) - v
        merged = dict(t1)
        for k, v in t2.items():
            merged[k] = merged.get(k, 0) + v
        f.append({k: v for k, v in merged.items() if v != 0})
    return f[n]


def E_from_gf(n):
    """E(n) from the GF distribution."""
    dist = gf_distribution(n)
    total = sum(v for v in dist.values())
    weighted = sum(k * v for k, v in dist.items())
    return Fraction(weighted, total)


if __name__ == '__main__':
    print('=== Section 5 transfer-matrix GF vs brute force ===')
    print(f'{"n":>3}  {"GF distribution":>40}  {"Brute force":>40}  {"match":>6}')
    all_ok = True
    for n in range(2, 9):
        gf = gf_distribution(n)
        bf = brute_force_distribution(n)
        ok = gf == bf
        all_ok = all_ok and ok
        gf_str = ', '.join(f'A({n},{k})={v}' for k, v in sorted(gf.items()))
        bf_str = ', '.join(f'A({n},{k})={v}' for k, v in sorted(bf.items()))
        print(f'{n:3d}  {gf_str:>40}  {bf_str:>40}  {"OK" if ok else "FAIL":>6}')
    print(f'\nAll match: {all_ok}')

    print('\n=== E(n) = 2(n-1)/9 cross-check ===')
    for n in range(2, 9):
        e_gf = E_from_gf(n)
        e_paper = Fraction(2 * (n - 1), 9)
        ok = e_gf == e_paper
        print(f'  n={n}: E_gf = {e_gf}, paper = {e_paper}  {"OK" if ok else "FAIL"}')
