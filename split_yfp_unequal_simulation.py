#!/usr/bin/python
"""Monte Carlo verification of the corrected Section 6.1 formula.

The paper's original (incorrect) two-state Markov chain gave
    R_SY -> 4 alpha (1 - alpha) / (1 + 2 alpha (1 - alpha))
while the corrected three-state chain gives
    R_SY -> 2 alpha (1 - alpha) / (1 - alpha (1 - alpha))
The two agree at alpha = 1/2 (both -> 2/3) and diverge elsewhere.
"""

import random
from fractions import Fraction


def correct_R(alpha):
    """Corrected formula: 2 alpha (1-alpha) / (1 - alpha(1-alpha))."""
    return 2 * alpha * (1 - alpha) / (1 - alpha * (1 - alpha))


def old_wrong_R(alpha):
    """Paper's original (incorrect) formula."""
    return 4 * alpha * (1 - alpha) / (1 + 2 * alpha * (1 - alpha))


def simulate_R(alpha, n, trials, seed=0):
    """Simulate R_SY(n) at protein-A probability alpha."""
    rng = random.Random(seed)
    total = 0.0
    for _ in range(trials):
        seq = ['A' if rng.random() < alpha else 'B' for _ in range(n)]
        fluor = 0
        fused = [False] * n
        for i in range(1, n):
            if not fused[i - 1] and seq[i - 1] != seq[i]:
                fluor += 1
                fused[i - 1] = True
                fused[i] = True
        total += 2 * fluor / n
    return total / trials


if __name__ == '__main__':
    print('Section 6.1 corrected formula vs Monte Carlo simulation:')
    print('  R_SY(n -> infty) = 2 alpha (1-alpha) / (1 - alpha(1-alpha))')
    print()
    print(f'  {"alpha":>8}  {"correct":>10}  {"old(wrong)":>12}  {"MC":>10}  {"match":>10}')
    n = 5000
    trials = 400
    for alpha in [0.1, 0.2, 0.25, Fraction(1, 3), 0.4, 0.5, 0.6, 0.75, 0.8, 0.9]:
        a = float(alpha)
        correct = correct_R(a)
        old = old_wrong_R(a)
        mc = simulate_R(a, n=n, trials=trials)
        if abs(mc - correct) < 0.01:
            tag = 'correct'
        elif abs(mc - old) < 0.01:
            tag = 'old'
        else:
            tag = '?'
        print(f'  {a:>8.4f}  {correct:>10.6f}  {old:>12.6f}  {mc:>10.6f}  {tag:>10}')

    print()
    print('Symmetric point check (alpha = 1/2): both formulas give 2/3')
    print(f'  correct(0.5) = {correct_R(0.5):.10f}')
    print(f'  old(0.5)     = {old_wrong_R(0.5):.10f}')
    print(f'  2/3          = {2/3:.10f}')

    print()
    print('Numerical contrast at alpha = 1/4:')
    print(f'  correct = 2 * (1/4)(3/4) / (1 - 3/16) = {Fraction(2) * Fraction(1, 4) * Fraction(3, 4) / (1 - Fraction(1, 4) * Fraction(3, 4))}')
    print(f'  old     = 4 * (1/4)(3/4) / (1 + 3/8) = {4 * Fraction(1, 4) * Fraction(3, 4) / (1 + 2 * Fraction(1, 4) * Fraction(3, 4))}')
