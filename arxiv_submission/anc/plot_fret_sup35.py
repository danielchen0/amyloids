#!/usr/bin/python
"""Generate FretandSup35.png: R(n) for FRET YFP/CFP + Sup35p approaching 2/9."""

import matplotlib.pyplot as plt

# R(n) = 2(n-1)/(9n) by linearity of expectation
N = 400
ns = list(range(2, N + 2))
rs = [2 * (n - 1) / (9 * n) for n in ns]

plt.figure()
plt.plot(ns, rs, color='tab:orange', label='$R(n)$')
plt.axhline(y=2/9, color='tab:blue', linestyle='-', label='$2/9$')
plt.xlabel('$n$')
plt.ylabel('$R(n)$')
plt.title('Expected total yellow fluorescence ratio (FRET YFP/CFP + Sup35p)')
plt.legend()
plt.tight_layout()
plt.savefig('FretandSup35.png', dpi=150)
print("Saved FretandSup35.png")
