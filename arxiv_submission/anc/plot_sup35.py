#!/usr/bin/python
"""Generate splityfpandsup35.png: R(n) for split-YFP + Sup35p approaching 1/3."""

import matplotlib.pyplot as plt

# R(n) = (4n-3)/(12n) + (-1)^n / (12n * 3^(n-1)) by Markov chain derivation
N = 400
ns = list(range(2, N + 2))
rs = [(4*n - 3) / (12*n) + ((-1)**n) / (12*n * 3**(n-1)) for n in ns]

plt.figure()
plt.plot(ns, rs, color='tab:orange', label='$R(n)$')
plt.axhline(y=1/3, color='tab:blue', linestyle='-', label='$1/3$')
plt.xlabel('$n$')
plt.ylabel('$R(n)$')
plt.title('Expected percentage of proteins involved\nin fluorescence (split-YFP + Sup35p)')
plt.legend()
plt.tight_layout()
plt.savefig('splityfpandsup35.png', dpi=150)
print("Saved splityfpandsup35.png")
