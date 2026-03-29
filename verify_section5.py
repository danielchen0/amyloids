#!/usr/bin/python
"""Verify Section 5 (FRET + Sup35p) by brute force.

Total yellow fluorescence = number of adjacent {C,Y} pairs.
By linearity of expectation, E(n) = (n-1) * 2/9.
"""

import itertools
from fractions import Fraction


def brute_force_E(n):
    """Brute force: enumerate all 3^n amyloids, count adjacent {C,Y} pairs."""
    proteins = ['C', 'Y', 'S']
    total_fluor = 0
    total_amyloids = 0
    for amyloid in itertools.product(proteins, repeat=n):
        fluor = 0
        for i in range(1, n):
            if {amyloid[i-1], amyloid[i]} == {'C', 'Y'}:
                fluor += 1
        total_fluor += fluor
        total_amyloids += 1
    return Fraction(total_fluor, total_amyloids)


def linearity_E(n):
    """E(n) = (n-1) * 2/9 by linearity of expectation."""
    return Fraction(2 * (n - 1), 9)


print("=== Brute force vs linearity of expectation E(n) for Section 5 ===")
print(f"{'n':>3}  {'E_brute':>15}  {'E_formula':>15}  {'Match':>6}  {'R(n)':>15}")
for n in range(2, 9):
    eb = brute_force_E(n)
    ef = linearity_E(n)
    r = ef / n
    ok = eb == ef
    print(f"{n:3d}  {str(eb):>15}  {str(ef):>15}  {'OK' if ok else 'FAIL':>6}  {float(r):>15.10f}")

print(f"\n=== R(n) -> 2/9 = {float(Fraction(2,9)):.10f} ===")
for n in [10, 50, 100, 1000]:
    r = linearity_E(n) / n
    print(f"n={n:5d}  R(n) = {float(r):.15f}  error = {float(r - Fraction(2,9)):.2e}")

print("\n=== Bug in paper's simulation ===")
print(f"Correct   R(10) = {float(linearity_E(10)/10):.10f}")
print(f"Paper     R(10) = 0.203698623177")
print("Paper used floor(n/2) as upper limit for k, but FRET allows k up to n-1")
