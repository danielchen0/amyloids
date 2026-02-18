#!/usr/bin/python
"""Verify Section 3 by brute force enumeration and Markov chain formula."""

import itertools
from fractions import Fraction


def brute_force_E(n):
    """Brute force: enumerate all 3^n amyloids, count fluorescences."""
    proteins = ['A', 'B', 'S']
    total_fluor = 0
    total_amyloids = 0
    for amyloid in itertools.product(proteins, repeat=n):
        fluor = 0
        fused = [False] * n
        for i in range(1, n):
            if not fused[i-1]:
                pair = {amyloid[i-1], amyloid[i]}
                if pair == {'A', 'B'}:
                    fluor += 1
                    fused[i-1] = True
                    fused[i] = True
        total_fluor += fluor
        total_amyloids += 1
    return Fraction(total_fluor, total_amyloids)


def markov_E(n):
    """E(n) via Markov chain: E(n) = (4n-3)/24 - (-1)^(n-1)/(24*3^(n-1))"""
    return Fraction(4*n - 3, 24) - Fraction((-1)**(n-1), 24 * 3**(n-1))


print("=== Brute force vs Markov chain E(n) ===")
print(f"{'n':>3}  {'E_brute':>15}  {'E_markov':>15}  {'Match':>6}  {'R(n)':>15}")
for n in range(2, 9):
    eb = brute_force_E(n)
    em = markov_E(n)
    r = 2 * em / n
    ok = eb == em
    print(f"{n:3d}  {str(eb):>15}  {str(em):>15}  {'OK' if ok else 'FAIL':>6}  {float(r):>15.10f}")

print("\n=== R(n) convergence to 1/3 (Markov chain) ===")
for n in [10, 50, 100, 500, 1000]:
    r = 2 * markov_E(n) / n
    print(f"n={n:5d}  R(n) = {float(r):.15f}  error = {float(r - Fraction(1,3)):.2e}")

print("\n=== Bug check: simulation output for n=6 ===")
print(f"Markov R(6) = {float(2 * markov_E(6) / 6):.10f}")
print(f"Paper   R(6) = 0.0146319159")
print("These differ => simulation has a bug (off-by-one in range upper bound)")
