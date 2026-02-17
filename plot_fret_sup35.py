#!/usr/bin/python
"""Generate FretandSup35.png: R(n) for FRET YFP/CFP + Sup35p amyloids."""

import matplotlib.pyplot as plt
from fret_sup35_simulation import expected_value

N = 15
ns = list(range(2, N + 1))
rs = [expected_value(n) / n for n in ns]

plt.figure()
plt.plot(ns, rs, color='tab:orange', marker='o', label='$R(n)$')
plt.xlabel('$n$')
plt.ylabel('$R(n)$')
plt.title('Expected total yellow fluorescence ratio (FRET YFP/CFP + Sup35p)')
plt.legend()
plt.tight_layout()
plt.savefig('FretandSup35.png', dpi=150)
print("Saved FretandSup35.png")
