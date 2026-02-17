#!/usr/bin/python
"""Verify the closed-form sum identities and algebra in Section 2.4/2.5."""

from fractions import Fraction
import math


def binom(n, k):
    if k < 0 or k > n:
        return Fraction(0)
    return Fraction(math.comb(n, k))


def sum1_direct(n):
    """Compute sum_{k=1}^{floor(n/2)} k * 2^k * C(n-k-1, k-1) directly."""
    total = Fraction(0)
    for k in range(1, n // 2 + 1):
        total += k * Fraction(2)**k * binom(n - k - 1, k - 1)
    return total


def sum1_closed(n):
    """Closed form: (2^n (3n+2) + 2(6n-1)(-1)^n) / 27"""
    return (Fraction(2)**n * (3*n + 2) + 2 * (6*n - 1) * (-1)**n) / 27


def sum2_direct(n):
    """Compute sum_{k=1}^{floor(n/2)} k * 2^k * C(n-k-1, k) directly."""
    total = Fraction(0)
    for k in range(1, n // 2 + 1):
        total += k * Fraction(2)**k * binom(n - k - 1, k)
    return total


def sum2_closed(n):
    """Closed form: (2^n (3n-4) - 2(3n-2)(-1)^n) / 27"""
    return (Fraction(2)**n * (3*n - 4) - 2 * (3*n - 2) * (-1)**n) / 27


def R_direct(n):
    """R(n) computed from scratch using A(n,k)."""
    total = Fraction(0)
    for k in range(0, n // 2 + 1):
        A_nk = (Fraction(2)**k * binom(n - k - 1, k - 1)
                + Fraction(2)**(k + 1) * binom(n - k - 1, k))
        total += k * A_nk
    return total / (n * Fraction(2)**(n - 1))


def R_closed(n):
    """R(n) from the closed-form sums."""
    return (sum1_closed(n) + 2 * sum2_closed(n)) / (n * Fraction(2)**(n - 1))


if __name__ == '__main__':
    print("=== Verifying Sum Identity 1 ===")
    print(f"{'n':>4}  {'Direct':>30}  {'Closed':>30}  {'Match':>6}")
    all_ok = True
    for n in range(2, 51):
        d = sum1_direct(n)
        c = sum1_closed(n)
        ok = d == c
        if not ok:
            all_ok = False
        print(f"{n:4d}  {str(d):>30}  {str(c):>30}  {'OK' if ok else 'FAIL':>6}")
    print(f"\nSum 1 all match: {all_ok}\n")

    print("=== Verifying Sum Identity 2 ===")
    print(f"{'n':>4}  {'Direct':>30}  {'Closed':>30}  {'Match':>6}")
    all_ok2 = True
    for n in range(2, 51):
        d = sum2_direct(n)
        c = sum2_closed(n)
        ok = d == c
        if not ok:
            all_ok2 = False
        print(f"{n:4d}  {str(d):>30}  {str(c):>30}  {'OK' if ok else 'FAIL':>6}")
    print(f"\nSum 2 all match: {all_ok2}\n")

    print("=== Verifying R(n) direct vs closed ===")
    all_ok3 = True
    for n in range(2, 51):
        rd = R_direct(n)
        rc = R_closed(n)
        ok = rd == rc
        if not ok:
            all_ok3 = False
        print(f"n={n:3d}  R_direct={float(rd):.10f}  R_closed={float(rc):.10f}  {'OK' if ok else 'FAIL'}")
    print(f"\nR(n) all match: {all_ok3}\n")

    print("=== R(n) convergence to 2/3 ===")
    for n in [10, 50, 100, 500, 1000]:
        r = R_direct(n)
        print(f"n={n:5d}  R(n) = {float(r):.15f}  error = {float(r - Fraction(2,3)):.2e}")
