#!/usr/bin/python
"""Generate splityfpandsup35.png: R(n) for split-YFP + Sup35p amyloids approaching 1/3."""

import matplotlib.pyplot as plt
from sup35_simulation import expected_value

N = 26
ns = list(range(2, N + 1))
rs = [2 * expected_value(n) / n for n in ns]

plt.figure()
plt.plot(ns, rs, color='tab:orange', label='$R(n)$')
plt.axhline(y=1/3, color='tab:blue', linestyle='-', label='$1/3$')
plt.xlabel('$n$')
plt.ylabel('$R(n)$')
plt.title('Expected percentage of proteins involved in fluorescence (split-YFP + Sup35p)')
plt.legend()
plt.tight_layout()
plt.savefig('splityfpandsup35.png', dpi=150)
print("Saved splityfpandsup35.png")
