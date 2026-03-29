#!/usr/bin/python
"""Generate SplitYFPamyloids.png: R(n) for split-YFP amyloids approaching 2/3."""

import matplotlib.pyplot as plt
from split_yfp_simulation import expected_value

N = 400
ns = list(range(4, N + 4))
rs = [2 * expected_value(n) / n for n in ns]

plt.figure()
plt.plot(ns, rs, color='tab:orange', label='$R(n)$')
plt.axhline(y=2/3, color='tab:blue', linestyle='-', label='$2/3$')
plt.xlabel('$n$')
plt.ylabel('$R(n)$')
plt.title('Expected percentage of proteins involved in fluorescence (split-YFP)')
plt.legend()
plt.tight_layout()
plt.savefig('SplitYFPamyloids.png', dpi=150)
print("Saved SplitYFPamyloids.png")
