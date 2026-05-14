#!/usr/bin/python
"""Monte Carlo verification of the unequal-concentration split-YFP formulas.

The paper's original (incorrect) two-state Markov chain gave
    R_SY -> 4 alpha (1 - alpha) / (1 + 2 alpha (1 - alpha))
while the corrected three-state chain gives
    R_SY -> 2 alpha (1 - alpha) / (1 - alpha (1 - alpha))
The two agree at alpha = 1/2 (both -> 2/3) and diverge elsewhere.

With Sup35p at probabilities P(A)=alpha, P(B)=beta, P(S)=1-alpha-beta,
the corresponding limit is
    R_SY -> 2 alpha beta (2 - alpha - beta) / (1 - alpha beta).
"""

import random
from fractions import Fraction


def correct_R(alpha):
    """Corrected formula: 2 alpha (1-alpha) / (1 - alpha(1-alpha))."""
    return 2 * alpha * (1 - alpha) / (1 - alpha * (1 - alpha))


def old_wrong_R(alpha):
    """Paper's original (incorrect) formula."""
    return 4 * alpha * (1 - alpha) / (1 + 2 * alpha * (1 - alpha))


def correct_sup35_R(alpha, beta):
    """Corrected formula with Sup35p at probability 1-alpha-beta."""
    return 2 * alpha * beta * (2 - alpha - beta) / (1 - alpha * beta)


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


def simulate_sup35_R(alpha, beta, n, trials, seed=1):
    """Simulate R_SY(n) with A/B/S probabilities alpha/beta/remaining."""
    rng = random.Random(seed)
    total = 0.0
    for _ in range(trials):
        seq = []
        for _ in range(n):
            roll = rng.random()
            if roll < alpha:
                seq.append('A')
            elif roll < alpha + beta:
                seq.append('B')
            else:
                seq.append('S')
        fluor = 0
        fused = [False] * n
        for i in range(1, n):
            if not fused[i - 1] and {seq[i - 1], seq[i]} == {'A', 'B'}:
                fluor += 1
                fused[i - 1] = True
                fused[i] = True
        total += 2 * fluor / n
    return total / trials


if __name__ == '__main__':
    print('Split-YFP unequal-concentration formula vs Monte Carlo simulation:')
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

    print()
    print('Split-YFP + Sup35p unequal-concentration formula vs Monte Carlo simulation:')
    print('  R_SY(n -> infty) = 2 alpha beta (2-alpha-beta) / (1 - alpha beta)')
    print()
    print(f'  {"alpha":>8}  {"beta":>8}  {"formula":>10}  {"MC":>10}  {"match":>10}')
    for alpha, beta in [
        (0.10, 0.10),
        (0.20, 0.30),
        (0.25, 0.25),
        (1 / 3, 1 / 3),
        (0.40, 0.20),
        (0.45, 0.45),
    ]:
        formula = correct_sup35_R(alpha, beta)
        mc = simulate_sup35_R(alpha, beta, n=n, trials=trials)
        tag = 'correct' if abs(mc - formula) < 0.01 else '?'
        print(f'  {alpha:>8.4f}  {beta:>8.4f}  {formula:>10.6f}  {mc:>10.6f}  {tag:>10}')
