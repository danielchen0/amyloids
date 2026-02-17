#!/usr/bin/python
"""Verify the intermediate algebra steps in lines 248-250."""

from fractions import Fraction

def R_line248(n):
    """Line 248: direct substitution of closed forms."""
    s1 = (Fraction(2)**n * (3*n + 2) + 2*(6*n - 1)*(-1)**n) / 27
    s2 = (Fraction(2)**n * (3*n - 4) - 2*(3*n - 2)*(-1)**n) / 27
    return (s1 + 2*s2) / (n * Fraction(2)**(n-1))

def R_line249_paper(n):
    """Line 249 as written in paper (with the factor of 2)."""
    t = Fraction((-1)**n, 2**(n-1))
    part1 = (2*(3 + Fraction(2,n)) + 2*(6 - Fraction(1,n)) * t) / 27
    part2 = 4 * ((3 - Fraction(4,n)) - 2*(3 - Fraction(2,n)) * t) / 27
    return part1 + part2

def R_line249_fixed(n):
    """Line 249 with the factor of 2 removed."""
    t = Fraction((-1)**n, 2**(n-1))
    part1 = (2*(3 + Fraction(2,n)) + 2*(6 - Fraction(1,n)) * t) / 27
    part2 = 4 * ((3 - Fraction(4,n)) - (3 - Fraction(2,n)) * t) / 27
    return part1 + part2

print(f"{'n':>4}  {'line248':>20}  {'line249_paper':>20}  {'line249_fixed':>20}  paper_ok  fixed_ok")
for n in range(2, 21):
    v248 = R_line248(n)
    v249p = R_line249_paper(n)
    v249f = R_line249_fixed(n)
    print(f"{n:4d}  {float(v248):20.15f}  {float(v249p):20.15f}  {float(v249f):20.15f}  {'OK' if v248 == v249p else 'FAIL':>8}  {'OK' if v248 == v249f else 'FAIL':>8}")
