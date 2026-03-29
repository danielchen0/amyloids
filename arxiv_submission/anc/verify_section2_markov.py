#!/usr/bin/python
"""Verify Section 2 Markov chain E(n) against brute force."""

import itertools
from fractions import Fraction


def brute_force_E(n):
    """Brute force: enumerate all 2^n amyloids of A,B, count fluorescences."""
    proteins = ['A', 'B']
    total_fluor = 0
    total_amyloids = 0
    for amyloid in itertools.product(proteins, repeat=n):
        fluor = 0
        fused = [False] * n
        for i in range(1, n):
            if not fused[i-1]:
                if amyloid[i-1] != amyloid[i]:
                    fluor += 1
                    fused[i-1] = True
                    fused[i] = True
        total_fluor += fluor
        total_amyloids += 1
    return Fraction(total_fluor, total_amyloids)


def markov_E(n):
    """E(n) via Markov chain for split-YFP (A,B each prob 1/2)."""
    return Fraction(n - 1, 3) + Fraction(1, 9) * (1 - Fraction(-1, 2)**(n - 1))


print("=== Brute force vs Markov chain E(n) for Section 2 ===")
print(f"{'n':>3}  {'E_brute':>15}  {'E_markov':>15}  {'Match':>6}  {'R(n)':>15}")
for n in range(2, 16):
    eb = brute_force_E(n)
    em = markov_E(n)
    r = 2 * em / n
    ok = eb == em
    print(f"{n:3d}  {str(eb):>15}  {str(em):>15}  {'OK' if ok else 'FAIL':>6}  {float(r):>15.10f}")

print("\n=== Cross-check: Markov E(n) vs generating function R(n) ===")
for n in range(2, 20):
    em = markov_E(n)
    r_markov = 2 * em / n
    # From the generating function closed form:
    r_gf = Fraction(2*(3*n - 2), 9*n) + Fraction(2*(-1)**n, 9*n * 2**(n-1))
    ok = r_markov == r_gf
    print(f"n={n:3d}  R_markov={float(r_markov):.12f}  R_gf={float(r_gf):.12f}  {'OK' if ok else 'FAIL'}")
